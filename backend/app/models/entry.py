"""
Data models for entries and related entities.
"""
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


class EntryType(str, Enum):
    """Type of entry."""
    NOTE = "note"
    TASK = "task"
    IDEA = "idea"
    REFERENCE = "reference"
    MEETING = "meeting"
    DECISION = "decision"


class Priority(str, Enum):
    """Priority level."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class ActionStatus(str, Enum):
    """Status of extracted actions."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class EntryBase(BaseModel):
    """Base entry model."""
    content: str = Field(..., min_length=1, description="Main content of the entry")
    type: EntryType = Field(default=EntryType.NOTE, description="Type of entry")
    tags: List[str] = Field(default_factory=list, description="User-defined tags")


class EntryCreate(EntryBase):
    """Model for creating a new entry."""
    pass


class EntryUpdate(BaseModel):
    """Model for updating an entry."""
    content: Optional[str] = None
    type: Optional[EntryType] = None
    tags: Optional[List[str]] = None


class ExtractedEntity(BaseModel):
    """Extracted entity from text."""
    text: str
    label: str  # PERSON, ORG, DATE, GPE, etc.
    start: int
    end: int


class ExtractedAction(BaseModel):
    """Extracted action/task from entry."""
    id: Optional[str] = None
    description: str
    priority: Priority = Priority.MEDIUM
    due_date: Optional[datetime] = None
    status: ActionStatus = ActionStatus.PENDING
    entry_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AIProcessingResult(BaseModel):
    """Result of AI processing."""
    categories: List[str] = Field(default_factory=list)
    entities: List[ExtractedEntity] = Field(default_factory=list)
    actions: List[ExtractedAction] = Field(default_factory=list)
    summary: Optional[str] = None
    sentiment: Optional[Dict[str, float]] = None
    key_phrases: List[str] = Field(default_factory=list)


class Entry(EntryBase):
    """Complete entry model with AI processing results."""
    id: str
    created_at: datetime
    updated_at: datetime

    # AI-generated fields
    ai_categories: List[str] = Field(default_factory=list)
    ai_entities: List[ExtractedEntity] = Field(default_factory=list)
    ai_summary: Optional[str] = None
    ai_sentiment: Optional[Dict[str, float]] = None
    ai_key_phrases: List[str] = Field(default_factory=list)

    # Relationships
    extracted_actions: List[ExtractedAction] = Field(default_factory=list)
    related_entry_ids: List[str] = Field(default_factory=list)

    # Metadata
    embedding: Optional[List[float]] = None  # Not returned by default
    view_count: int = 0
    last_accessed: Optional[datetime] = None

    class Config:
        """Pydantic config."""
        from_attributes = True


class GraphNode(BaseModel):
    """Node in knowledge graph."""
    id: str
    label: str
    type: str  # entry, concept, person, etc.
    size: int = 1  # For visualization
    color: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class GraphEdge(BaseModel):
    """Edge in knowledge graph."""
    source: str
    target: str
    weight: float
    type: str  # similarity, reference, temporal, etc.
    label: Optional[str] = None


class KnowledgeGraph(BaseModel):
    """Complete knowledge graph."""
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SearchResult(BaseModel):
    """Search result with relevance score."""
    entry: Entry
    score: float
    highlights: List[str] = Field(default_factory=list)


class Suggestion(BaseModel):
    """AI-generated suggestion."""
    type: str  # related_entry, action, insight, etc.
    title: str
    description: str
    relevance_score: float
    data: Dict[str, Any] = Field(default_factory=dict)
