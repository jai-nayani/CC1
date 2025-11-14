"""
API routes for entries management.
"""
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.models.entry import (
    Entry,
    EntryCreate,
    EntryUpdate,
    SearchResult,
    KnowledgeGraph
)
from app.db.database import db
from app.services.ai_processor import ai_processor
from app.services.semantic_search import semantic_search
from app.services.knowledge_graph import knowledge_graph
from datetime import datetime
import uuid

router = APIRouter()


@router.post("/entries", response_model=Entry, status_code=201)
async def create_entry(entry_data: EntryCreate):
    """
    Create a new entry with AI processing.

    This endpoint:
    1. Accepts the entry content
    2. Processes it with AI to extract insights
    3. Generates embeddings for semantic search
    4. Builds knowledge graph connections
    5. Returns the enriched entry
    """
    try:
        # Process content with AI
        ai_result = await ai_processor.process_entry(entry_data.content)

        # Create entry in database
        entry_dict = {
            'content': entry_data.content,
            'type': entry_data.type.value,
            'tags': entry_data.tags,
            'ai_categories': ai_result.categories,
            'ai_entities': [e.dict() for e in ai_result.entities],
            'ai_summary': ai_result.summary,
            'ai_sentiment': ai_result.sentiment,
            'ai_key_phrases': ai_result.key_phrases,
        }

        created_entry = await db.create_entry(entry_dict)
        entry_id = created_entry['id']

        # Add to semantic search
        await semantic_search.add_entry(
            entry_id,
            entry_data.content,
            {'type': entry_data.type.value, 'categories': ai_result.categories}
        )

        # Add to knowledge graph
        await knowledge_graph.add_entry_node(
            entry_id,
            entry_data.content,
            {
                'created_at': created_entry['created_at'],
                'categories': ai_result.categories,
                'entities': [e.dict() for e in ai_result.entities]
            }
        )

        # Build connections
        await knowledge_graph.build_connections(entry_id)

        # Create actions if extracted
        extracted_actions = []
        for action in ai_result.actions:
            action_dict = {
                'entry_id': entry_id,
                'description': action.description,
                'priority': action.priority.value,
                'due_date': action.due_date.isoformat() if action.due_date else None,
                'status': action.status.value
            }
            created_action = await db.create_action(action_dict)
            extracted_actions.append(created_action)

        # Build response
        response = Entry(
            id=entry_id,
            content=entry_data.content,
            type=entry_data.type,
            tags=entry_data.tags,
            created_at=datetime.fromisoformat(created_entry['created_at']),
            updated_at=datetime.fromisoformat(created_entry['updated_at']),
            ai_categories=ai_result.categories,
            ai_entities=ai_result.entities,
            ai_summary=ai_result.summary,
            ai_sentiment=ai_result.sentiment,
            ai_key_phrases=ai_result.key_phrases,
            extracted_actions=[],
            related_entry_ids=[],
            view_count=0
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating entry: {str(e)}")


@router.get("/entries", response_model=List[Entry])
async def list_entries(
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    type: Optional[str] = None,
    tag: Optional[str] = None
):
    """
    List entries with optional filters.

    Supports pagination and filtering by type and tags.
    """
    try:
        entries = await db.list_entries(
            limit=limit,
            offset=offset,
            type_filter=type,
            tag_filter=tag
        )

        result = []
        for entry_data in entries:
            # Get actions for this entry
            actions = await db.list_actions(entry_id=entry_data['id'])

            result.append(Entry(
                id=entry_data['id'],
                content=entry_data['content'],
                type=entry_data['type'],
                tags=entry_data.get('tags', []),
                created_at=datetime.fromisoformat(entry_data['created_at']),
                updated_at=datetime.fromisoformat(entry_data['updated_at']),
                ai_categories=entry_data.get('ai_categories', []),
                ai_entities=entry_data.get('ai_entities', []),
                ai_summary=entry_data.get('ai_summary'),
                ai_sentiment=entry_data.get('ai_sentiment'),
                ai_key_phrases=entry_data.get('ai_key_phrases', []),
                extracted_actions=[],
                related_entry_ids=[],
                view_count=entry_data.get('view_count', 0)
            ))

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing entries: {str(e)}")


@router.get("/entries/{entry_id}", response_model=Entry)
async def get_entry(entry_id: str):
    """
    Get a specific entry by ID.

    Returns full entry details including AI insights and related information.
    """
    try:
        entry_data = await db.get_entry(entry_id)
        if not entry_data:
            raise HTTPException(status_code=404, detail="Entry not found")

        # Get related entries from graph
        similar = await semantic_search.find_similar(entry_id, limit=5)
        related_ids = [s['entry_id'] for s in similar]

        # Get actions
        actions = await db.list_actions(entry_id=entry_id)

        return Entry(
            id=entry_data['id'],
            content=entry_data['content'],
            type=entry_data['type'],
            tags=entry_data.get('tags', []),
            created_at=datetime.fromisoformat(entry_data['created_at']),
            updated_at=datetime.fromisoformat(entry_data['updated_at']),
            ai_categories=entry_data.get('ai_categories', []),
            ai_entities=entry_data.get('ai_entities', []),
            ai_summary=entry_data.get('ai_summary'),
            ai_sentiment=entry_data.get('ai_sentiment'),
            ai_key_phrases=entry_data.get('ai_key_phrases', []),
            extracted_actions=[],
            related_entry_ids=related_ids,
            view_count=entry_data.get('view_count', 0)
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting entry: {str(e)}")


@router.put("/entries/{entry_id}", response_model=Entry)
async def update_entry(entry_id: str, update_data: EntryUpdate):
    """Update an existing entry."""
    try:
        # Check if entry exists
        existing = await db.get_entry(entry_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Entry not found")

        # Update database
        updates = {}
        if update_data.content is not None:
            updates['content'] = update_data.content
        if update_data.type is not None:
            updates['type'] = update_data.type.value
        if update_data.tags is not None:
            updates['tags'] = update_data.tags

        updated_entry = await db.update_entry(entry_id, updates)

        # If content changed, reprocess with AI
        if update_data.content is not None:
            await semantic_search.update_entry(
                entry_id,
                update_data.content,
                {'type': updated_entry['type']}
            )

        return Entry(
            id=updated_entry['id'],
            content=updated_entry['content'],
            type=updated_entry['type'],
            tags=updated_entry.get('tags', []),
            created_at=datetime.fromisoformat(updated_entry['created_at']),
            updated_at=datetime.fromisoformat(updated_entry['updated_at']),
            ai_categories=updated_entry.get('ai_categories', []),
            ai_entities=updated_entry.get('ai_entities', []),
            ai_summary=updated_entry.get('ai_summary'),
            ai_sentiment=updated_entry.get('ai_sentiment'),
            ai_key_phrases=updated_entry.get('ai_key_phrases', []),
            extracted_actions=[],
            related_entry_ids=[],
            view_count=updated_entry.get('view_count', 0)
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating entry: {str(e)}")


@router.delete("/entries/{entry_id}", status_code=204)
async def delete_entry(entry_id: str):
    """Delete an entry."""
    try:
        # Check if exists
        existing = await db.get_entry(entry_id)
        if not existing:
            raise HTTPException(status_code=404, detail="Entry not found")

        # Delete from all systems
        await db.delete_entry(entry_id)
        await semantic_search.delete_entry(entry_id)
        await knowledge_graph.remove_entry(entry_id)

        return None

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting entry: {str(e)}")


@router.get("/search", response_model=List[SearchResult])
async def search_entries(
    query: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1, le=50)
):
    """
    Perform semantic search across all entries.

    Uses AI embeddings to find relevant entries by meaning, not just keywords.
    """
    try:
        # Perform semantic search
        search_results = await semantic_search.search(query, limit=limit)

        # Fetch full entry details
        results = []
        for result in search_results:
            entry_data = await db.get_entry(result['entry_id'])
            if entry_data:
                entry = Entry(
                    id=entry_data['id'],
                    content=entry_data['content'],
                    type=entry_data['type'],
                    tags=entry_data.get('tags', []),
                    created_at=datetime.fromisoformat(entry_data['created_at']),
                    updated_at=datetime.fromisoformat(entry_data['updated_at']),
                    ai_categories=entry_data.get('ai_categories', []),
                    ai_entities=entry_data.get('ai_entities', []),
                    ai_summary=entry_data.get('ai_summary'),
                    ai_sentiment=entry_data.get('ai_sentiment'),
                    ai_key_phrases=entry_data.get('ai_key_phrases', []),
                    extracted_actions=[],
                    related_entry_ids=[],
                    view_count=entry_data.get('view_count', 0)
                )

                results.append(SearchResult(
                    entry=entry,
                    score=result['score'],
                    highlights=[]
                ))

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching: {str(e)}")


@router.get("/graph", response_model=KnowledgeGraph)
async def get_knowledge_graph(
    entry_id: Optional[str] = None,
    depth: int = Query(2, ge=1, le=3),
    min_weight: float = Query(0.5, ge=0.0, le=1.0)
):
    """
    Get knowledge graph visualization.

    If entry_id is provided, returns a subgraph centered on that entry.
    Otherwise, returns the full graph.
    """
    try:
        if entry_id:
            graph = await knowledge_graph.get_subgraph(entry_id, depth, min_weight)
        else:
            graph = await knowledge_graph.get_full_graph(min_weight)

        return graph

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting graph: {str(e)}")
