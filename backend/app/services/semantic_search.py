"""
Semantic Search Service using ChromaDB for vector similarity search.
"""
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings as ChromaSettings
from app.core.config import settings
from app.services.ai_processor import ai_processor


class SemanticSearchService:
    """Semantic search using vector embeddings."""

    def __init__(self):
        """Initialize semantic search service."""
        self.client = None
        self.collection = None
        self._initialized = False

    async def initialize(self):
        """Initialize ChromaDB client and collection."""
        if self._initialized:
            return

        # Initialize ChromaDB
        self.client = chromadb.Client(ChromaSettings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.CHROMA_PERSIST_DIR
        ))

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION_NAME,
            metadata={"description": "Coherence entry embeddings"}
        )

        self._initialized = True

    async def add_entry(self, entry_id: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """
        Add entry to vector database.

        Args:
            entry_id: Unique entry identifier
            content: Text content to embed
            metadata: Additional metadata
        """
        await self.initialize()

        # Generate embedding
        embedding = await ai_processor.generate_embedding(content)

        # Add to collection
        self.collection.add(
            ids=[entry_id],
            embeddings=[embedding],
            documents=[content],
            metadatas=[metadata or {}]
        )

        # Persist changes
        self.client.persist()

    async def update_entry(self, entry_id: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Update entry in vector database."""
        await self.initialize()

        # Generate new embedding
        embedding = await ai_processor.generate_embedding(content)

        # Update in collection
        self.collection.update(
            ids=[entry_id],
            embeddings=[embedding],
            documents=[content],
            metadatas=[metadata or {}]
        )

        self.client.persist()

    async def delete_entry(self, entry_id: str):
        """Delete entry from vector database."""
        await self.initialize()

        try:
            self.collection.delete(ids=[entry_id])
            self.client.persist()
        except Exception:
            # Entry might not exist, ignore
            pass

    async def search(
        self,
        query: str,
        limit: int = 10,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Perform semantic search.

        Args:
            query: Search query
            limit: Maximum number of results
            filters: Optional metadata filters

        Returns:
            List of search results with scores
        """
        await self.initialize()

        # Generate query embedding
        query_embedding = await ai_processor.generate_embedding(query)

        # Search in collection
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=limit,
            where=filters
        )

        # Format results
        search_results = []
        if results['ids'] and results['ids'][0]:
            for i, entry_id in enumerate(results['ids'][0]):
                search_results.append({
                    'entry_id': entry_id,
                    'score': 1 - results['distances'][0][i],  # Convert distance to similarity
                    'content': results['documents'][0][i] if results['documents'] else None,
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {}
                })

        return search_results

    async def find_similar(
        self,
        entry_id: str,
        limit: int = 5,
        threshold: float = None
    ) -> List[Dict[str, Any]]:
        """
        Find entries similar to a given entry.

        Args:
            entry_id: Entry to find similar entries for
            limit: Maximum number of results
            threshold: Minimum similarity threshold

        Returns:
            List of similar entries with scores
        """
        await self.initialize()

        threshold = threshold or settings.SIMILARITY_THRESHOLD

        # Get entry embedding
        try:
            entry = self.collection.get(ids=[entry_id], include=['embeddings'])
            if not entry['embeddings']:
                return []

            embedding = entry['embeddings'][0]

            # Search for similar entries
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=limit + 1  # +1 to exclude the entry itself
            )

            # Format and filter results
            similar_entries = []
            if results['ids'] and results['ids'][0]:
                for i, result_id in enumerate(results['ids'][0]):
                    if result_id == entry_id:
                        continue  # Skip the entry itself

                    similarity = 1 - results['distances'][0][i]
                    if similarity >= threshold:
                        similar_entries.append({
                            'entry_id': result_id,
                            'score': similarity,
                            'content': results['documents'][0][i] if results['documents'] else None,
                            'metadata': results['metadatas'][0][i] if results['metadatas'] else {}
                        })

            return similar_entries[:limit]

        except Exception:
            return []

    async def get_all_embeddings(self) -> Dict[str, List[float]]:
        """Get all embeddings from the collection."""
        await self.initialize()

        try:
            results = self.collection.get(include=['embeddings'])
            embeddings = {}
            if results['ids']:
                for i, entry_id in enumerate(results['ids']):
                    if results['embeddings'] and i < len(results['embeddings']):
                        embeddings[entry_id] = results['embeddings'][i]
            return embeddings
        except Exception:
            return {}

    async def count(self) -> int:
        """Get total number of entries in collection."""
        await self.initialize()
        return self.collection.count()


# Global semantic search instance
semantic_search = SemanticSearchService()
