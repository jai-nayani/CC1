"""
JARVIS API Endpoints - WebSocket and HTTP endpoints for conversational AI.
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, Depends
from typing import List, Dict, Any, Optional
import json
import asyncio
from datetime import datetime

from app.services.jarvis_agent import (
    JARVISAgent,
    UserContext,
    AgentMessage
)
from app.services.semantic_search import semantic_search
from app.services.knowledge_graph import knowledge_graph
from app.db.database import db
from app.core.config import settings

router = APIRouter()

# Initialize JARVIS agent
jarvis = None

def get_jarvis() -> JARVISAgent:
    """Get or create JARVIS instance."""
    global jarvis
    if jarvis is None:
        if not settings.OPENAI_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="JARVIS requires OpenAI API key. Please set OPENAI_API_KEY in environment."
            )
        jarvis = JARVISAgent(
            openai_api_key=settings.OPENAI_API_KEY,
            model="gpt-4-turbo-preview",
            streaming=True
        )
    return jarvis


class ConnectionManager:
    """Manage WebSocket connections."""

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        """Connect a new client."""
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: str):
        """Disconnect a client."""
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def send_message(self, message: Dict[str, Any], client_id: str):
        """Send message to specific client."""
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(json.dumps(message))


manager = ConnectionManager()


async def build_user_context(
    user_id: str,
    query: str,
    conversation_history: List[Dict[str, Any]] = None
) -> UserContext:
    """
    Build comprehensive user context for JARVIS.

    This includes:
    - Relevant entries from semantic search
    - Knowledge graph summary
    - User preferences
    - Recent activity
    - Active goals
    """

    # Semantic search for relevant entries
    search_results = await semantic_search.search(query, limit=20)

    relevant_entries = []
    for result in search_results:
        entry_data = await db.get_entry(result['entry_id'])
        if entry_data:
            relevant_entries.append(entry_data)

    # Get knowledge graph summary
    try:
        graph = await knowledge_graph.get_full_graph(min_weight=0.6)
        central_nodes = await knowledge_graph.get_central_nodes(limit=10)
        graph_summary = {
            "total_nodes": len(graph.nodes),
            "total_edges": len(graph.edges),
            "central_concepts": [node["label"] for node in central_nodes]
        }
    except:
        graph_summary = {}

    # Extract user preferences from recent entries
    user_preferences = {
        "tech_stack": [],
        "priorities": [],
        "working_style": "focused"  # Could be extracted from entries
    }

    # Get recent activity (last 10 entries)
    recent_entries = await db.list_entries(limit=10, offset=0)
    recent_activity = [
        {
            "type": entry["type"],
            "created_at": entry["created_at"],
            "categories": entry.get("ai_categories", [])
        }
        for entry in recent_entries
    ]

    # Extract active goals from entries
    # (In production, this would be a dedicated goals table)
    active_goals = []
    for entry in relevant_entries[:5]:
        content = entry.get("content", "").lower()
        if "goal:" in content or "objective:" in content:
            active_goals.append(entry.get("content", "")[:100])

    return UserContext(
        user_id=user_id,
        relevant_entries=relevant_entries,
        knowledge_graph_summary=graph_summary,
        user_preferences=user_preferences,
        recent_activity=recent_activity,
        active_goals=active_goals,
        conversation_history=conversation_history or []
    )


@router.websocket("/ws/jarvis/{client_id}")
async def jarvis_websocket(websocket: WebSocket, client_id: str):
    """
    WebSocket endpoint for real-time JARVIS conversations.

    Protocol:
    - Client sends: {"query": "user question", "user_id": "user123", "history": [...]}
    - Server streams: {"type": "thinking|progress|partial|complete", "content": "...", ...}
    """
    await manager.connect(websocket, client_id)

    try:
        agent = get_jarvis()

        while True:
            # Receive query from client
            data = await websocket.receive_text()
            message = json.loads(data)

            query = message.get("query")
            user_id = message.get("user_id", "default_user")
            conversation_history = message.get("history", [])

            if not query:
                await manager.send_message(
                    {
                        "type": "error",
                        "content": "Query is required",
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    client_id
                )
                continue

            # Build user context
            user_context = await build_user_context(user_id, query, conversation_history)

            # Process query and stream responses
            async for agent_message in agent.process_query(query, user_context):
                await manager.send_message(
                    agent_message.to_dict(),
                    client_id
                )

                # Small delay to prevent overwhelming the client
                await asyncio.sleep(0.01)

    except WebSocketDisconnect:
        manager.disconnect(client_id)
    except Exception as e:
        await manager.send_message(
            {
                "type": "error",
                "content": f"Server error: {str(e)}",
                "timestamp": datetime.utcnow().isoformat()
            },
            client_id
        )
        manager.disconnect(client_id)


@router.post("/jarvis/query")
async def jarvis_http_query(
    query: str,
    user_id: str = "default_user",
    conversation_history: List[Dict[str, Any]] = None
):
    """
    HTTP endpoint for JARVIS queries (non-streaming).

    Use this for:
    - Testing
    - Batch processing
    - Clients that don't support WebSocket
    """
    try:
        agent = get_jarvis()

        # Build context
        user_context = await build_user_context(
            user_id,
            query,
            conversation_history or []
        )

        # Collect all messages
        messages = []
        async for agent_message in agent.process_query(query, user_context):
            messages.append(agent_message.to_dict())

        return {
            "success": True,
            "query": query,
            "messages": messages,
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/jarvis/health")
async def jarvis_health():
    """Check if JARVIS is ready."""
    try:
        agent = get_jarvis()
        return {
            "status": "operational",
            "model": agent.model,
            "streaming": agent.streaming,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }
