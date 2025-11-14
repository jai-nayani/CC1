"""
Core configuration for Coherence backend.
"""
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """Application settings."""

    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Coherence"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "AI-Powered Universal Personal Intelligence System"

    # CORS Settings
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:3001"]

    # Database Settings
    DATABASE_URL: str = "sqlite+aiosqlite:///./coherence.db"

    # ChromaDB Settings
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    CHROMA_COLLECTION_NAME: str = "coherence_embeddings"

    # AI Settings
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    OPENAI_API_KEY: str = ""  # Optional
    USE_LOCAL_EMBEDDINGS: bool = True

    # Spacy Model
    SPACY_MODEL: str = "en_core_web_sm"

    # Search Settings
    SIMILARITY_THRESHOLD: float = 0.7
    MAX_SEARCH_RESULTS: int = 20

    # Graph Settings
    GRAPH_MAX_DEPTH: int = 3
    GRAPH_MIN_SIMILARITY: float = 0.6

    # WebSocket Settings
    WS_MESSAGE_QUEUE_SIZE: int = 100

    # Security (for future auth)
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v):
        """Parse CORS origins from string or list."""
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True


settings = Settings()
