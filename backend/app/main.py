"""
Main FastAPI application for Coherence.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.api import entries
from app.db.database import db
from app.services.ai_processor import ai_processor
from app.services.semantic_search import semantic_search
from app.services.knowledge_graph import knowledge_graph


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup
    print("🚀 Starting Coherence AI System...")

    # Initialize database
    print("📊 Initializing database...")
    await db.initialize()

    # Initialize AI services
    print("🧠 Loading AI models...")
    await ai_processor.initialize()
    await semantic_search.initialize()
    await knowledge_graph.initialize()

    print("✅ Coherence is ready!")

    yield

    # Shutdown
    print("👋 Shutting down Coherence...")


# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    entries.router,
    prefix=settings.API_V1_STR,
    tags=["entries"]
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to Coherence - AI-Powered Personal Intelligence System",
        "version": settings.VERSION,
        "docs": "/docs",
        "status": "operational"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "services": {
            "database": "operational",
            "ai_processor": "operational",
            "semantic_search": "operational",
            "knowledge_graph": "operational"
        }
    }


@app.get(f"{settings.API_V1_STR}/stats")
async def get_stats():
    """Get system statistics."""
    try:
        entry_count = await semantic_search.count()
        central_nodes = await knowledge_graph.get_central_nodes(limit=5)

        return {
            "total_entries": entry_count,
            "central_nodes": central_nodes,
            "ai_model": settings.EMBEDDING_MODEL,
            "version": settings.VERSION
        }
    except Exception as e:
        return {
            "total_entries": 0,
            "central_nodes": [],
            "error": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
