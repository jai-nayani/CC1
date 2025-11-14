"""
Database connection and session management.
"""
import json
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid
import aiosqlite
from pathlib import Path


class Database:
    """Async SQLite database manager."""

    def __init__(self, db_path: str = "coherence.db"):
        """Initialize database."""
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Ensure database file exists."""
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        """Initialize database schema."""
        async with aiosqlite.connect(self.db_path) as db:
            # Entries table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS entries (
                    id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    type TEXT NOT NULL,
                    tags TEXT,
                    ai_categories TEXT,
                    ai_entities TEXT,
                    ai_summary TEXT,
                    ai_sentiment TEXT,
                    ai_key_phrases TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    view_count INTEGER DEFAULT 0,
                    last_accessed TEXT
                )
            """)

            # Actions table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS actions (
                    id TEXT PRIMARY KEY,
                    entry_id TEXT NOT NULL,
                    description TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    due_date TEXT,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY (entry_id) REFERENCES entries (id) ON DELETE CASCADE
                )
            """)

            # Relationships table (for graph connections)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS relationships (
                    id TEXT PRIMARY KEY,
                    source_id TEXT NOT NULL,
                    target_id TEXT NOT NULL,
                    weight REAL NOT NULL,
                    type TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY (source_id) REFERENCES entries (id) ON DELETE CASCADE,
                    FOREIGN KEY (target_id) REFERENCES entries (id) ON DELETE CASCADE
                )
            """)

            # Create indexes
            await db.execute("CREATE INDEX IF NOT EXISTS idx_entries_created_at ON entries(created_at)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_entries_type ON entries(type)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_actions_entry_id ON actions(entry_id)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_actions_status ON actions(status)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_relationships_source ON relationships(source_id)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_relationships_target ON relationships(target_id)")

            await db.commit()

    async def create_entry(self, entry_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new entry."""
        entry_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO entries (
                    id, content, type, tags, ai_categories, ai_entities,
                    ai_summary, ai_sentiment, ai_key_phrases,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entry_id,
                entry_data['content'],
                entry_data['type'],
                json.dumps(entry_data.get('tags', [])),
                json.dumps(entry_data.get('ai_categories', [])),
                json.dumps(entry_data.get('ai_entities', [])),
                entry_data.get('ai_summary'),
                json.dumps(entry_data.get('ai_sentiment')),
                json.dumps(entry_data.get('ai_key_phrases', [])),
                now,
                now
            ))
            await db.commit()

        return await self.get_entry(entry_id)

    async def get_entry(self, entry_id: str) -> Optional[Dict[str, Any]]:
        """Get entry by ID."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("SELECT * FROM entries WHERE id = ?", (entry_id,)) as cursor:
                row = await cursor.fetchone()
                if row:
                    return self._row_to_dict(row)
        return None

    async def list_entries(
        self,
        limit: int = 50,
        offset: int = 0,
        type_filter: Optional[str] = None,
        tag_filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List entries with filters."""
        query = "SELECT * FROM entries WHERE 1=1"
        params = []

        if type_filter:
            query += " AND type = ?"
            params.append(type_filter)

        if tag_filter:
            query += " AND tags LIKE ?"
            params.append(f'%"{tag_filter}"%')

        query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, params) as cursor:
                rows = await cursor.fetchall()
                return [self._row_to_dict(row) for row in rows]

    async def update_entry(self, entry_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an entry."""
        now = datetime.utcnow().isoformat()
        set_clauses = []
        params = []

        for key, value in updates.items():
            if key in ['content', 'type']:
                set_clauses.append(f"{key} = ?")
                params.append(value)
            elif key == 'tags':
                set_clauses.append("tags = ?")
                params.append(json.dumps(value))

        if not set_clauses:
            return await self.get_entry(entry_id)

        set_clauses.append("updated_at = ?")
        params.append(now)
        params.append(entry_id)

        query = f"UPDATE entries SET {', '.join(set_clauses)} WHERE id = ?"

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(query, params)
            await db.commit()

        return await self.get_entry(entry_id)

    async def delete_entry(self, entry_id: str) -> bool:
        """Delete an entry."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
            await db.commit()
            return True

    async def create_action(self, action_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create an action."""
        action_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO actions (id, entry_id, description, priority, due_date, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                action_id,
                action_data['entry_id'],
                action_data['description'],
                action_data.get('priority', 'medium'),
                action_data.get('due_date'),
                action_data.get('status', 'pending'),
                now
            ))
            await db.commit()

        return await self.get_action(action_id)

    async def get_action(self, action_id: str) -> Optional[Dict[str, Any]]:
        """Get action by ID."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("SELECT * FROM actions WHERE id = ?", (action_id,)) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
        return None

    async def list_actions(self, entry_id: Optional[str] = None, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """List actions with filters."""
        query = "SELECT * FROM actions WHERE 1=1"
        params = []

        if entry_id:
            query += " AND entry_id = ?"
            params.append(entry_id)

        if status:
            query += " AND status = ?"
            params.append(status)

        query += " ORDER BY created_at DESC"

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, params) as cursor:
                rows = await cursor.fetchall()
                return [dict(row) for row in rows]

    async def update_action(self, action_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an action."""
        set_clauses = []
        params = []

        for key, value in updates.items():
            if key in ['description', 'priority', 'due_date', 'status']:
                set_clauses.append(f"{key} = ?")
                params.append(value)

        if not set_clauses:
            return await self.get_action(action_id)

        params.append(action_id)
        query = f"UPDATE actions SET {', '.join(set_clauses)} WHERE id = ?"

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(query, params)
            await db.commit()

        return await self.get_action(action_id)

    async def create_relationship(self, source_id: str, target_id: str, weight: float, rel_type: str) -> Dict[str, Any]:
        """Create a relationship between entries."""
        rel_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO relationships (id, source_id, target_id, weight, type, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (rel_id, source_id, target_id, weight, rel_type, now))
            await db.commit()

        return {
            'id': rel_id,
            'source_id': source_id,
            'target_id': target_id,
            'weight': weight,
            'type': rel_type,
            'created_at': now
        }

    async def get_relationships(self, entry_id: str) -> List[Dict[str, Any]]:
        """Get relationships for an entry."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute("""
                SELECT * FROM relationships
                WHERE source_id = ? OR target_id = ?
                ORDER BY weight DESC
            """, (entry_id, entry_id)) as cursor:
                rows = await cursor.fetchall()
                return [dict(row) for row in rows]

    def _row_to_dict(self, row: aiosqlite.Row) -> Dict[str, Any]:
        """Convert SQLite row to dictionary."""
        d = dict(row)
        # Parse JSON fields
        for field in ['tags', 'ai_categories', 'ai_entities', 'ai_key_phrases']:
            if d.get(field):
                try:
                    d[field] = json.loads(d[field])
                except json.JSONDecodeError:
                    d[field] = []
        if d.get('ai_sentiment'):
            try:
                d['ai_sentiment'] = json.loads(d['ai_sentiment'])
            except json.JSONDecodeError:
                d['ai_sentiment'] = None
        return d


# Global database instance
db = Database()
