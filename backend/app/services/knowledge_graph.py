"""
Knowledge Graph Service - Build and query dynamic knowledge graphs.
"""
from typing import List, Dict, Any, Optional, Set, Tuple
import networkx as nx
from datetime import datetime
from app.models.entry import KnowledgeGraph, GraphNode, GraphEdge
from app.services.semantic_search import semantic_search
from app.db.database import db


class KnowledgeGraphService:
    """Service for building and querying knowledge graphs."""

    def __init__(self):
        """Initialize knowledge graph service."""
        self.graph = nx.DiGraph()
        self._initialized = False

    async def initialize(self):
        """Initialize graph from database."""
        if self._initialized:
            return

        # Load all entries and relationships from database
        await self._rebuild_graph()
        self._initialized = True

    async def _rebuild_graph(self):
        """Rebuild graph from database."""
        self.graph.clear()

        # This would load from database in production
        # For now, graph will be built incrementally

    async def add_entry_node(
        self,
        entry_id: str,
        content: str,
        metadata: Dict[str, Any]
    ):
        """
        Add an entry as a node in the knowledge graph.

        Args:
            entry_id: Unique entry identifier
            content: Entry content
            metadata: Entry metadata (categories, entities, etc.)
        """
        await self.initialize()

        self.graph.add_node(
            entry_id,
            content=content,
            label=content[:50] + "..." if len(content) > 50 else content,
            type='entry',
            created_at=metadata.get('created_at', datetime.utcnow().isoformat()),
            categories=metadata.get('categories', []),
            entities=metadata.get('entities', []),
            view_count=0
        )

    async def build_connections(self, entry_id: str):
        """
        Build connections for a new entry based on similarity and entities.

        Args:
            entry_id: Entry to build connections for
        """
        await self.initialize()

        if entry_id not in self.graph:
            return

        # Find similar entries using semantic search
        similar_entries = await semantic_search.find_similar(entry_id, limit=5)

        for similar in similar_entries:
            similar_id = similar['entry_id']
            if similar_id in self.graph:
                weight = similar['score']
                self.graph.add_edge(
                    entry_id,
                    similar_id,
                    weight=weight,
                    type='similarity'
                )

                # Save relationship to database
                await db.create_relationship(
                    entry_id,
                    similar_id,
                    weight,
                    'similarity'
                )

        # Build entity-based connections
        await self._build_entity_connections(entry_id)

        # Build temporal connections (entries created around same time)
        await self._build_temporal_connections(entry_id)

    async def _build_entity_connections(self, entry_id: str):
        """Build connections based on shared entities."""
        if entry_id not in self.graph:
            return

        node_entities = set(
            entity['text']
            for entity in self.graph.nodes[entry_id].get('entities', [])
        )

        if not node_entities:
            return

        # Find other nodes with overlapping entities
        for other_id, other_data in self.graph.nodes(data=True):
            if other_id == entry_id or other_data.get('type') != 'entry':
                continue

            other_entities = set(
                entity['text']
                for entity in other_data.get('entities', [])
            )

            shared_entities = node_entities.intersection(other_entities)
            if shared_entities:
                # Calculate weight based on number of shared entities
                weight = len(shared_entities) / max(len(node_entities), len(other_entities))

                if weight > 0.3:  # Threshold for connection
                    self.graph.add_edge(
                        entry_id,
                        other_id,
                        weight=weight,
                        type='entity',
                        shared_entities=list(shared_entities)
                    )

                    await db.create_relationship(entry_id, other_id, weight, 'entity')

    async def _build_temporal_connections(self, entry_id: str):
        """Build connections to temporally related entries."""
        if entry_id not in self.graph:
            return

        node_time = self.graph.nodes[entry_id].get('created_at')
        if not node_time:
            return

        try:
            node_datetime = datetime.fromisoformat(node_time)
        except:
            return

        # Find entries created within 24 hours
        for other_id, other_data in self.graph.nodes(data=True):
            if other_id == entry_id or other_data.get('type') != 'entry':
                continue

            other_time = other_data.get('created_at')
            if not other_time:
                continue

            try:
                other_datetime = datetime.fromisoformat(other_time)
                time_diff = abs((node_datetime - other_datetime).total_seconds())

                # If within 24 hours, create temporal connection
                if time_diff < 86400:  # 24 hours
                    weight = 1 - (time_diff / 86400)  # Closer in time = higher weight

                    self.graph.add_edge(
                        entry_id,
                        other_id,
                        weight=weight,
                        type='temporal'
                    )

                    await db.create_relationship(entry_id, other_id, weight, 'temporal')
            except:
                continue

    async def get_subgraph(
        self,
        entry_id: str,
        depth: int = 2,
        min_weight: float = 0.5
    ) -> KnowledgeGraph:
        """
        Get a subgraph centered on a specific entry.

        Args:
            entry_id: Center entry
            depth: How many hops to include
            min_weight: Minimum edge weight to include

        Returns:
            KnowledgeGraph containing nodes and edges
        """
        await self.initialize()

        if entry_id not in self.graph:
            return KnowledgeGraph(nodes=[], edges=[])

        # BFS to find nodes within depth
        visited = {entry_id}
        current_level = {entry_id}
        all_nodes = {entry_id}

        for _ in range(depth):
            next_level = set()
            for node in current_level:
                # Get neighbors
                for neighbor in self.graph.neighbors(node):
                    edge_data = self.graph.edges[node, neighbor]
                    if edge_data.get('weight', 0) >= min_weight and neighbor not in visited:
                        next_level.add(neighbor)
                        all_nodes.add(neighbor)
                        visited.add(neighbor)

                # Also check incoming edges
                for predecessor in self.graph.predecessors(node):
                    edge_data = self.graph.edges[predecessor, node]
                    if edge_data.get('weight', 0) >= min_weight and predecessor not in visited:
                        next_level.add(predecessor)
                        all_nodes.add(predecessor)
                        visited.add(predecessor)

            current_level = next_level

        # Build nodes list
        nodes = []
        for node_id in all_nodes:
            node_data = self.graph.nodes[node_id]
            nodes.append(GraphNode(
                id=node_id,
                label=node_data.get('label', node_id),
                type=node_data.get('type', 'entry'),
                size=node_data.get('view_count', 0) + 1,
                metadata={
                    'categories': node_data.get('categories', []),
                    'created_at': node_data.get('created_at')
                }
            ))

        # Build edges list
        edges = []
        for source, target, edge_data in self.graph.edges(data=True):
            if source in all_nodes and target in all_nodes:
                if edge_data.get('weight', 0) >= min_weight:
                    edges.append(GraphEdge(
                        source=source,
                        target=target,
                        weight=edge_data['weight'],
                        type=edge_data.get('type', 'unknown'),
                        label=edge_data.get('type', '')
                    ))

        return KnowledgeGraph(
            nodes=nodes,
            edges=edges,
            metadata={
                'center_node': entry_id,
                'depth': depth,
                'total_nodes': len(nodes),
                'total_edges': len(edges)
            }
        )

    async def get_full_graph(self, min_weight: float = 0.5) -> KnowledgeGraph:
        """Get the entire knowledge graph."""
        await self.initialize()

        nodes = []
        for node_id, node_data in self.graph.nodes(data=True):
            nodes.append(GraphNode(
                id=node_id,
                label=node_data.get('label', node_id),
                type=node_data.get('type', 'entry'),
                size=node_data.get('view_count', 0) + 1,
                metadata={
                    'categories': node_data.get('categories', []),
                    'created_at': node_data.get('created_at')
                }
            ))

        edges = []
        for source, target, edge_data in self.graph.edges(data=True):
            if edge_data.get('weight', 0) >= min_weight:
                edges.append(GraphEdge(
                    source=source,
                    target=target,
                    weight=edge_data['weight'],
                    type=edge_data.get('type', 'unknown'),
                    label=edge_data.get('type', '')
                ))

        return KnowledgeGraph(
            nodes=nodes,
            edges=edges,
            metadata={
                'total_nodes': len(nodes),
                'total_edges': len(edges)
            }
        )

    async def find_paths(
        self,
        source_id: str,
        target_id: str,
        max_length: int = 5
    ) -> List[List[str]]:
        """
        Find paths between two entries.

        Args:
            source_id: Starting entry
            target_id: Ending entry
            max_length: Maximum path length

        Returns:
            List of paths (each path is a list of entry IDs)
        """
        await self.initialize()

        if source_id not in self.graph or target_id not in self.graph:
            return []

        try:
            # Find all simple paths up to max_length
            paths = nx.all_simple_paths(
                self.graph,
                source_id,
                target_id,
                cutoff=max_length
            )
            return list(paths)[:5]  # Limit to 5 paths
        except nx.NetworkXNoPath:
            return []

    async def get_central_nodes(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get most central/important nodes using PageRank.

        Args:
            limit: Number of nodes to return

        Returns:
            List of nodes with centrality scores
        """
        await self.initialize()

        if len(self.graph.nodes()) == 0:
            return []

        # Calculate PageRank
        pagerank = nx.pagerank(self.graph, weight='weight')

        # Sort by score
        sorted_nodes = sorted(
            pagerank.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

        result = []
        for node_id, score in sorted_nodes:
            node_data = self.graph.nodes[node_id]
            result.append({
                'entry_id': node_id,
                'centrality_score': score,
                'label': node_data.get('label', ''),
                'categories': node_data.get('categories', [])
            })

        return result

    async def remove_entry(self, entry_id: str):
        """Remove entry from graph."""
        await self.initialize()

        if entry_id in self.graph:
            self.graph.remove_node(entry_id)


# Global knowledge graph instance
knowledge_graph = KnowledgeGraphService()
