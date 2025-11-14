# 🎓 Complete Project Guide: Coherence AI System
## From Zero to Hero - Understanding Every Detail

---

# 📚 Table of Contents

1. [What Problem Are We Solving?](#problem)
2. [The Big Picture - What Is Coherence?](#big-picture)
3. [Core Concepts Explained Simply](#core-concepts)
4. [Architecture - How Everything Fits Together](#architecture)
5. [Technology Stack - Why Each Tool?](#tech-stack)
6. [Backend Deep Dive - The Brain](#backend)
7. [Frontend Deep Dive - The Face](#frontend)
8. [JARVIS - The AI Assistant](#jarvis)
9. [Data Flow - How Information Moves](#data-flow)
10. [Real-World Examples - Step by Step](#examples)
11. [How to Build This - Implementation Roadmap](#build-roadmap)
12. [Advanced Features Explained](#advanced-features)
13. [Deployment & Scaling](#deployment)
14. [Business Model & Startup Potential](#business)

---

<a name="problem"></a>
# 1. 🎯 What Problem Are We Solving?

## The Modern Information Overload Crisis

Imagine you're a busy professional. Every day you:
- Have 50+ ideas, thoughts, and notes
- Attend 10+ meetings
- Read 20+ articles
- Save 15+ bookmarks
- Take screenshots of important information
- Jot down tasks and action items

**The Problem:** All this information is scattered across:
- Phone notes
- Computer files
- Email drafts
- Slack messages
- Bookmark folders
- Sticky notes
- Voice memos

**Result:** You forget 90% of it. You can't find what you need when you need it.

## The Current Solutions (And Why They Fail)

**Note-taking apps (Notion, Evernote):**
❌ Require manual organization
❌ No AI understanding
❌ Can't connect ideas automatically
❌ Search is basic keyword matching

**AI Assistants (ChatGPT, Claude):**
❌ No memory of your data
❌ Start fresh each conversation
❌ Can't access your personal context
❌ Don't learn from your patterns

## Our Solution: Coherence

**Think of it as:** Your second brain that:
- ✅ Captures everything (text, voice, images)
- ✅ Understands what you capture (using AI)
- ✅ Automatically organizes and connects ideas
- ✅ Finds patterns you didn't see
- ✅ Remembers everything forever
- ✅ Surfaces the right information at the right time
- ✅ Acts as your personal AI assistant (JARVIS)

**Analogy:** If your brain is like a library, Coherence is the world's best librarian who:
- Reads every book
- Knows exactly where everything is
- Connects related topics automatically
- Recommends what you should read next
- Answers questions instantly

---

<a name="big-picture"></a>
# 2. 🌟 The Big Picture - What Is Coherence?

## Simple Explanation

**Coherence is like having Tony Stark's JARVIS for your personal knowledge.**

You throw information at it (thoughts, notes, ideas, screenshots, voice memos), and it:
1. **Understands** what you gave it using AI
2. **Organizes** it automatically
3. **Connects** it with other related information
4. **Remembers** everything
5. **Helps you** find and use that information through an AI assistant

## The Three Layers

Think of Coherence as having three main parts:

### Layer 1: The Capture System (Input)
- Quick note taking
- Voice input (planned)
- Image/screenshot capture (planned)
- Browser extension integration (planned)

**Like:** The front desk of a hotel that accepts all guests

### Layer 2: The AI Brain (Processing)
- Analyzes what you captured
- Extracts key information
- Creates connections
- Builds knowledge graphs
- Generates insights

**Like:** The hotel manager who knows everything about every guest, their preferences, and organizes everything perfectly

### Layer 3: The Interface (Output)
- Timeline view (see everything chronologically)
- Graph view (see how ideas connect)
- Search (find anything instantly)
- JARVIS chat (ask questions, get insights)

**Like:** Different ways to access hotel services - front desk, concierge, room service

---

<a name="core-concepts"></a>
# 3. 🧠 Core Concepts Explained Simply

Before we dive into the technical details, let's understand the key concepts:

## Concept 1: Semantic Search

**Normal Search (Keyword Matching):**
- You search "apple"
- It finds documents with the word "apple"
- Misses documents about "fruit" or "iPhone"

**Semantic Search (Meaning Matching):**
- You search "healthy snacks"
- It finds documents about "apples, carrots, nuts" even if they never mention "healthy snacks"
- It understands MEANING, not just words

**How it works:**
1. Convert text to numbers (vectors) that represent meaning
2. Similar meanings = similar numbers
3. Search by finding similar number patterns

**Analogy:**
- Keyword search = finding books by looking for exact title
- Semantic search = asking librarian "show me books about adventure" and they understand the theme

## Concept 2: Knowledge Graphs

**What is it?**
A visual network showing how your ideas connect.

**Example:**
```
[Meeting Notes] ──relates to──> [Project X]
       │                            │
       │                            │
   mentions                     needs
       │                            │
       ↓                            ↓
  [John Doe] ──works on──> [Feature Y]
```

**Why is this powerful?**
- Discover unexpected connections
- See patterns in your thinking
- Find related information you forgot about

**Real Example:**
You captured a note about "improving customer onboarding" 3 months ago. Today you're working on "user experience improvements." The knowledge graph connects these automatically, reminding you of your earlier insights.

## Concept 3: Vector Embeddings

**What are vectors?**
Numbers that represent text meaning.

**Simple Example:**
- "cat" → [0.2, 0.8, 0.1, 0.9] (simplified)
- "kitten" → [0.3, 0.8, 0.2, 0.8] (very similar!)
- "car" → [0.9, 0.1, 0.9, 0.2] (completely different!)

**Why use them?**
- Computers can't understand text
- Computers CAN compare numbers
- Similar meanings = similar numbers

**Analogy:** Like giving every book a unique barcode, but similar books have similar barcodes.

## Concept 4: Multi-Agent Systems (JARVIS)

**What is it?**
Instead of one AI doing everything, we have multiple specialized AIs working together.

**The Team:**
1. **Router Agent** - "What kind of question is this?"
2. **Context Agent** - "What background info is relevant?"
3. **Analyzer Agent** - "What's the deeper meaning?"
4. **Planner Agent** - "How should we solve this?"
5. **Coder Agent** - "Need to write code? I got it!"
6. **Verifier Agent** - "Is this answer correct?"
7. **Synthesizer Agent** - "Let me explain it clearly"

**Analogy:** Like a company:
- CEO (Router) delegates tasks
- Research team (Context, Analyzer) gathers info
- Engineering team (Planner, Coder) builds solutions
- QA team (Verifier) checks quality
- Communications team (Synthesizer) presents results

**Why is this better?**
- Each agent is specialized and excellent at one thing
- They work together for better results
- Inspired by Google's DS-STAR research paper

## Concept 5: Real-Time Streaming

**Traditional:**
- You ask a question
- You wait 30 seconds
- You get the full answer

**Streaming:**
- You ask a question
- You see words appearing in real-time (like ChatGPT)
- Feels instant and responsive

**Technical:** Uses WebSockets instead of HTTP requests

## Concept 6: Pre-Processing

**What is it?**
The AI works in the background, preparing answers before you ask.

**Example:**
While you sleep, the system:
- Analyzes all your recent notes
- Identifies trends and patterns
- Pre-computes common insights
- Prepares summaries

**Result:** When you ask "What were my top priorities this week?" - instant answer (already computed)

**Analogy:** Like a chef prepping ingredients before dinner service, so meals come out fast.

---

<a name="architecture"></a>
# 4. 🏗️ Architecture - How Everything Fits Together

## High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │ Timeline │  │  Graph   │  │  Search  │  │ JARVIS Chat  │   │
│  │   View   │  │   View   │  │   View   │  │  (WebSocket) │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│                     React + TypeScript Frontend                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                         HTTP/WS
                             │
┌────────────────────────────┴────────────────────────────────────┐
│                      API GATEWAY (FastAPI)                       │
│  ┌──────────────────┐              ┌────────────────────────┐  │
│  │  REST Endpoints  │              │ WebSocket Endpoints    │  │
│  │  /api/v1/entries │              │ /ws/jarvis            │  │
│  │  /api/v1/search  │              │                        │  │
│  └──────────────────┘              └────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
┌───────────────────┴───┐    ┌────────┴─────────────────────┐
│   CORE AI SERVICES    │    │    JARVIS AI SYSTEM          │
│                       │    │                              │
│ ┌──────────────────┐ │    │ ┌────────────────────────┐  │
│ │  AI Processor    │ │    │ │   Multi-Agent System   │  │
│ │  - NER           │ │    │ │   (7 Agents)           │  │
│ │  - Sentiment     │ │    │ │                        │  │
│ │  - Categorization│ │    │ └────────────────────────┘  │
│ └──────────────────┘ │    │                              │
│                       │    │ ┌────────────────────────┐  │
│ ┌──────────────────┐ │    │ │   Pre-Processor        │  │
│ │ Semantic Search  │ │    │ │   (Background Service) │  │
│ │  - Embeddings    │ │    │ └────────────────────────┘  │
│ │  - Vector DB     │ │    │                              │
│ └──────────────────┘ │    └──────────────────────────────┘
│                       │
│ ┌──────────────────┐ │
│ │ Knowledge Graph  │ │
│ │  - NetworkX      │ │
│ │  - PageRank      │ │
│ └──────────────────┘ │
└───────────────────────┘
           │
    ┌──────┴──────┐
    │             │
┌───┴────┐   ┌────┴─────┐
│SQLite  │   │ ChromaDB │
│Database│   │ (Vectors)│
└────────┘   └──────────┘
```

## How Data Flows (Step by Step)

### Scenario: User Saves a Note

**Step 1: User Types Note**
```
User: "Meeting with John about Project X. Need to finalize design by Friday."
```

**Step 2: Frontend Captures**
```javascript
// React component
const captureNote = async (content) => {
  const response = await fetch('/api/v1/entries', {
    method: 'POST',
    body: JSON.stringify({ content })
  });
};
```

**Step 3: API Receives**
```python
# FastAPI endpoint
@router.post("/entries")
async def create_entry(entry: EntryCreate):
    # Process the entry
```

**Step 4: AI Processing Pipeline**

```python
# AI Processor extracts information
result = await ai_processor.process_entry(content)

# Results:
{
  "entities": ["John", "Project X"],
  "actions": ["finalize design"],
  "deadline": "Friday",
  "category": "work",
  "sentiment": "neutral",
  "summary": "Design finalization meeting"
}
```

**Step 5: Store in Database**
```python
# Save to SQLite
entry_id = await db.create_entry(
    content=content,
    entities=entities,
    category=category
)
```

**Step 6: Create Vector Embedding**
```python
# Generate embedding for semantic search
embedding = await ai_processor.generate_embedding(content)
# embedding = [0.23, 0.45, -0.12, ...] (384 numbers)

# Store in ChromaDB
await semantic_search.add_entry(entry_id, content, embedding)
```

**Step 7: Build Knowledge Graph**
```python
# Add as node
await knowledge_graph.add_entry_node(entry_id, content)

# Find similar entries
similar = await semantic_search.find_similar(content, limit=5)

# Create connections
for similar_entry in similar:
    await knowledge_graph.add_edge(entry_id, similar_entry.id)
```

**Step 8: Return to User**
```python
return {
    "id": entry_id,
    "content": content,
    "ai_insights": result,
    "related_entries": similar
}
```

**Step 9: Frontend Updates**
```javascript
// Display in timeline
setEntries([newEntry, ...entries]);

// Update graph visualization
updateGraph(newEntry);
```

### Scenario: User Asks JARVIS a Question

**Step 1: User Types in Chat**
```
User: "What were my main priorities this week?"
```

**Step 2: WebSocket Connection**
```javascript
// Frontend sends via WebSocket
ws.send(JSON.stringify({
  type: 'query',
  message: 'What were my main priorities this week?'
}));
```

**Step 3: JARVIS Router Agent**
```python
# Determines type of query
routing = await router.route(query)
# Result: "analysis_query" (not coding, not factual lookup)
```

**Step 4: Context Agent Gathers Data**
```python
# Fetch recent entries
recent_entries = await db.get_entries(
    user_id=user_id,
    since=week_ago
)

# Fetch pre-computed insights from Redis cache
cached_insights = await redis.get(f"weekly_insights:{user_id}")
```

**Step 5: Analyzer Agent Processes**
```python
# Analyze patterns
analysis = await analyzer.analyze({
    "entries": recent_entries,
    "cached_insights": cached_insights,
    "query": query
})

# Result:
{
  "top_topics": ["Project X", "Team hiring", "Q4 planning"],
  "action_items_completed": 12,
  "action_items_pending": 5,
  "recurring_themes": ["design", "deadlines"]
}
```

**Step 6: Synthesizer Streams Response**
```python
# Generate response with streaming
async for chunk in synthesizer.synthesize_streaming(analysis):
    # Each chunk is a few words
    await websocket.send_json({
        "type": "partial",
        "content": chunk
    })
```

**Step 7: Frontend Displays**
```javascript
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  if (data.type === 'partial') {
    // Append to existing message
    setCurrentMessage(prev => prev + data.content);
  }
};
```

**User Sees (Streaming):**
```
This week, your main priorities were...

1. Project X Design: You had 3 meetings about finalizing...
2. Team Hiring: You reviewed 5 candidates for...
3. Q4 Planning: You started planning for...

You completed 12 action items and have 5 pending...
```

---

<a name="tech-stack"></a>
# 5. 🛠️ Technology Stack - Why Each Tool?

## Backend Stack

### 1. Python
**Why?** Best language for AI/ML work
- Huge ecosystem of AI libraries
- Easy to read and write
- Great for rapid development

### 2. FastAPI
**Why?** Modern, fast, async web framework
- Built-in async support (handles many users simultaneously)
- Automatic API documentation
- Type safety with Pydantic
- WebSocket support

**Alternative options we didn't choose:**
- Flask: Too old, no async support
- Django: Too heavy, designed for traditional web apps
- Node.js: Not as good for AI/ML

### 3. SQLite (with aiosqlite)
**Why?** Simple, fast, embedded database
- No separate database server needed
- Perfect for getting started
- Easy to backup (single file)
- Async support with aiosqlite

**For production scale:**
- Would migrate to PostgreSQL
- SQLite works perfectly for 10,000s of entries

### 4. ChromaDB
**Why?** Purpose-built vector database
- Optimized for embeddings
- Fast similarity search
- Easy to use
- Local-first (no cloud required)

**What it does:**
- Stores vector embeddings
- Performs similarity searches
- Much faster than storing vectors in SQL

**Alternative options:**
- Pinecone: Cloud-only, costs money
- Weaviate: More complex setup
- Milvus: Overkill for our needs

### 5. Sentence Transformers
**Why?** Generate high-quality embeddings locally
- No API calls needed (privacy + speed)
- Pre-trained models available
- Model: `all-MiniLM-L6-v2` (fast + good quality)

**What it does:**
- Converts text → 384-dimensional vectors
- Captures semantic meaning
- Free and runs locally

### 6. spaCy
**Why?** Industrial-strength NLP
- Named Entity Recognition (NER)
- Fast and accurate
- Extensive language support

**What it does:**
- Extracts people, organizations, locations
- Part-of-speech tagging
- Dependency parsing

### 7. OpenAI API
**Why?** Best-in-class language models
- GPT-4 Turbo for complex reasoning
- Reliable and well-documented
- Streaming support

**Used for:**
- JARVIS multi-agent system
- Complex analysis and synthesis
- Natural conversation

**Cost considerations:**
- Can be expensive at scale
- Pre-processor caches results to reduce API calls
- Could replace with local LLMs (LLaMA, Mistral) for cost savings

### 8. Redis
**Why?** In-memory caching
- Extremely fast (microsecond latency)
- Pub/sub for real-time features
- Reduces database load

**Used for:**
- Caching pre-computed insights
- Session management
- Real-time notifications

### 9. NetworkX
**Why?** Graph algorithms in Python
- PageRank for importance scoring
- Community detection
- Path finding

**Used for:**
- Knowledge graph construction
- Finding related entries
- Discovering patterns

## Frontend Stack

### 1. React 18
**Why?** Industry standard for modern UIs
- Component-based architecture
- Huge ecosystem
- Excellent developer tools
- Concurrent rendering (smooth UX)

### 2. TypeScript
**Why?** Type safety prevents bugs
- Catches errors at compile time
- Better IDE support
- Self-documenting code

**Example benefit:**
```typescript
// JavaScript - easy to make mistakes
function createEntry(data) {
  // What fields does data have? No idea!
}

// TypeScript - compiler checks for you
interface EntryData {
  content: string;
  category: string;
  tags: string[];
}

function createEntry(data: EntryData) {
  // Compiler ensures data has all required fields
}
```

### 3. Vite
**Why?** Next-generation build tool
- Extremely fast dev server
- Instant hot module replacement
- Optimized production builds

**Comparison:**
- Create React App: 30 second startup
- Vite: 1 second startup

### 4. TailwindCSS
**Why?** Utility-first CSS framework
- Rapid UI development
- Consistent design system
- Small bundle size (only uses what you need)

**Example:**
```jsx
// Traditional CSS
<div className="button-primary">Click me</div>

// Tailwind
<div className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
  Click me
</div>
```

### 5. Zustand
**Why?** Simple state management
- Much simpler than Redux
- TypeScript support
- Minimal boilerplate

**What it does:**
- Manages global state (user, entries, settings)
- Reactive updates across components

### 6. Framer Motion
**Why?** Beautiful animations made easy
- Declarative animations
- Gesture support
- Smooth 60 FPS animations

**Used for:**
- Page transitions
- Loading states
- Interactive elements

### 7. date-fns
**Why?** Date manipulation library
- Lightweight alternative to Moment.js
- Tree-shakeable (only import what you use)
- Immutable (prevents bugs)

## Development Tools

### 1. Docker
**Why?** Containerization for consistency
- "Works on my machine" → "Works everywhere"
- Easy deployment
- Isolated environments

### 2. Docker Compose
**Why?** Multi-container orchestration
- Define entire stack in one file
- One command to start everything
- Perfect for development

---

<a name="backend"></a>
# 6. 🧠 Backend Deep Dive - The Brain

Let's understand every backend component in detail.

## File Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── core/
│   │   ├── config.py        # Configuration management
│   ├── db/
│   │   ├── database.py      # Database operations
│   ├── models/
│   │   ├── entry.py         # Data models
│   ├── api/
│   │   ├── entries.py       # Entry endpoints
│   │   ├── jarvis.py        # JARVIS endpoints
│   └── services/
│       ├── ai_processor.py      # Core AI
│       ├── semantic_search.py   # Vector search
│       ├── knowledge_graph.py   # Graph operations
│       ├── jarvis_agent.py      # Multi-agent system
│       └── pre_processor.py     # Background processing
├── Dockerfile
└── requirements.txt
```

## Component 1: main.py - The Application Entry Point

**What it does:** Starts the FastAPI application

```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Runs when app starts and shuts down"""
    # STARTUP
    print("🚀 Starting Coherence...")

    # Initialize all services
    await db.initialize()              # Connect to database
    await ai_processor.initialize()    # Load AI models
    await semantic_search.initialize() # Connect to ChromaDB
    await knowledge_graph.initialize() # Set up graph
    await pre_processor.start()        # Start background jobs

    print("✅ Ready!")

    yield  # App runs here

    # SHUTDOWN
    print("👋 Shutting down...")
    await pre_processor.stop()

app = FastAPI(
    title="Coherence AI",
    lifespan=lifespan
)

# Include routers
app.include_router(entries.router, prefix="/api/v1")
app.include_router(jarvis.router, prefix="/api/v1")
```

**Key concepts:**
- **Lifespan events:** Code that runs on startup/shutdown
- **Routers:** Organize endpoints into logical groups
- **Async:** Everything is non-blocking

## Component 2: config.py - Configuration Management

**What it does:** Manages all settings

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App settings
    PROJECT_NAME: str = "Coherence"
    VERSION: str = "1.0.0"

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./coherence.db"

    # ChromaDB
    CHROMADB_PATH: str = "./chroma_db"

    # OpenAI
    OPENAI_API_KEY: str = ""

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"  # Load from .env file

settings = Settings()
```

**Key concepts:**
- **Environment variables:** Secrets never in code
- **Type validation:** Pydantic checks types automatically
- **.env file:** Easy configuration

## Component 3: database.py - Database Operations

**What it does:** All database CRUD operations

```python
import aiosqlite
from typing import List, Optional

class Database:
    def __init__(self):
        self.db_path = settings.DATABASE_URL
        self.db = None

    async def initialize(self):
        """Create tables if they don't exist"""
        self.db = await aiosqlite.connect(self.db_path)

        # Create entries table
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                content TEXT NOT NULL,
                category TEXT,
                entities TEXT,  -- JSON array
                actions TEXT,   -- JSON array
                sentiment REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create indexes for fast queries
        await self.db.execute("""
            CREATE INDEX IF NOT EXISTS idx_user_created
            ON entries(user_id, created_at DESC)
        """)

        await self.db.commit()

    async def create_entry(
        self,
        user_id: str,
        content: str,
        category: Optional[str] = None,
        entities: Optional[List[str]] = None,
        actions: Optional[List[str]] = None,
        sentiment: Optional[float] = None
    ) -> str:
        """Create a new entry"""
        entry_id = str(uuid.uuid4())

        await self.db.execute("""
            INSERT INTO entries
            (id, user_id, content, category, entities, actions, sentiment)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entry_id,
            user_id,
            content,
            category,
            json.dumps(entities or []),
            json.dumps(actions or []),
            sentiment
        ))

        await self.db.commit()
        return entry_id

    async def get_entry(self, entry_id: str) -> Optional[dict]:
        """Get a single entry by ID"""
        async with self.db.execute(
            "SELECT * FROM entries WHERE id = ?",
            (entry_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return self._row_to_dict(row)
            return None

    async def list_entries(
        self,
        user_id: str,
        limit: int = 50,
        offset: int = 0,
        category: Optional[str] = None
    ) -> List[dict]:
        """List entries with pagination and filtering"""
        query = "SELECT * FROM entries WHERE user_id = ?"
        params = [user_id]

        if category:
            query += " AND category = ?"
            params.append(category)

        query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        async with self.db.execute(query, params) as cursor:
            rows = await cursor.fetchall()
            return [self._row_to_dict(row) for row in rows]

    def _row_to_dict(self, row) -> dict:
        """Convert database row to dictionary"""
        return {
            "id": row[0],
            "user_id": row[1],
            "content": row[2],
            "category": row[3],
            "entities": json.loads(row[4]),
            "actions": json.loads(row[5]),
            "sentiment": row[6],
            "created_at": row[7],
            "updated_at": row[8]
        }

db = Database()
```

**Key concepts:**
- **Async operations:** Non-blocking database queries
- **Connection pooling:** Reuse connections
- **Indexes:** Make queries fast
- **Type hints:** Clear function signatures

## Component 4: entry.py - Data Models

**What it does:** Defines data structures

```python
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class EntryCreate(BaseModel):
    """Data for creating an entry"""
    content: str = Field(..., min_length=1, max_length=10000)
    category: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "content": "Meeting with John about Project X",
                "category": "work"
            }
        }

class EntryResponse(BaseModel):
    """Response when returning an entry"""
    id: str
    user_id: str
    content: str
    category: Optional[str]
    entities: List[str]
    actions: List[str]
    sentiment: Optional[float]
    created_at: datetime
    updated_at: datetime

    # AI-generated insights
    summary: Optional[str]
    key_phrases: List[str]
    related_entries: List[str]

class EntryUpdate(BaseModel):
    """Data for updating an entry"""
    content: Optional[str] = None
    category: Optional[str] = None
```

**Key concepts:**
- **Pydantic models:** Automatic validation
- **Type safety:** Prevents bugs
- **Documentation:** Auto-generates API docs

## Component 5: entries.py - API Endpoints

**What it does:** HTTP endpoints for entry management

```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List

router = APIRouter(prefix="/entries", tags=["entries"])

@router.post("/", response_model=EntryResponse)
async def create_entry(
    entry: EntryCreate,
    user_id: str = Depends(get_current_user)
):
    """
    Create a new entry with AI processing

    - Analyzes content with AI
    - Extracts entities, actions, sentiment
    - Creates vector embedding
    - Adds to knowledge graph
    """
    try:
        # Step 1: Process with AI
        ai_result = await ai_processor.process_entry(entry.content)

        # Step 2: Save to database
        entry_id = await db.create_entry(
            user_id=user_id,
            content=entry.content,
            category=ai_result.category,
            entities=ai_result.entities,
            actions=ai_result.actions,
            sentiment=ai_result.sentiment
        )

        # Step 3: Add to vector database
        await semantic_search.add_entry(
            entry_id=entry_id,
            content=entry.content,
            metadata={
                "user_id": user_id,
                "category": ai_result.category
            }
        )

        # Step 4: Update knowledge graph
        await knowledge_graph.add_entry_node(entry_id, entry.content)
        await knowledge_graph.build_connections(entry_id)

        # Step 5: Return response
        return EntryResponse(
            id=entry_id,
            user_id=user_id,
            content=entry.content,
            category=ai_result.category,
            entities=ai_result.entities,
            actions=ai_result.actions,
            sentiment=ai_result.sentiment,
            summary=ai_result.summary,
            key_phrases=ai_result.key_phrases,
            related_entries=await semantic_search.find_similar(entry_id)
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[EntryResponse])
async def list_entries(
    user_id: str = Depends(get_current_user),
    limit: int = 50,
    offset: int = 0,
    category: Optional[str] = None
):
    """List entries with pagination and filtering"""
    entries = await db.list_entries(
        user_id=user_id,
        limit=limit,
        offset=offset,
        category=category
    )
    return entries

@router.get("/{entry_id}", response_model=EntryResponse)
async def get_entry(
    entry_id: str,
    user_id: str = Depends(get_current_user)
):
    """Get a specific entry by ID"""
    entry = await db.get_entry(entry_id)

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    if entry["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    return entry

@router.get("/search", response_model=List[EntryResponse])
async def semantic_search(
    query: str,
    user_id: str = Depends(get_current_user),
    limit: int = 10
):
    """Semantic search across entries"""
    results = await semantic_search.search(
        query=query,
        user_id=user_id,
        limit=limit
    )
    return results
```

**Key concepts:**
- **REST API:** Standard HTTP methods (GET, POST, PUT, DELETE)
- **Dependency injection:** `Depends()` for auth
- **Error handling:** Proper HTTP status codes
- **Documentation:** Auto-generated from docstrings

## Component 6: ai_processor.py - Core AI Engine

**What it does:** All AI processing logic

```python
import spacy
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import openai

class AIProcessor:
    def __init__(self):
        self.nlp = None  # spaCy model
        self.embedding_model = None  # Sentence transformer
        self.openai_client = None

    async def initialize(self):
        """Load AI models"""
        print("Loading AI models...")

        # Load spaCy for NER
        self.nlp = spacy.load("en_core_web_sm")

        # Load sentence transformer for embeddings
        self.embedding_model = SentenceTransformer(
            'sentence-transformers/all-MiniLM-L6-v2'
        )

        # Initialize OpenAI client
        self.openai_client = openai.AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        print("✅ AI models loaded")

    async def process_entry(self, content: str) -> AIProcessingResult:
        """
        Complete AI processing pipeline

        Steps:
        1. Extract entities (people, places, organizations)
        2. Detect actions and tasks
        3. Categorize content
        4. Analyze sentiment
        5. Generate summary
        6. Extract key phrases
        """

        # Run NLP analysis
        doc = self.nlp(content)

        # Extract entities
        entities = self._extract_entities(doc)

        # Detect actions
        actions = self._extract_actions(doc)

        # Categorize
        category = await self._categorize(content)

        # Sentiment analysis
        sentiment = self._analyze_sentiment(doc)

        # Generate summary
        summary = await self._generate_summary(content)

        # Extract key phrases
        key_phrases = self._extract_key_phrases(doc)

        return AIProcessingResult(
            entities=entities,
            actions=actions,
            category=category,
            sentiment=sentiment,
            summary=summary,
            key_phrases=key_phrases
        )

    def _extract_entities(self, doc) -> List[str]:
        """Extract named entities using spaCy"""
        entities = []

        for ent in doc.ents:
            if ent.label_ in ["PERSON", "ORG", "GPE", "PRODUCT"]:
                entities.append({
                    "text": ent.text,
                    "type": ent.label_
                })

        return entities

    def _extract_actions(self, doc) -> List[str]:
        """Extract action items and tasks"""
        actions = []

        # Look for verbs followed by objects
        for token in doc:
            if token.pos_ == "VERB":
                # Get the verb phrase
                phrase = " ".join([
                    child.text
                    for child in token.subtree
                ])

                # Check for action indicators
                if any(word in phrase.lower() for word in [
                    "need", "should", "must", "have to",
                    "finalize", "complete", "review", "send"
                ]):
                    actions.append(phrase)

        return actions

    async def _categorize(self, content: str) -> str:
        """Categorize content using AI"""

        # Simple keyword-based categorization
        # (Could use AI for more accuracy)
        content_lower = content.lower()

        if any(word in content_lower for word in ["meeting", "call", "discuss"]):
            return "meeting"
        elif any(word in content_lower for word in ["task", "todo", "need to"]):
            return "task"
        elif any(word in content_lower for word in ["idea", "thought", "maybe"]):
            return "idea"
        elif any(word in content_lower for word in ["note", "remember"]):
            return "note"
        else:
            return "general"

    def _analyze_sentiment(self, doc) -> float:
        """Analyze sentiment (-1 to 1)"""
        # Use spaCy's sentiment analysis
        # (Simplified - could use more sophisticated model)

        positive_words = ["great", "good", "excellent", "happy", "love"]
        negative_words = ["bad", "terrible", "awful", "hate", "problem"]

        text_lower = doc.text.lower()

        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)

        if pos_count + neg_count == 0:
            return 0.0

        return (pos_count - neg_count) / (pos_count + neg_count)

    async def _generate_summary(self, content: str) -> str:
        """Generate a concise summary"""

        # If content is short, return as-is
        if len(content) < 100:
            return content[:50] + "..."

        # Use OpenAI for longer content
        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[{
                    "role": "system",
                    "content": "Summarize this in 10 words or less."
                }, {
                    "role": "user",
                    "content": content
                }],
                max_tokens=20
            )

            return response.choices[0].message.content

        except Exception as e:
            # Fallback to simple truncation
            return content[:50] + "..."

    def _extract_key_phrases(self, doc) -> List[str]:
        """Extract important phrases"""
        key_phrases = []

        # Extract noun phrases
        for chunk in doc.noun_chunks:
            if len(chunk.text.split()) >= 2:  # At least 2 words
                key_phrases.append(chunk.text)

        # Remove duplicates and sort by importance
        key_phrases = list(set(key_phrases))

        return key_phrases[:5]  # Top 5

    async def generate_embedding(self, text: str) -> List[float]:
        """Generate vector embedding for text"""

        # Use sentence transformer
        embedding = self.embedding_model.encode(
            text,
            convert_to_numpy=True
        )

        # Convert to list
        return embedding.tolist()

ai_processor = AIProcessor()
```

**Key concepts:**
- **NLP pipeline:** Multi-step processing
- **Named Entity Recognition:** Extract people, places, things
- **Embeddings:** Convert text to vectors
- **Caching:** Avoid recomputing same results

## Component 7: semantic_search.py - Vector Search

**What it does:** Semantic search using ChromaDB

```python
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional

class SemanticSearch:
    def __init__(self):
        self.client = None
        self.collection = None

    async def initialize(self):
        """Initialize ChromaDB"""

        # Create client
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.CHROMADB_PATH
        ))

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="entries",
            metadata={"description": "User entries"}
        )

    async def add_entry(
        self,
        entry_id: str,
        content: str,
        metadata: Optional[Dict] = None
    ):
        """Add entry to vector database"""

        # Generate embedding
        embedding = await ai_processor.generate_embedding(content)

        # Add to ChromaDB
        self.collection.add(
            ids=[entry_id],
            embeddings=[embedding],
            documents=[content],
            metadatas=[metadata or {}]
        )

        # Persist to disk
        self.client.persist()

    async def search(
        self,
        query: str,
        user_id: str,
        limit: int = 10
    ) -> List[Dict]:
        """Semantic search for similar entries"""

        # Generate query embedding
        query_embedding = await ai_processor.generate_embedding(query)

        # Search in ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=limit,
            where={"user_id": user_id}  # Filter by user
        )

        # Format results
        formatted_results = []
        for i in range(len(results['ids'][0])):
            formatted_results.append({
                "id": results['ids'][0][i],
                "content": results['documents'][0][i],
                "similarity": 1 - results['distances'][0][i],  # Convert distance to similarity
                "metadata": results['metadatas'][0][i]
            })

        return formatted_results

    async def find_similar(
        self,
        entry_id: str,
        limit: int = 5
    ) -> List[str]:
        """Find similar entries to a given entry"""

        # Get the entry content
        result = self.collection.get(ids=[entry_id])
        if not result['documents']:
            return []

        content = result['documents'][0]

        # Search for similar
        similar = await self.search(
            query=content,
            user_id=result['metadatas'][0]['user_id'],
            limit=limit + 1  # +1 because it will include itself
        )

        # Remove the entry itself
        similar = [s for s in similar if s['id'] != entry_id]

        return [s['id'] for s in similar[:limit]]

semantic_search = SemanticSearch()
```

**Key concepts:**
- **Vector database:** Optimized for embeddings
- **Cosine similarity:** Measures how similar vectors are
- **Filtering:** Search within user's data only
- **Persistence:** Save to disk

## Component 8: knowledge_graph.py - Graph Operations

**What it does:** Build and query knowledge graphs

```python
import networkx as nx
from typing import List, Dict, Set
import json

class KnowledgeGraph:
    def __init__(self):
        self.graph = None

    async def initialize(self):
        """Initialize empty graph"""
        self.graph = nx.DiGraph()  # Directed graph

    async def add_entry_node(
        self,
        entry_id: str,
        content: str,
        metadata: Dict = None
    ):
        """Add entry as a node"""

        self.graph.add_node(
            entry_id,
            content=content,
            label=content[:50],  # Short label for visualization
            type='entry',
            **metadata or {}
        )

    async def add_entity_node(
        self,
        entity_name: str,
        entity_type: str
    ):
        """Add entity (person, org, etc.) as a node"""

        node_id = f"entity:{entity_name}"

        if not self.graph.has_node(node_id):
            self.graph.add_node(
                node_id,
                label=entity_name,
                type=entity_type
            )

        return node_id

    async def build_connections(self, entry_id: str):
        """Build connections for a new entry"""

        # Get entry data
        entry_data = self.graph.nodes[entry_id]
        content = entry_data['content']

        # Step 1: Find similar entries (semantic)
        similar_entries = await semantic_search.find_similar(
            entry_id,
            limit=5
        )

        for similar_id in similar_entries:
            if self.graph.has_node(similar_id):
                # Add edge with weight based on similarity
                self.graph.add_edge(
                    entry_id,
                    similar_id,
                    weight=0.8,  # High similarity
                    type='similar'
                )

        # Step 2: Connect entities
        entities = entry_data.get('entities', [])

        for entity in entities:
            # Create entity node
            entity_id = await self.add_entity_node(
                entity['text'],
                entity['type']
            )

            # Connect entry to entity
            self.graph.add_edge(
                entry_id,
                entity_id,
                type='mentions'
            )

            # Find other entries that mention this entity
            for node_id, node_data in self.graph.nodes(data=True):
                if node_data.get('type') == 'entry' and node_id != entry_id:
                    node_entities = node_data.get('entities', [])
                    if any(e['text'] == entity['text'] for e in node_entities):
                        # Both entries mention same entity
                        self.graph.add_edge(
                            entry_id,
                            node_id,
                            weight=0.6,
                            type='shared_entity'
                        )

    async def get_related_entries(
        self,
        entry_id: str,
        depth: int = 2
    ) -> List[str]:
        """Get entries within N hops"""

        if not self.graph.has_node(entry_id):
            return []

        # BFS (Breadth-First Search) to depth N
        related = set()
        current_level = {entry_id}

        for _ in range(depth):
            next_level = set()

            for node in current_level:
                # Get all neighbors
                neighbors = set(self.graph.successors(node))
                neighbors.update(self.graph.predecessors(node))

                # Filter for entries only
                entry_neighbors = {
                    n for n in neighbors
                    if self.graph.nodes[n].get('type') == 'entry'
                }

                next_level.update(entry_neighbors)

            related.update(next_level)
            current_level = next_level

        # Remove the entry itself
        related.discard(entry_id)

        return list(related)

    async def get_important_entries(self, limit: int = 10) -> List[str]:
        """Get most important entries using PageRank"""

        # Calculate PageRank scores
        pagerank = nx.pagerank(self.graph)

        # Filter for entry nodes only
        entry_scores = {
            node_id: score
            for node_id, score in pagerank.items()
            if self.graph.nodes[node_id].get('type') == 'entry'
        }

        # Sort by score
        sorted_entries = sorted(
            entry_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [node_id for node_id, _ in sorted_entries[:limit]]

    async def find_shortest_path(
        self,
        entry_id_1: str,
        entry_id_2: str
    ) -> List[str]:
        """Find shortest path between two entries"""

        try:
            path = nx.shortest_path(
                self.graph.to_undirected(),  # Treat as undirected
                entry_id_1,
                entry_id_2
            )
            return path
        except nx.NetworkXNoPath:
            return []

    async def export_for_visualization(self) -> Dict:
        """Export graph in format for frontend visualization"""

        nodes = []
        edges = []

        # Export nodes
        for node_id, node_data in self.graph.nodes(data=True):
            nodes.append({
                "id": node_id,
                "label": node_data.get('label', node_id),
                "type": node_data.get('type', 'unknown'),
                "data": node_data
            })

        # Export edges
        for source, target, edge_data in self.graph.edges(data=True):
            edges.append({
                "source": source,
                "target": target,
                "weight": edge_data.get('weight', 1.0),
                "type": edge_data.get('type', 'related')
            })

        return {
            "nodes": nodes,
            "edges": edges
        }

knowledge_graph = KnowledgeGraph()
```

**Key concepts:**
- **Directed graph:** Edges have direction
- **Node types:** Entries and entities
- **Edge weights:** Strength of connection
- **Graph algorithms:** PageRank, shortest path, BFS
- **NetworkX:** Powerful graph library

---

## Component 9: jarvis_agent.py - Multi-Agent System

This is the most complex component. Let me break it down:

**What it does:** JARVIS AI assistant with 7 specialized agents

```python
from openai import AsyncOpenAI
from typing import AsyncGenerator, Dict, List
import json

class AgentMessage:
    """Message from an agent"""
    def __init__(
        self,
        agent: str,
        message_type: str,  # 'thinking', 'progress', 'partial', 'complete'
        content: str,
        metadata: Dict = None
    ):
        self.agent = agent
        self.message_type = message_type
        self.content = content
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "agent": self.agent,
            "type": self.message_type,
            "content": self.content,
            "metadata": self.metadata
        }

class UserContext:
    """Context about the user"""
    def __init__(
        self,
        user_id: str,
        recent_entries: List[Dict],
        cached_insights: Dict,
        conversation_history: List[Dict]
    ):
        self.user_id = user_id
        self.recent_entries = recent_entries
        self.cached_insights = cached_insights
        self.conversation_history = conversation_history

class RouterAgent:
    """
    Agent 1: Routes queries to appropriate handling strategy

    Determines:
    - Type of query (question, task, analysis, coding)
    - Urgency level
    - Required resources
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def route(
        self,
        query: str,
        context: UserContext
    ) -> Dict:
        """Determine how to handle this query"""

        prompt = f"""You are a query router. Analyze this query and determine:
1. Type: question, task, analysis, coding, casual_chat
2. Complexity: low, medium, high
3. Requires: List of resources needed (e.g., user_data, web_search, code_execution)

Query: {query}

Respond with JSON only."""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            response_format={"type": "json_object"}
        )

        routing = json.loads(response.choices[0].message.content)

        return routing

class ContextAgent:
    """
    Agent 2: Gathers and enriches context

    Retrieves:
    - Relevant past entries
    - Related entities
    - Pre-computed insights
    - Conversation history
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def enrich(
        self,
        query: str,
        context: UserContext
    ) -> Dict:
        """Gather all relevant context"""

        enriched = {
            "query": query,
            "user_id": context.user_id,
            "timestamp": datetime.now().isoformat()
        }

        # Step 1: Semantic search for relevant entries
        relevant_entries = await semantic_search.search(
            query=query,
            user_id=context.user_id,
            limit=10
        )
        enriched["relevant_entries"] = relevant_entries

        # Step 2: Get cached insights
        enriched["insights"] = context.cached_insights

        # Step 3: Extract entities from query
        doc = ai_processor.nlp(query)
        entities = [ent.text for ent in doc.ents]
        enriched["mentioned_entities"] = entities

        # Step 4: Find entries mentioning these entities
        entity_entries = []
        for entity in entities:
            # Search for entries with this entity
            results = await db.search_by_entity(entity, context.user_id)
            entity_entries.extend(results)
        enriched["entity_related_entries"] = entity_entries

        # Step 5: Get conversation context
        enriched["conversation_history"] = context.conversation_history[-5:]  # Last 5 turns

        return enriched

class AnalyzerAgent:
    """
    Agent 3: Deep analysis and pattern recognition

    Analyzes:
    - Patterns in user data
    - Trends over time
    - Hidden connections
    - Actionable insights
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def analyze(
        self,
        query: str,
        enriched_context: Dict
    ) -> Dict:
        """Perform deep analysis"""

        # Build analysis prompt
        prompt = f"""You are a data analyst. Analyze this user's data and provide insights.

Query: {query}

User Data Summary:
- Total relevant entries: {len(enriched_context.get('relevant_entries', []))}
- Recent insights: {enriched_context.get('insights', {})}
- Mentioned entities: {enriched_context.get('mentioned_entities', [])}

Analyze and provide:
1. Key patterns
2. Trends
3. Recommendations
4. Action items

Respond with structured JSON."""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": json.dumps(enriched_context, indent=2)}
            ],
            response_format={"type": "json_object"}
        )

        analysis = json.loads(response.choices[0].message.content)

        return analysis

class PlannerAgent:
    """
    Agent 4: Creates execution plans

    Plans:
    - Steps to answer query
    - Resources needed
    - Sub-tasks
    - Dependencies
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def plan(
        self,
        query: str,
        analysis: Dict
    ) -> Dict:
        """Create execution plan"""

        prompt = f"""You are a planner. Create a step-by-step plan to answer this query.

Query: {query}

Analysis: {json.dumps(analysis, indent=2)}

Create a plan with:
1. Steps (in order)
2. Expected outcome for each step
3. Dependencies between steps

Respond with JSON only."""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            response_format={"type": "json_object"}
        )

        plan = json.loads(response.choices[0].message.content)

        return plan

class CoderAgent:
    """
    Agent 5: Writes and executes code

    Capabilities:
    - Data analysis code
    - Visualizations
    - Custom computations
    - API integrations
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def code(
        self,
        task: str,
        context: Dict
    ) -> Dict:
        """Generate and execute code"""

        # This would generate Python code to analyze data
        # For safety, we'd use a sandboxed environment

        prompt = f"""Generate Python code for this task: {task}

Context: {json.dumps(context, indent=2)}

Requirements:
- Use pandas for data analysis
- Return results as JSON
- Handle errors gracefully

Code only, no explanation."""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": task}
            ]
        )

        code = response.choices[0].message.content

        # In production, execute in sandbox
        # For now, return the code
        return {
            "code": code,
            "executed": False,
            "results": None
        }

class VerifierAgent:
    """
    Agent 6: Verifies accuracy and quality

    Checks:
    - Factual correctness
    - Completeness
    - Relevance
    - Quality of response
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def verify(
        self,
        query: str,
        proposed_answer: str,
        context: Dict
    ) -> Dict:
        """Verify the proposed answer"""

        prompt = f"""You are a quality verifier. Check if this answer is:
1. Accurate
2. Complete
3. Relevant to the query
4. Well-structured

Query: {query}

Proposed Answer: {proposed_answer}

Context: {json.dumps(context, indent=2)}

Respond with JSON:
{{
    "is_accurate": true/false,
    "is_complete": true/false,
    "is_relevant": true/false,
    "quality_score": 0-100,
    "suggestions": ["improvement 1", "improvement 2"],
    "approved": true/false
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": proposed_answer}
            ],
            response_format={"type": "json_object"}
        )

        verification = json.loads(response.choices[0].message.content)

        return verification

class SynthesizerAgent:
    """
    Agent 7: Synthesizes final response

    Creates:
    - Clear, concise answers
    - Natural language
    - Proper formatting
    - Citations to sources
    """

    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def synthesize_streaming(
        self,
        query: str,
        analysis: Dict,
        plan: Dict,
        verification: Dict,
        context: Dict
    ) -> AsyncGenerator[str, None]:
        """Generate final response with streaming"""

        # Build comprehensive prompt
        prompt = f"""You are JARVIS, an intelligent assistant.

User Query: {query}

Analysis: {json.dumps(analysis, indent=2)}

Plan: {json.dumps(plan, indent=2)}

Context: {json.dumps(context, indent=2)}

Create a clear, helpful response that:
1. Directly answers the query
2. Provides relevant insights from the analysis
3. Cites specific entries when relevant
4. Suggests next steps if applicable

Be conversational and helpful."""

        # Stream the response
        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            stream=True
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

class JARVISAgent:
    """
    Main JARVIS agent that orchestrates all sub-agents
    """

    def __init__(self, openai_api_key: str, model: str = "gpt-4-turbo-preview"):
        self.client = AsyncOpenAI(api_key=openai_api_key)
        self.model = model

        # Initialize all agents
        self.router = RouterAgent(self.client, self.model)
        self.context = ContextAgent(self.client, self.model)
        self.analyzer = AnalyzerAgent(self.client, self.model)
        self.planner = PlannerAgent(self.client, self.model)
        self.coder = CoderAgent(self.client, self.model)
        self.verifier = VerifierAgent(self.client, self.model)
        self.synthesizer = SynthesizerAgent(self.client, self.model)

    async def process_query(
        self,
        user_query: str,
        user_context: UserContext
    ) -> AsyncGenerator[AgentMessage, None]:
        """
        Main processing pipeline with streaming updates

        Flow:
        1. Route query
        2. Enrich context
        3. Analyze
        4. Plan
        5. (Optionally) Code
        6. Verify
        7. Synthesize (streaming)
        """

        # Stage 1: Routing
        yield AgentMessage(
            agent="router",
            message_type="thinking",
            content="Analyzing your query..."
        )

        routing = await self.router.route(user_query, user_context)

        yield AgentMessage(
            agent="router",
            message_type="progress",
            content=f"Query type: {routing['type']}, Complexity: {routing['complexity']}"
        )

        # Stage 2: Context enrichment
        yield AgentMessage(
            agent="context",
            message_type="thinking",
            content="Gathering relevant information..."
        )

        enriched_context = await self.context.enrich(user_query, user_context)

        yield AgentMessage(
            agent="context",
            message_type="progress",
            content=f"Found {len(enriched_context.get('relevant_entries', []))} relevant entries"
        )

        # Stage 3: Analysis
        yield AgentMessage(
            agent="analyzer",
            message_type="thinking",
            content="Analyzing patterns and insights..."
        )

        analysis = await self.analyzer.analyze(user_query, enriched_context)

        yield AgentMessage(
            agent="analyzer",
            message_type="progress",
            content="Analysis complete"
        )

        # Stage 4: Planning
        yield AgentMessage(
            agent="planner",
            message_type="thinking",
            content="Creating response plan..."
        )

        plan = await self.planner.plan(user_query, analysis)

        # Stage 5: Coding (if needed)
        if routing.get('requires_code', False):
            yield AgentMessage(
                agent="coder",
                message_type="thinking",
                content="Generating code..."
            )

            code_result = await self.coder.code(user_query, enriched_context)

        # Stage 6: Synthesis with streaming
        yield AgentMessage(
            agent="synthesizer",
            message_type="thinking",
            content="Formulating response..."
        )

        # Stream the final response
        full_response = ""
        async for chunk in self.synthesizer.synthesize_streaming(
            user_query,
            analysis,
            plan,
            {},  # verification results
            enriched_context
        ):
            full_response += chunk
            yield AgentMessage(
                agent="synthesizer",
                message_type="partial",
                content=chunk
            )

        # Final message
        yield AgentMessage(
            agent="synthesizer",
            message_type="complete",
            content=full_response,
            metadata={
                "routing": routing,
                "analysis": analysis,
                "sources": enriched_context.get('relevant_entries', [])[:3]
            }
        )

jarvis_agent = JARVISAgent(openai_api_key=settings.OPENAI_API_KEY)
```

**Key concepts:**
- **Multi-agent system:** Specialized agents work together
- **Streaming:** Real-time response generation
- **Context enrichment:** Gather all relevant data
- **Verification:** Quality control
- **Async generators:** Stream data efficiently

---

## Component 10: pre_processor.py - Background Intelligence

**What it does:** Pre-computes insights in the background

```python
import asyncio
import redis.asyncio as redis
from datetime import datetime, timedelta
import json

class PreProcessor:
    """
    Background service that pre-computes insights

    Runs every 5 minutes to:
    1. Update user summaries
    2. Compute common insights
    3. Refresh hot data
    4. Update trending topics
    """

    def __init__(self):
        self.redis_client = None
        self.is_running = False
        self.task = None

    async def initialize(self):
        """Connect to Redis"""
        self.redis_client = await redis.from_url(settings.REDIS_URL)

    async def start(self):
        """Start background processing"""
        self.is_running = True
        self.task = asyncio.create_task(self._processing_loop())

    async def stop(self):
        """Stop background processing"""
        self.is_running = False
        if self.task:
            self.task.cancel()

    async def _processing_loop(self):
        """Main processing loop"""
        while self.is_running:
            try:
                # Run all pre-processing tasks
                await asyncio.gather(
                    self.update_user_summaries(),
                    self.pre_compute_insights(),
                    self.refresh_hot_data(),
                    self.update_trending_topics(),
                    return_exceptions=True
                )

                # Wait 5 minutes
                await asyncio.sleep(300)

            except Exception as e:
                print(f"Pre-processor error: {e}")
                await asyncio.sleep(60)  # Wait 1 minute on error

    async def update_user_summaries(self):
        """Update summaries for all active users"""

        # Get list of users (simplified)
        users = await db.get_active_users()

        for user_id in users:
            try:
                # Get recent entries (last 7 days)
                week_ago = datetime.now() - timedelta(days=7)
                entries = await db.get_entries(
                    user_id=user_id,
                    since=week_ago
                )

                if not entries:
                    continue

                # Compute summary
                summary = {
                    "total_entries": len(entries),
                    "categories": self._count_categories(entries),
                    "top_entities": self._get_top_entities(entries),
                    "action_items": self._count_actions(entries),
                    "sentiment_trend": self._analyze_sentiment_trend(entries),
                    "updated_at": datetime.now().isoformat()
                }

                # Cache in Redis (30 minute expiry)
                cache_key = f"user_summary:{user_id}"
                await self.redis_client.setex(
                    cache_key,
                    1800,  # 30 minutes
                    json.dumps(summary)
                )

            except Exception as e:
                print(f"Error processing user {user_id}: {e}")

    async def pre_compute_insights(self):
        """Pre-compute common insights"""

        users = await db.get_active_users()

        for user_id in users:
            try:
                # Get recent entries
                entries = await db.get_entries(
                    user_id=user_id,
                    limit=100
                )

                # Compute insights
                insights = {
                    "top_categories": self._get_top_categories(entries),
                    "recurring_topics": self._get_recurring_topics(entries),
                    "action_items_summary": await self._get_action_summary(entries),
                    "productivity_patterns": self._get_productivity_patterns(entries),
                    "suggestions": self._generate_suggestions(entries),
                    "computed_at": datetime.now().isoformat()
                }

                # Cache insights
                cache_key = f"pre_computed_insights:{user_id}"
                await self.redis_client.setex(
                    cache_key,
                    1800,  # 30 minutes
                    json.dumps(insights)
                )

            except Exception as e:
                print(f"Error computing insights for {user_id}: {e}")

    async def refresh_hot_data(self):
        """Refresh frequently accessed data"""

        # Get list of "hot" entries (frequently accessed)
        hot_entries = await db.get_frequently_accessed_entries(limit=50)

        for entry_id in hot_entries:
            try:
                # Get full entry data
                entry = await db.get_entry(entry_id)

                if entry:
                    # Cache the entry
                    cache_key = f"entry:{entry_id}"
                    await self.redis_client.setex(
                        cache_key,
                        600,  # 10 minutes
                        json.dumps(entry)
                    )

                    # Pre-compute related entries
                    related = await semantic_search.find_similar(entry_id)
                    related_cache_key = f"related:{entry_id}"
                    await self.redis_client.setex(
                        related_cache_key,
                        600,
                        json.dumps(related)
                    )

            except Exception as e:
                print(f"Error refreshing entry {entry_id}: {e}")

    async def update_trending_topics(self):
        """Identify trending topics across all users"""

        # Get all recent entries (last 24 hours)
        day_ago = datetime.now() - timedelta(days=1)
        recent_entries = await db.get_all_entries_since(day_ago)

        # Extract all entities
        all_entities = []
        for entry in recent_entries:
            all_entities.extend(entry.get('entities', []))

        # Count occurrences
        entity_counts = {}
        for entity in all_entities:
            entity_text = entity['text']
            entity_counts[entity_text] = entity_counts.get(entity_text, 0) + 1

        # Sort by frequency
        trending = sorted(
            entity_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        # Cache trending topics
        await self.redis_client.setex(
            "trending_topics",
            3600,  # 1 hour
            json.dumps([{
                "entity": entity,
                "count": count
            } for entity, count in trending])
        )

    def _count_categories(self, entries: List[Dict]) -> Dict[str, int]:
        """Count entries by category"""
        categories = {}
        for entry in entries:
            cat = entry.get('category', 'uncategorized')
            categories[cat] = categories.get(cat, 0) + 1
        return categories

    def _get_top_entities(self, entries: List[Dict], limit: int = 10) -> List[Dict]:
        """Get most mentioned entities"""
        entity_counts = {}

        for entry in entries:
            for entity in entry.get('entities', []):
                text = entity['text']
                entity_counts[text] = entity_counts.get(text, 0) + 1

        # Sort and return top N
        sorted_entities = sorted(
            entity_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            {"entity": entity, "count": count}
            for entity, count in sorted_entities[:limit]
        ]

    def _count_actions(self, entries: List[Dict]) -> Dict[str, int]:
        """Count action items"""
        total = 0
        completed = 0

        for entry in entries:
            actions = entry.get('actions', [])
            total += len(actions)
            # Simplified - would track completion status

        return {
            "total": total,
            "completed": completed,
            "pending": total - completed
        }

    def _analyze_sentiment_trend(self, entries: List[Dict]) -> Dict:
        """Analyze sentiment over time"""
        if not entries:
            return {"average": 0.0, "trend": "neutral"}

        sentiments = [
            entry.get('sentiment', 0.0)
            for entry in entries
        ]

        average = sum(sentiments) / len(sentiments)

        # Simple trend: compare first half vs second half
        mid = len(sentiments) // 2
        first_half_avg = sum(sentiments[:mid]) / mid if mid > 0 else 0
        second_half_avg = sum(sentiments[mid:]) / (len(sentiments) - mid) if len(sentiments) > mid else 0

        if second_half_avg > first_half_avg + 0.1:
            trend = "improving"
        elif second_half_avg < first_half_avg - 0.1:
            trend = "declining"
        else:
            trend = "stable"

        return {
            "average": round(average, 2),
            "trend": trend
        }

    def _get_top_categories(self, entries: List[Dict]) -> List[Dict]:
        """Get top categories"""
        counts = self._count_categories(entries)
        sorted_cats = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [
            {"category": cat, "count": count}
            for cat, count in sorted_cats[:5]
        ]

    def _get_recurring_topics(self, entries: List[Dict]) -> List[str]:
        """Identify recurring topics"""
        # Use key phrases from entries
        all_phrases = []
        for entry in entries:
            all_phrases.extend(entry.get('key_phrases', []))

        # Count occurrences
        phrase_counts = {}
        for phrase in all_phrases:
            phrase_counts[phrase] = phrase_counts.get(phrase, 0) + 1

        # Return phrases that appear 3+ times
        recurring = [
            phrase for phrase, count in phrase_counts.items()
            if count >= 3
        ]

        return recurring[:10]

    async def _get_action_summary(self, entries: List[Dict]) -> Dict:
        """Summarize action items"""
        all_actions = []
        for entry in entries:
            all_actions.extend(entry.get('actions', []))

        return {
            "total": len(all_actions),
            "recent": all_actions[:5] if all_actions else []
        }

    def _get_productivity_patterns(self, entries: List[Dict]) -> Dict:
        """Identify productivity patterns"""
        # Group by day of week
        day_counts = {i: 0 for i in range(7)}  # 0 = Monday

        for entry in entries:
            created_at = datetime.fromisoformat(entry['created_at'])
            day_counts[created_at.weekday()] += 1

        # Find most productive day
        most_productive_day = max(day_counts, key=day_counts.get)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        return {
            "most_productive_day": days[most_productive_day],
            "entries_by_day": {
                days[day]: count
                for day, count in day_counts.items()
            }
        }

    def _generate_suggestions(self, entries: List[Dict]) -> List[str]:
        """Generate helpful suggestions"""
        suggestions = []

        # Check if user has many unprocessed entries
        if len(entries) > 50:
            suggestions.append("You have many entries. Consider reviewing and archiving old ones.")

        # Check for action items
        total_actions = sum(len(e.get('actions', [])) for e in entries)
        if total_actions > 10:
            suggestions.append(f"You have {total_actions} action items. Focus on completing high-priority ones.")

        # Check for specific patterns
        categories = self._count_categories(entries)
        if categories.get('idea', 0) > 10:
            suggestions.append("You have many ideas captured. Consider turning some into action plans.")

        return suggestions

pre_processor = PreProcessor()
```

**Key concepts:**
- **Background jobs:** Runs independently of user requests
- **Caching:** Store results in Redis for instant access
- **Batch processing:** Process all users periodically
- **Pattern detection:** Find trends and insights
- **Performance optimization:** Pre-compute expensive operations

---

That completes the Backend Deep Dive! The backend has:
- ✅ FastAPI application structure
- ✅ Database operations
- ✅ AI processing pipeline
- ✅ Semantic search
- ✅ Knowledge graphs
- ✅ Multi-agent JARVIS system
- ✅ Background pre-processing

Next, I'll cover the Frontend in the same level of detail. Would you like me to continue with that section?

---

<a name="frontend"></a>
# 7. 🎨 Frontend Deep Dive - The Face

Now let's understand the user interface in detail.

## File Structure
```
frontend/
├── src/
│   ├── main.tsx              # App entry point
│   ├── App.tsx               # Root component
│   ├── index.css             # Global styles
│   ├── components/
│   │   ├── Header.tsx        # App header
│   │   └── Sidebar.tsx       # Navigation
│   ├── pages/
│   │   ├── CaptureView.tsx   # Quick capture
│   │   ├── TimelineView.tsx  # Entry feed
│   │   ├── GraphView.tsx     # Knowledge graph
│   │   ├── SearchView.tsx    # Search interface
│   │   └── JARVISView.tsx    # AI assistant
│   ├── services/
│   │   └── api.ts            # Backend API client
│   └── store/
│       └── useStore.ts       # Global state
├── index.html
├── package.json
├── tailwind.config.js
└── vite.config.ts
```

## Component 1: main.tsx - Application Entry Point

**What it does:** Boots up the React application

```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

**Key concepts:**
- **React.StrictMode:** Helps catch bugs in development
- **Root element:** Mounts React app to DOM

## Component 2: App.tsx - Root Component

**What it does:** Main app structure and routing

```typescript
import { useState, useEffect } from 'react'
import { Header } from './components/Header'
import { Sidebar } from './components/Sidebar'
import { CaptureView } from './pages/CaptureView'
import { TimelineView } from './pages/TimelineView'
import { GraphView } from './pages/GraphView'
import { SearchView } from './pages/SearchView'
import { JARVISView } from './pages/JARVISView'
import { useStore } from './store/useStore'

type View = 'capture' | 'timeline' | 'graph' | 'search' | 'jarvis'

export default function App() {
  const [currentView, setCurrentView] = useState<View>('capture')
  const { theme, user } = useStore()

  // Apply theme class to body
  useEffect(() => {
    document.body.className = theme
  }, [theme])

  // Render current view
  const renderView = () => {
    switch (currentView) {
      case 'capture':
        return <CaptureView />
      case 'timeline':
        return <TimelineView />
      case 'graph':
        return <GraphView />
      case 'search':
        return <SearchView />
      case 'jarvis':
        return <JARVISView />
      default:
        return <CaptureView />
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Header />
      
      <div className="flex">
        <Sidebar 
          currentView={currentView}
          onViewChange={setCurrentView}
        />
        
        <main className="flex-1 p-8">
          {renderView()}
        </main>
      </div>
    </div>
  )
}
```

**Key concepts:**
- **State management:** `useState` for current view
- **Conditional rendering:** Different views based on state
- **Global state:** `useStore` for theme and user
- **Responsive layout:** Flexbox for sidebar + main content

## Component 3: useStore.ts - Global State Management

**What it does:** Manages app-wide state using Zustand

```typescript
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface Entry {
  id: string
  content: string
  category: string
  entities: string[]
  actions: string[]
  sentiment: number
  created_at: string
}

interface User {
  id: string
  name: string
  email: string
}

interface StoreState {
  // User
  user: User | null
  setUser: (user: User | null) => void

  // Entries
  entries: Entry[]
  setEntries: (entries: Entry[]) => void
  addEntry: (entry: Entry) => void
  updateEntry: (id: string, updates: Partial<Entry>) => void
  deleteEntry: (id: string) => void

  // UI State
  theme: 'light' | 'dark'
  toggleTheme: () => void

  // Loading states
  isLoading: boolean
  setIsLoading: (loading: boolean) => void
}

export const useStore = create<StoreState>()(
  persist(
    (set, get) => ({
      // User
      user: null,
      setUser: (user) => set({ user }),

      // Entries
      entries: [],
      setEntries: (entries) => set({ entries }),
      
      addEntry: (entry) => set((state) => ({
        entries: [entry, ...state.entries]
      })),
      
      updateEntry: (id, updates) => set((state) => ({
        entries: state.entries.map((entry) =>
          entry.id === id ? { ...entry, ...updates } : entry
        )
      })),
      
      deleteEntry: (id) => set((state) => ({
        entries: state.entries.filter((entry) => entry.id !== id)
      })),

      // UI State
      theme: 'light',
      toggleTheme: () => set((state) => ({
        theme: state.theme === 'light' ? 'dark' : 'light'
      })),

      // Loading
      isLoading: false,
      setIsLoading: (loading) => set({ isLoading: loading })
    }),
    {
      name: 'coherence-storage',  // localStorage key
      partialize: (state) => ({
        user: state.user,
        theme: state.theme
        // Don't persist entries (fetch from server)
      })
    }
  )
)
```

**Key concepts:**
- **Zustand:** Minimal state management
- **TypeScript:** Fully typed store
- **Persistence:** Save to localStorage
- **Immutable updates:** Never mutate state directly

## Component 4: api.ts - Backend API Client

**What it does:** Handles all API calls to backend

```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

// Types
interface EntryCreate {
  content: string
  category?: string
}

interface EntryResponse {
  id: string
  user_id: string
  content: string
  category: string
  entities: string[]
  actions: string[]
  sentiment: number
  summary: string
  key_phrases: string[]
  related_entries: string[]
  created_at: string
  updated_at: string
}

interface SearchParams {
  query: string
  limit?: number
}

class APIClient {
  private baseURL: string
  private token: string | null

  constructor(baseURL: string) {
    this.baseURL = baseURL
    this.token = localStorage.getItem('auth_token')
  }

  // Helper: Make authenticated request
  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    
    const headers = {
      'Content-Type': 'application/json',
      ...(this.token && { 'Authorization': `Bearer ${this.token}` }),
      ...options.headers
    }

    try {
      const response = await fetch(url, {
        ...options,
        headers
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail || 'API request failed')
      }

      return await response.json()
    } catch (error) {
      console.error('API Error:', error)
      throw error
    }
  }

  // Auth
  setToken(token: string) {
    this.token = token
    localStorage.setItem('auth_token', token)
  }

  clearToken() {
    this.token = null
    localStorage.removeItem('auth_token')
  }

  // Entries
  async createEntry(data: EntryCreate): Promise<EntryResponse> {
    return this.request('/api/v1/entries', {
      method: 'POST',
      body: JSON.stringify(data)
    })
  }

  async listEntries(params?: {
    limit?: number
    offset?: number
    category?: string
  }): Promise<EntryResponse[]> {
    const queryParams = new URLSearchParams(
      Object.entries(params || {})
        .filter(([_, v]) => v !== undefined)
        .map(([k, v]) => [k, String(v)])
    )
    
    return this.request(`/api/v1/entries?${queryParams}`)
  }

  async getEntry(id: string): Promise<EntryResponse> {
    return this.request(`/api/v1/entries/${id}`)
  }

  async updateEntry(id: string, updates: Partial<EntryCreate>): Promise<EntryResponse> {
    return this.request(`/api/v1/entries/${id}`, {
      method: 'PUT',
      body: JSON.stringify(updates)
    })
  }

  async deleteEntry(id: string): Promise<void> {
    return this.request(`/api/v1/entries/${id}`, {
      method: 'DELETE'
    })
  }

  // Search
  async semanticSearch(params: SearchParams): Promise<EntryResponse[]> {
    const queryParams = new URLSearchParams({
      query: params.query,
      limit: String(params.limit || 10)
    })
    
    return this.request(`/api/v1/search?${queryParams}`)
  }

  // Knowledge Graph
  async getKnowledgeGraph(): Promise<{
    nodes: any[]
    edges: any[]
  }> {
    return this.request('/api/v1/graph')
  }

  // JARVIS WebSocket
  createJARVISWebSocket(clientId: string): WebSocket {
    const wsURL = this.baseURL.replace('http', 'ws')
    return new WebSocket(`${wsURL}/api/v1/ws/jarvis/${clientId}`)
  }
}

export const api = new APIClient(API_BASE_URL)
```

**Key concepts:**
- **API client pattern:** Centralized API logic
- **Error handling:** Proper try-catch
- **Authentication:** Token-based auth
- **Type safety:** TypeScript interfaces
- **WebSocket support:** For real-time features

## Component 5: Header.tsx - App Header

**What it does:** Top navigation bar

```typescript
import { Sun, Moon, User } from 'lucide-react'
import { useStore } from '../store/useStore'

export function Header() {
  const { theme, toggleTheme, user } = useStore()

  return (
    <header className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
      <div className="px-8 py-4 flex items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-xl">C</span>
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900 dark:text-white">
              Coherence
            </h1>
            <p className="text-xs text-gray-500 dark:text-gray-400">
              Your Personal Intelligence System
            </p>
          </div>
        </div>

        {/* Actions */}
        <div className="flex items-center gap-4">
          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
            aria-label="Toggle theme"
          >
            {theme === 'light' ? (
              <Moon className="w-5 h-5 text-gray-600 dark:text-gray-300" />
            ) : (
              <Sun className="w-5 h-5 text-gray-600 dark:text-gray-300" />
            )}
          </button>

          {/* User Profile */}
          <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-gray-100 dark:bg-gray-700">
            <User className="w-4 h-4 text-gray-600 dark:text-gray-300" />
            <span className="text-sm font-medium text-gray-900 dark:text-white">
              {user?.name || 'Guest'}
            </span>
          </div>
        </div>
      </div>
    </header>
  )
}
```

**Key concepts:**
- **Lucide icons:** Beautiful icon library
- **Theme toggle:** Switch between light/dark
- **Conditional rendering:** Show user info if logged in
- **Tailwind classes:** Responsive, theme-aware styling

## Component 6: Sidebar.tsx - Navigation Sidebar

**What it does:** View navigation

```typescript
import { 
  PenTool, 
  Clock, 
  Network, 
  Search, 
  Sparkles 
} from 'lucide-react'
import { motion } from 'framer-motion'

interface SidebarProps {
  currentView: string
  onViewChange: (view: string) => void
}

const menuItems = [
  { id: 'capture', label: 'Capture', icon: PenTool },
  { id: 'timeline', label: 'Timeline', icon: Clock },
  { id: 'graph', label: 'Graph', icon: Network },
  { id: 'search', label: 'Search', icon: Search },
  { id: 'jarvis', label: 'JARVIS', icon: Sparkles }
]

export function Sidebar({ currentView, onViewChange }: SidebarProps) {
  return (
    <aside className="w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 min-h-[calc(100vh-73px)]">
      <nav className="p-4">
        <ul className="space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon
            const isActive = currentView === item.id

            return (
              <li key={item.id}>
                <motion.button
                  onClick={() => onViewChange(item.id)}
                  className={`
                    w-full flex items-center gap-3 px-4 py-3 rounded-lg
                    transition-colors relative
                    ${isActive 
                      ? 'bg-blue-50 dark:bg-blue-900/20 text-blue-600 dark:text-blue-400' 
                      : 'text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700'
                    }
                  `}
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                >
                  {isActive && (
                    <motion.div
                      layoutId="activeTab"
                      className="absolute inset-0 bg-blue-50 dark:bg-blue-900/20 rounded-lg"
                      transition={{ type: 'spring', bounce: 0.2, duration: 0.6 }}
                    />
                  )}
                  
                  <Icon className="w-5 h-5 relative z-10" />
                  <span className="font-medium relative z-10">
                    {item.label}
                  </span>
                </motion.button>
              </li>
            )
          })}
        </ul>
      </nav>
    </aside>
  )
}
```

**Key concepts:**
- **Framer Motion:** Smooth animations
- **Layout animations:** Animated active indicator
- **Icon mapping:** Dynamic icon components
- **Active state:** Visual feedback

## Component 7: CaptureView.tsx - Quick Capture Interface

**What it does:** Fast entry creation

```typescript
import { useState } from 'react'
import { Send, Loader } from 'lucide-react'
import { motion } from 'framer-motion'
import { api } from '../services/api'
import { useStore } from '../store/useStore'

export function CaptureView() {
  const [content, setContent] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const { addEntry } = useStore()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!content.trim() || isSubmitting) return

    setIsSubmitting(true)

    try {
      // Create entry via API
      const newEntry = await api.createEntry({ content })
      
      // Add to local state
      addEntry(newEntry)
      
      // Clear form
      setContent('')
      
      // Show success (could use toast notification)
      console.log('Entry created:', newEntry)
      
    } catch (error) {
      console.error('Failed to create entry:', error)
      // Show error notification
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="max-w-4xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
          Quick Capture
        </h2>
        <p className="text-gray-600 dark:text-gray-400 mb-8">
          Capture thoughts, ideas, and notes instantly. AI will organize them for you.
        </p>

        <form onSubmit={handleSubmit}>
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 overflow-hidden">
            <textarea
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="What's on your mind? Type anything..."
              className="w-full p-6 bg-transparent text-gray-900 dark:text-white placeholder-gray-400 resize-none focus:outline-none"
              rows={8}
              disabled={isSubmitting}
            />
            
            <div className="px-6 py-4 bg-gray-50 dark:bg-gray-700/50 border-t border-gray-200 dark:border-gray-700 flex justify-between items-center">
              <div className="text-sm text-gray-500 dark:text-gray-400">
                {content.length} characters
              </div>
              
              <button
                type="submit"
                disabled={!content.trim() || isSubmitting}
                className="
                  px-6 py-2.5 rounded-lg font-medium
                  bg-blue-600 hover:bg-blue-700 
                  text-white
                  disabled:opacity-50 disabled:cursor-not-allowed
                  transition-colors
                  flex items-center gap-2
                "
              >
                {isSubmitting ? (
                  <>
                    <Loader className="w-4 h-4 animate-spin" />
                    Processing...
                  </>
                ) : (
                  <>
                    <Send className="w-4 h-4" />
                    Capture
                  </>
                )}
              </button>
            </div>
          </div>
        </form>

        {/* Recent Captures */}
        <div className="mt-8">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Recent Captures
          </h3>
          <RecentEntries />
        </div>
      </motion.div>
    </div>
  )
}

function RecentEntries() {
  const { entries } = useStore()
  const recent = entries.slice(0, 5)

  if (recent.length === 0) {
    return (
      <div className="text-center py-12 text-gray-500 dark:text-gray-400">
        No entries yet. Start capturing your thoughts above!
      </div>
    )
  }

  return (
    <div className="space-y-3">
      {recent.map((entry, index) => (
        <motion.div
          key={entry.id}
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: index * 0.1 }}
          className="p-4 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-blue-300 dark:hover:border-blue-700 transition-colors"
        >
          <p className="text-gray-900 dark:text-white mb-2">
            {entry.content}
          </p>
          <div className="flex items-center gap-4 text-sm text-gray-500 dark:text-gray-400">
            <span>{entry.category}</span>
            <span>•</span>
            <span>{new Date(entry.created_at).toLocaleDateString()}</span>
            {entry.entities.length > 0 && (
              <>
                <span>•</span>
                <span>{entry.entities.length} entities</span>
              </>
            )}
          </div>
        </motion.div>
      ))}
    </div>
  )
}
```

**Key concepts:**
- **Form handling:** Controlled components
- **Async operations:** API calls with loading states
- **Optimistic updates:** Instant UI feedback
- **Animations:** Staggered list animations
- **Error handling:** Try-catch with user feedback

## Component 8: TimelineView.tsx - Chronological Feed

**What it does:** Shows all entries in timeline

```typescript
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Calendar, Tag, TrendingUp, Clock } from 'lucide-react'
import { api } from '../services/api'
import { useStore } from '../store/useStore'
import { format, parseISO } from 'date-fns'

export function TimelineView() {
  const { entries, setEntries } = useStore()
  const [isLoading, setIsLoading] = useState(true)
  const [filter, setFilter] = useState<string | null>(null)

  useEffect(() => {
    loadEntries()
  }, [])

  const loadEntries = async () => {
    try {
      setIsLoading(true)
      const data = await api.listEntries({ limit: 100 })
      setEntries(data)
    } catch (error) {
      console.error('Failed to load entries:', error)
    } finally {
      setIsLoading(false)
    }
  }

  // Group entries by date
  const groupedEntries = entries.reduce((groups, entry) => {
    const date = format(parseISO(entry.created_at), 'yyyy-MM-dd')
    if (!groups[date]) {
      groups[date] = []
    }
    groups[date].push(entry)
    return groups
  }, {} as Record<string, typeof entries>)

  const filteredGroups = filter
    ? Object.entries(groupedEntries).reduce((acc, [date, dateEntries]) => {
        const filtered = dateEntries.filter(e => e.category === filter)
        if (filtered.length > 0) {
          acc[date] = filtered
        }
        return acc
      }, {} as Record<string, typeof entries>)
    : groupedEntries

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto">
      <div className="mb-8">
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
          Timeline
        </h2>
        <p className="text-gray-600 dark:text-gray-400">
          Your knowledge journey, organized chronologically
        </p>
      </div>

      {/* Filters */}
      <div className="mb-6 flex gap-2">
        <FilterButton
          label="All"
          isActive={filter === null}
          onClick={() => setFilter(null)}
        />
        <FilterButton
          label="Work"
          isActive={filter === 'work'}
          onClick={() => setFilter('work')}
        />
        <FilterButton
          label="Ideas"
          isActive={filter === 'idea'}
          onClick={() => setFilter('idea')}
        />
        <FilterButton
          label="Tasks"
          isActive={filter === 'task'}
          onClick={() => setFilter('task')}
        />
        <FilterButton
          label="Notes"
          isActive={filter === 'note'}
          onClick={() => setFilter('note')}
        />
      </div>

      {/* Timeline */}
      <div className="relative">
        {/* Vertical line */}
        <div className="absolute left-8 top-0 bottom-0 w-0.5 bg-gray-200 dark:bg-gray-700" />

        {Object.entries(filteredGroups).map(([date, dateEntries]) => (
          <div key={date} className="mb-12">
            {/* Date header */}
            <div className="flex items-center gap-3 mb-4 sticky top-0 bg-gray-50 dark:bg-gray-900 py-2 z-10">
              <div className="w-16 h-16 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center relative z-10">
                <Calendar className="w-6 h-6 text-blue-600 dark:text-blue-400" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                  {format(parseISO(date), 'MMMM d, yyyy')}
                </h3>
                <p className="text-sm text-gray-500 dark:text-gray-400">
                  {dateEntries.length} entries
                </p>
              </div>
            </div>

            {/* Entries for this date */}
            <div className="ml-24 space-y-4">
              {dateEntries.map((entry, index) => (
                <EntryCard key={entry.id} entry={entry} index={index} />
              ))}
            </div>
          </div>
        ))}
      </div>

      {Object.keys(filteredGroups).length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500 dark:text-gray-400">
            No entries found {filter && `for category: ${filter}`}
          </p>
        </div>
      )}
    </div>
  )
}

function FilterButton({ label, isActive, onClick }: {
  label: string
  isActive: boolean
  onClick: () => void
}) {
  return (
    <button
      onClick={onClick}
      className={`
        px-4 py-2 rounded-lg font-medium transition-colors
        ${isActive
          ? 'bg-blue-600 text-white'
          : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
        }
      `}
    >
      {label}
    </button>
  )
}

function EntryCard({ entry, index }: { entry: any; index: number }) {
  const getSentimentColor = (sentiment: number) => {
    if (sentiment > 0.3) return 'text-green-600 dark:text-green-400'
    if (sentiment < -0.3) return 'text-red-600 dark:text-red-400'
    return 'text-gray-600 dark:text-gray-400'
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05 }}
      className="p-6 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 hover:shadow-md transition-shadow"
    >
      {/* Content */}
      <p className="text-gray-900 dark:text-white mb-4">
        {entry.content}
      </p>

      {/* Summary */}
      {entry.summary && (
        <div className="mb-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
          <p className="text-sm text-blue-900 dark:text-blue-300">
            <strong>Summary:</strong> {entry.summary}
          </p>
        </div>
      )}

      {/* Metadata */}
      <div className="flex flex-wrap items-center gap-4 text-sm text-gray-600 dark:text-gray-400">
        {/* Category */}
        <div className="flex items-center gap-1">
          <Tag className="w-4 h-4" />
          <span className="capitalize">{entry.category}</span>
        </div>

        {/* Time */}
        <div className="flex items-center gap-1">
          <Clock className="w-4 h-4" />
          <span>{format(parseISO(entry.created_at), 'h:mm a')}</span>
        </div>

        {/* Sentiment */}
        {entry.sentiment !== null && (
          <div className={`flex items-center gap-1 ${getSentimentColor(entry.sentiment)}`}>
            <TrendingUp className="w-4 h-4" />
            <span>Sentiment: {(entry.sentiment * 100).toFixed(0)}%</span>
          </div>
        )}

        {/* Entities */}
        {entry.entities.length > 0 && (
          <div>
            <span className="text-gray-400 mr-2">Entities:</span>
            {entry.entities.slice(0, 3).map((entity: any, i: number) => (
              <span
                key={i}
                className="inline-block px-2 py-1 mr-1 bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 rounded text-xs"
              >
                {entity.text}
              </span>
            ))}
            {entry.entities.length > 3 && (
              <span className="text-xs">+{entry.entities.length - 3} more</span>
            )}
          </div>
        )}
      </div>

      {/* Actions */}
      {entry.actions.length > 0 && (
        <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
          <p className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Action Items:
          </p>
          <ul className="space-y-1">
            {entry.actions.map((action: string, i: number) => (
              <li key={i} className="text-sm text-gray-600 dark:text-gray-400 flex items-start gap-2">
                <span className="text-blue-600 dark:text-blue-400">→</span>
                {action}
              </li>
            ))}
          </ul>
        </div>
      )}
    </motion.div>
  )
}
```

**Key concepts:**
- **Data grouping:** Group entries by date
- **Filtering:** Category-based filtering
- **Date formatting:** date-fns library
- **Infinite scroll:** (Would add with IntersectionObserver)
- **Rich metadata display:** Show AI insights

---

<a name="jarvis"></a>
# 8. 🤖 JARVIS - The AI Assistant (Detailed Walkthrough)

JARVIS is the crown jewel of Coherence. Let's understand it completely.

## What Makes JARVIS Special?

**Traditional AI Assistants:**
- Single-shot responses
- No memory of your data
- Generic answers

**JARVIS:**
- Multi-agent collaboration (7 specialized AIs)
- Full access to your personal knowledge
- Context-aware intelligence
- Real-time streaming responses
- Pre-computed insights for speed

## The Multi-Agent Architecture (Inspired by DS-STAR)

Think of JARVIS as a company with specialized departments:

```
┌─────────────────────────────────────────────────────────┐
│                    USER QUERY                            │
│              "What were my priorities this week?"         │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 1: Router                                         │
│  ├─ Determines: This is an "analysis query"             │
│  ├─ Complexity: Medium                                   │
│  └─ Resources needed: user_data, recent_entries          │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 2: Context Builder                                │
│  ├─ Fetches last 7 days of entries (23 entries)         │
│  ├─ Retrieves pre-computed weekly insights (from Redis) │
│  ├─ Extracts entities mentioned in query                │
│  └─ Gathers conversation history                        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 3: Analyzer                                       │
│  ├─ Analyzes 23 entries                                 │
│  ├─ Finds patterns:                                      │
│  │   • "Project X" mentioned 12 times                   │
│  │   • "Design finalization" recurring theme            │
│  │   • 5 meetings about Project X                       │
│  ├─ Identifies trends:                                   │
│  │   • Increasing focus on Project X (up 40%)           │
│  │   • Most active on Tuesday/Wednesday                 │
│  └─ Extracts action items: 12 completed, 5 pending      │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 4: Planner                                        │
│  ├─ Creates response structure:                         │
│  │   1. Summarize top 3 priorities                      │
│  │   2. Show progress metrics                           │
│  │   3. Highlight important patterns                    │
│  │   4. Suggest next steps                              │
│  └─ Determines presentation style: Bullet points + stats│
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 5: Coder (Not needed for this query)             │
│  └─ Skipped                                              │
└──────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 6: Verifier                                       │
│  ├─ Checks: Is analysis accurate? ✓                     │
│  ├─ Checks: Are numbers correct? ✓                      │
│  ├─ Checks: Is response complete? ✓                     │
│  └─ Quality score: 92/100 → Approved                    │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  AGENT 7: Synthesizer (STREAMING)                       │
│  └─ Generates natural language response:                │
│                                                          │
│  "This week, your main priorities were:                 │
│                                                          │
│  1. **Project X Design Finalization** (12 mentions)     │
│     - Had 5 meetings with John and the design team      │
│     - Completed initial mockups                         │
│     - Deadline: This Friday                             │
│                                                          │
│  2. **Team Hiring** (7 mentions)                        │
│     - Reviewed 5 candidates for senior engineer role    │
│     - Scheduled final interviews for 2 candidates       │
│                                                          │
│  3. **Q4 Planning** (4 mentions)                        │
│     - Started outlining Q4 goals                        │
│     - Need to finalize budget                           │
│                                                          │
│  **Progress:** You completed 12 of 17 action items      │
│  (71% completion rate - great work!)                    │
│                                                          │
│  **Pattern:** You're most productive on Tue/Wed.        │
│  Consider scheduling important work then.               │
│                                                          │
│  **Next steps:**                                         │
│  • Finalize Project X design by Friday                  │
│  • Make hiring decisions for the 2 finalists            │
│  • Complete Q4 budget proposal"                         │
└──────────────────────────────────────────────────────────┘
                      │
                      ▼
              USER SEES RESPONSE
         (Streaming word-by-word in real-time)
```

## Real Code Example: How a Query Flows

Let's trace a real query through the system:

**User asks:** "What should I focus on today?"

### Step 1: Frontend Sends Query
```typescript
// JARVISView.tsx
const sendMessage = (query: string) => {
  // Send via WebSocket
  ws.send(JSON.stringify({
    type: 'query',
    message: query,
    timestamp: new Date().toISOString()
  }))
}
```

### Step 2: Backend WebSocket Receives
```python
# jarvis.py
@router.websocket("/ws/jarvis/{client_id}")
async def jarvis_websocket(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    
    while True:
        # Receive message
        data = await websocket.receive_text()
        message = json.loads(data)
        query = message['message']
        
        # Build user context
        user_context = UserContext(
            user_id=get_user_id_from_client(client_id),
            recent_entries=await get_recent_entries(),
            cached_insights=await get_cached_insights(),
            conversation_history=get_conversation_history(client_id)
        )
        
        # Process with JARVIS
        async for agent_message in jarvis_agent.process_query(query, user_context):
            # Send each update to frontend
            await manager.send_message(agent_message.to_dict(), client_id)
```

### Step 3: JARVIS Agent Orchestrates
```python
# jarvis_agent.py
async def process_query(self, user_query: str, user_context: UserContext):
    # Stage 1: Route
    yield AgentMessage(agent="router", type="thinking", content="Analyzing...")
    routing = await self.router.route(user_query, user_context)
    # routing = {"type": "planning_query", "complexity": "low"}
    
    # Stage 2: Build context
    yield AgentMessage(agent="context", type="thinking", content="Gathering info...")
    context = await self.context.enrich(user_query, user_context)
    # context includes today's entries, pending actions, calendar
    
    # Stage 3: Analyze
    yield AgentMessage(agent="analyzer", type="thinking", content="Analyzing patterns...")
    analysis = await self.analyzer.analyze(user_query, context)
    # analysis = {
    #   "urgent_actions": ["Finalize design", "Review PR"],
    #   "meetings_today": 2,
    #   "available_time": "4 hours",
    #   "suggested_priorities": [...]
    # }
    
    # Stage 4: Plan response
    plan = await self.planner.plan(user_query, analysis)
    
    # Stage 5: Synthesize (streaming)
    yield AgentMessage(agent="synthesizer", type="thinking", content="Formulating...")
    
    async for chunk in self.synthesizer.synthesize_streaming(...):
        yield AgentMessage(agent="synthesizer", type="partial", content=chunk)
```

### Step 4: Frontend Displays Streaming Response
```typescript
// JARVISView.tsx
ws.onmessage = (event) => {
  const data = JSON.parse(event.data)
  
  switch (data.type) {
    case 'thinking':
      // Show thinking indicator
      setAgentStatus(`${data.agent} is ${data.content}`)
      break
      
    case 'progress':
      // Show progress update
      showProgress(data.content)
      break
      
    case 'partial':
      // Append to current message (streaming)
      setCurrentMessage(prev => prev + data.content)
      break
      
    case 'complete':
      // Finalize message
      addMessageToHistory({
        role: 'assistant',
        content: data.content,
        metadata: data.metadata
      })
      setAgentStatus(null)
      break
  }
}
```

## Pre-Processor: The Secret to Speed

While you sleep, the pre-processor works:

```python
# Runs every 5 minutes
async def pre_compute_insights(self):
    for user in all_users:
        entries = get_recent_entries(user, days=7)
        
        # Pre-compute common questions
        insights = {
            "top_priorities": analyze_priorities(entries),
            "action_items": extract_actions(entries),
            "trends": identify_trends(entries),
            "suggestions": generate_suggestions(entries),
            "productivity_score": calculate_score(entries)
        }
        
        # Cache in Redis (30 min expiry)
        await redis.set(f"insights:{user.id}", insights, ex=1800)
```

**Result:** When you ask "What are my priorities?" → instant answer (already computed!)

---

<a name="data-flow"></a>
# 9. 🔄 Data Flow - How Information Moves

Let's follow a piece of information from capture to insight.

## Scenario: User Captures a Meeting Note

**User types:**
```
"Met with Sarah about Q4 marketing strategy. 
Need to increase ad spend by 20%. 
Launch new campaign by October 15th."
```

### Flow Diagram:

```
USER INPUT
   │
   ▼
┌────────────────────┐
│ Frontend          │
│ CaptureView.tsx   │
│                   │
│ • User types note │
│ • Clicks "Capture"│
└─────────┬──────────┘
          │ HTTP POST /api/v1/entries
          │ { "content": "Met with..." }
          ▼
┌────────────────────┐
│ Backend API       │
│ entries.py        │
│                   │
│ • Receives request│
│ • Validates data  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────────────────────────────────────────┐
│ AI Processing Pipeline (ai_processor.py)               │
│                                                        │
│ Step 1: Named Entity Recognition (spaCy)              │
│    Input: "Met with Sarah about Q4..."                │
│    Output: entities = [                                │
│        {"text": "Sarah", "type": "PERSON"},           │
│        {"text": "Q4", "type": "DATE"},                │
│        {"text": "October 15th", "type": "DATE"}       │
│    ]                                                   │
│                                                        │
│ Step 2: Action Detection                              │
│    Output: actions = [                                 │
│        "increase ad spend by 20%",                     │
│        "launch new campaign by October 15th"           │
│    ]                                                   │
│                                                        │
│ Step 3: Categorization                                │
│    Keywords: "marketing strategy", "campaign"          │
│    Output: category = "work"                           │
│                                                        │
│ Step 4: Sentiment Analysis                            │
│    Positive words: "new", "strategy"                   │
│    Negative words: none                                │
│    Output: sentiment = 0.3 (slightly positive)         │
│                                                        │
│ Step 5: Summary Generation (GPT-4)                    │
│    Output: summary = "Q4 marketing strategy meeting"   │
│                                                        │
│ Step 6: Key Phrase Extraction                         │
│    Output: key_phrases = [                             │
│        "Q4 marketing strategy",                        │
│        "ad spend increase",                            │
│        "new campaign"                                  │
│    ]                                                   │
└─────────┬──────────────────────────────────────────────┘
          │
          ├─────────────────┬────────────────┬──────────────┐
          │                 │                │              │
          ▼                 ▼                ▼              ▼
┌──────────────┐  ┌────────────────┐  ┌──────────────┐  ┌─────────────┐
│ SQLite DB    │  │ ChromaDB       │  │ Knowledge    │  │ Redis Cache │
│              │  │                │  │ Graph        │  │             │
│ Store entry: │  │ Generate       │  │              │  │ Invalidate  │
│              │  │ embedding:     │  │ Add node:    │  │ user        │
│ id: abc123   │  │                │  │              │  │ insights    │
│ content: ... │  │ vector =       │  │ "abc123"     │  │             │
│ entities: [] │  │ [0.23, -0.45,  │  │ ├─mentions   │  │ (Will be    │
│ actions: []  │  │  0.12, ...]    │  │ │  "Sarah"   │  │ recomputed) │
│ category:    │  │                │  │ └─relates_to │  │             │
│ "work"       │  │ Search similar:│  │   "xyz789"   │  │             │
│ sentiment:   │  │ - entry xyz789 │  │   (similar   │  │             │
│ 0.3          │  │   (0.87 match) │  │   marketing  │  │             │
│ created_at:  │  │ - entry def456 │  │   entry)     │  │             │
│ 2024-11-14   │  │   (0.76 match) │  │              │  │             │
└──────────────┘  └────────────────┘  └──────────────┘  └─────────────┘
          │                 │                │              │
          └─────────────────┴────────────────┴──────────────┘
                             │
                             ▼
                   ┌──────────────────┐
                   │ Return Response  │
                   │                  │
                   │ {                │
                   │   id: "abc123",  │
                   │   content: ...,  │
                   │   entities: ..., │
                   │   actions: ...,  │
                   │   category: ..., │
                   │   summary: ...,  │
                   │   related: [     │
                   │     "xyz789",    │
                   │     "def456"     │
                   │   ]              │
                   │ }                │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Frontend Updates │
                   │                  │
                   │ • Add to store   │
                   │ • Update timeline│
                   │ • Show toast     │
                   │ • Clear form     │
                   └──────────────────┘
                            │
                            ▼
                     USER SEES RESULT
              "Entry captured successfully!"
```

### Later: User Asks JARVIS

**5 days later, user asks:**
```
"What marketing tasks do I have?"
```

```
USER QUERY
   │
   ▼
JARVIS Multi-Agent Processing
   │
   ├─ Router: "This is a task query"
   │
   ├─ Context: Semantic search for "marketing"
   │   └─> Finds entry "abc123" (0.92 similarity)
   │
   ├─ Analyzer: Extracts actions from entry
   │   └─> ["increase ad spend by 20%",
   │        "launch campaign by Oct 15"]
   │
   ├─ Planner: Structure response as checklist
   │
   └─ Synthesizer: Generate natural response
       │
       ▼
  "You have 2 marketing tasks:
  
  1. Increase ad spend by 20%
     (from your meeting with Sarah on Nov 9)
  
  2. Launch new campaign by October 15th
     ⚠️ Deadline approaching!
  
  Would you like me to break these down further?"
```

**The Power:** JARVIS automatically connected:
- Your query (today)
- Entry from 5 days ago
- Extracted action items
- Added context (who, when)
- Flagged urgent deadline

**You didn't have to:**
- Remember the meeting
- Search through notes
- Extract tasks manually
- Check deadlines

---

<a name="examples"></a>
# 10. 💡 Real-World Examples - Step by Step

## Example 1: Entrepreneur Sarah

**Background:**
- Runs a startup
- Captures 20-30 thoughts/day
- Attends 5+ meetings/day
- Needs to track investors, partners, tasks

### Day 1: Monday

**9:00 AM - Morning thought:**
```
Sarah (Capture): "Investor call with John from Sequoia went well. 
They're interested in our Q4 numbers. Need to prep deck by Friday."
```

**What Coherence does:**
- ✅ Identifies entity: "John", "Sequoia"
- ✅ Extracts action: "prep deck by Friday"
- ✅ Category: "work"
- ✅ Adds deadline to calendar integration
- ✅ Links to other "Sequoia" mentions

**2:00 PM - Quick note:**
```
Sarah (Capture): "Team brainstorm - everyone loves the new feature idea.
Alex will prototype, Maria will do market research."
```

**What Coherence does:**
- ✅ Entities: "Alex", "Maria"
- ✅ Actions: "Alex prototype", "Maria market research"
- ✅ Category: "meeting"
- ✅ Creates knowledge graph connections:
  - Alex → prototype feature
  - Maria → market research
  - Both connected to "new feature" node

**5:00 PM - End of day reflection:**
```
Sarah (Capture): "Productive day. Made progress on investor relations 
and product roadmap. Feeling good about Q4."
```

**What Coherence does:**
- ✅ Sentiment: 0.7 (positive)
- ✅ Key phrases: "investor relations", "product roadmap", "Q4"
- ✅ Links to earlier "investor call" entry

### Day 5: Friday

**9:00 AM - Sarah asks JARVIS:**
```
Sarah: "What do I need to finish today?"
```

**JARVIS Response (in 1 second):**
```
JARVIS: "You have 1 urgent task today:

📊 Prep investor deck for Sequoia
- Deadline: Today (Friday)
- Context: From your meeting with John on Monday
- Related: They want Q4 numbers

You also mentioned progress on:
• Product roadmap
• Team feature development (Alex prototyping)

Would you like me to help outline the investor deck?"
```

**How JARVIS knew:**
- Searched entries with deadline = today
- Found "prep deck by Friday" from Monday
- Connected to "John from Sequoia" context
- Pulled in related Q4 mentions
- Offered proactive help

### 2 Weeks Later

**Sarah asks:**
```
Sarah: "Show me everything related to Sequoia"
```

**JARVIS Response:**
```
JARVIS: "I found 4 entries related to Sequoia:

1. Nov 9 - Initial call with John
   - They're interested in Q4 numbers
   - Action: Prep deck (✓ Completed)

2. Nov 13 - Sent deck to John
   - Included Q4 projections
   - Waiting for feedback

3. Nov 15 - Follow-up email
   - John wants to schedule partner meeting

4. Nov 20 - Partner meeting scheduled
   - Date: Nov 27, 2:00 PM
   - Attendees: John, Sarah, 2 other partners

Knowledge Graph shows Sequoia is connected to:
• Q4 financials
• Investor relations
• Fundraising strategy

Would you like to see the full timeline?"
```

**The Power:**
- Complete history automatically organized
- No manual tagging needed
- Knowledge graph shows connections
- Action tracking (completed vs pending)
- Proactive reminders

---

## Example 2: PhD Student Marcus

**Background:**
- Researching machine learning
- Reads 10-15 papers/week
- Multiple projects simultaneously
- Needs to track ideas, citations, experiments

### Week 1

**Monday - Reading papers:**
```
Marcus (Capture): "Read 'Attention Is All You Need' paper. 
Transformer architecture is brilliant. Could apply to my 
protein folding project. Need to test on weekend."
```

**What Coherence does:**
- ✅ Entities: "Attention Is All You Need" (paper)
- ✅ Key phrases: "Transformer architecture", "protein folding"
- ✅ Action: "test on weekend"
- ✅ Category: "research"
- ✅ Creates node: "protein folding project"

**Wednesday - Experiment idea:**
```
Marcus (Capture): "What if we combine transformers with 
graph neural networks for protein structure prediction? 
Check if anyone has done this."
```

**What Coherence does:**
- ✅ Identifies: This is an "idea"
- ✅ Links to Monday's transformer entry
- ✅ Links to protein folding project
- ✅ Action: "check existing research"

**Friday - Found related work:**
```
Marcus (Capture): "AlphaFold2 uses attention mechanisms! 
Reading their paper now. Similar to my idea but different application."
```

**What Coherence does:**
- ✅ Entity: "AlphaFold2"
- ✅ Automatically links to:
  - Monday's transformer entry (similar concepts)
  - Wednesday's idea (confirms direction)
- ✅ Knowledge graph now shows:
  ```
  Transformers ──relates to──> Attention mechanisms
       │                              │
       └──────────┬────────────────────┘
                  │
  Protein Folding ───mentions──> AlphaFold2
       │
       └──connects to──> Marcus's idea
  ```

### Week 3

**Marcus asks JARVIS:**
```
Marcus: "Summarize my protein folding research progress"
```

**JARVIS Response:**
```
JARVIS: "Here's your protein folding research journey:

📚 Key Papers Read:
1. "Attention Is All You Need" (Nov 9)
   - Transformer architecture
   - You noted: Could apply to protein folding

2. "AlphaFold2" paper (Nov 13)
   - Uses attention mechanisms
   - Similar to your idea

💡 Your Original Ideas:
• Combine transformers + graph neural networks
  (Nov 11 - Original idea)
• Apply to protein structure prediction

🧪 Experiments Planned:
• Test transformer on protein data (Pending)
• Compare with AlphaFold2 approach

📊 Knowledge Graph Insights:
Your research connects 3 major areas:
1. Transformer architecture
2. Graph neural networks
3. Protein structure prediction

This is a novel combination! AlphaFold2 uses 
transformers but not GNNs for structure.

💡 Suggestion: 
You have enough background research. Consider 
starting your experiment this weekend as planned.

Would you like me to help outline your experiment 
methodology?"
```

**How JARVIS did this:**
- Semantic search found all protein-related entries
- Knowledge graph revealed connections
- Identified your unique contribution (transformers + GNN)
- Tracked progress (papers read vs experiments done)
- Gave actionable suggestion

### Week 6

**Marcus defending his approach:**
```
Marcus: "How is my approach different from AlphaFold2?"
```

**JARVIS Response:**
```
JARVIS: "Great question! Based on your notes:

**AlphaFold2 (from your Nov 13 reading):**
- Uses attention mechanisms
- Focuses on sequence-to-structure
- Doesn't explicitly model graph structure

**Your Approach (from your Nov 11 idea):**
- Combines transformers AND graph neural networks
- Explicitly models protein as graph
- Could capture structural relationships better

**Key Difference:**
You're adding graph neural network layer to 
explicitly model spatial relationships between amino acids.

**Your Advantage:**
GNNs are designed for graph-structured data (like proteins).
This could improve accuracy for complex structures.

**Evidence from your experiments (Nov 20):**
Your preliminary results show 12% improvement 
on beta-sheet prediction.

**For your thesis:**
Position this as "Graph-Augmented Transformers 
for Protein Structure Prediction"

Would you like me to help draft the related work section?"
```

**The Power:**
- Synthesized months of research
- Identified key differentiator
- Pulled supporting evidence
- Suggested thesis framing
- All from casual notes (no formal structure needed!)

---


<a name="build-roadmap"></a>
# 11. 🛠️ How to Build This - Implementation Roadmap

Let's say you want to build Coherence from scratch. Here's the step-by-step roadmap.

## Phase 1: Foundation (Week 1-2)

### Step 1: Set up Development Environment

```bash
# Create project structure
mkdir coherence-ai
cd coherence-ai
mkdir backend frontend

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy aiosqlite

# Frontend setup
cd ../frontend
npm create vite@latest . -- --template react-ts
npm install
```

### Step 2: Build Basic FastAPI Backend

```python
# backend/app/main.py
from fastapi import FastAPI

app = FastAPI(title="Coherence")

@app.get("/")
async def root():
    return {"message": "Coherence API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

**Test:**
```bash
uvicorn app.main:app --reload
# Visit http://localhost:8000/docs
```

### Step 3: Set Up Database

```python
# backend/app/db/database.py
import aiosqlite

async def init_db():
    db = await aiosqlite.connect("coherence.db")
    
    await db.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id TEXT PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    await db.commit()
    return db
```

### Step 4: Create First Endpoint

```python
# backend/app/api/entries.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EntryCreate(BaseModel):
    content: str

@router.post("/entries")
async def create_entry(entry: EntryCreate):
    # Save to database
    entry_id = str(uuid.uuid4())
    # ... database insert ...
    return {"id": entry_id, "content": entry.content}
```

### Step 5: Build Basic Frontend

```typescript
// frontend/src/App.tsx
import { useState } from 'react'

function App() {
  const [content, setContent] = useState('')
  
  const handleSubmit = async () => {
    const response = await fetch('http://localhost:8000/api/entries', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content })
    })
    const data = await response.json()
    console.log('Created:', data)
  }
  
  return (
    <div>
      <h1>Coherence</h1>
      <textarea 
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Write something..."
      />
      <button onClick={handleSubmit}>Save</button>
    </div>
  )
}
```

**✅ Milestone:** You can capture and save notes!

---

## Phase 2: Add AI Processing (Week 3-4)

### Step 6: Integrate spaCy for NER

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

```python
# backend/app/services/ai_processor.py
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    doc = nlp(text)
    return [
        {"text": ent.text, "type": ent.label_}
        for ent in doc.ents
    ]

# Test
entities = extract_entities("Meeting with John in New York")
# [{"text": "John", "type": "PERSON"}, 
#  {"text": "New York", "type": "GPE"}]
```

### Step 7: Add Sentiment Analysis

```python
def analyze_sentiment(text: str) -> float:
    positive_words = ["good", "great", "excellent", "happy"]
    negative_words = ["bad", "terrible", "awful", "sad"]
    
    text_lower = text.lower()
    pos = sum(1 for word in positive_words if word in text_lower)
    neg = sum(1 for word in negative_words if word in text_lower)
    
    if pos + neg == 0:
        return 0.0
    
    return (pos - neg) / (pos + neg)
```

### Step 8: Update Entry Creation to Use AI

```python
@router.post("/entries")
async def create_entry(entry: EntryCreate):
    # Process with AI
    entities = extract_entities(entry.content)
    sentiment = analyze_sentiment(entry.content)
    
    # Save with AI results
    entry_id = await db.create_entry(
        content=entry.content,
        entities=entities,
        sentiment=sentiment
    )
    
    return {
        "id": entry_id,
        "content": entry.content,
        "entities": entities,
        "sentiment": sentiment
    }
```

**✅ Milestone:** AI extracts information from notes!

---

## Phase 3: Semantic Search (Week 5-6)

### Step 9: Set Up ChromaDB

```bash
pip install chromadb sentence-transformers
```

```python
# backend/app/services/semantic_search.py
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize
client = chromadb.Client()
collection = client.create_collection("entries")
model = SentenceTransformer('all-MiniLM-L6-v2')

def add_to_vector_db(entry_id: str, content: str):
    # Generate embedding
    embedding = model.encode(content).tolist()
    
    # Add to ChromaDB
    collection.add(
        ids=[entry_id],
        embeddings=[embedding],
        documents=[content]
    )

def search_similar(query: str, limit: int = 5):
    # Generate query embedding
    query_embedding = model.encode(query).tolist()
    
    # Search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
    
    return results
```

### Step 10: Add Search Endpoint

```python
@router.get("/search")
async def search_entries(query: str):
    results = search_similar(query, limit=10)
    return {"results": results}
```

### Step 11: Build Search UI

```typescript
// frontend/src/pages/SearchView.tsx
function SearchView() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  
  const handleSearch = async () => {
    const response = await fetch(
      `http://localhost:8000/api/search?query=${query}`
    )
    const data = await response.json()
    setResults(data.results)
  }
  
  return (
    <div>
      <input 
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search anything..."
      />
      <button onClick={handleSearch}>Search</button>
      
      <div>
        {results.map(result => (
          <div key={result.id}>
            <p>{result.content}</p>
            <small>Similarity: {result.similarity}</small>
          </div>
        ))}
      </div>
    </div>
  )
}
```

**✅ Milestone:** Semantic search works!

---

## Phase 4: Knowledge Graph (Week 7-8)

### Step 12: Install NetworkX

```bash
pip install networkx matplotlib
```

### Step 13: Build Graph Service

```python
# backend/app/services/knowledge_graph.py
import networkx as nx

graph = nx.DiGraph()

def add_entry_to_graph(entry_id: str, content: str, entities: list):
    # Add entry node
    graph.add_node(entry_id, content=content, type='entry')
    
    # Add entity nodes and connections
    for entity in entities:
        entity_id = f"entity:{entity['text']}"
        if not graph.has_node(entity_id):
            graph.add_node(entity_id, label=entity['text'], type='entity')
        
        graph.add_edge(entry_id, entity_id, type='mentions')
    
    # Find similar entries and connect
    similar = search_similar(content, limit=3)
    for sim_id in similar:
        if graph.has_node(sim_id):
            graph.add_edge(entry_id, sim_id, type='similar', weight=0.8)

def get_graph_data():
    return {
        "nodes": [
            {"id": node, **data}
            for node, data in graph.nodes(data=True)
        ],
        "edges": [
            {"source": u, "target": v, **data}
            for u, v, data in graph.edges(data=True)
        ]
    }
```

### Step 14: Visualize Graph

```typescript
// frontend/src/pages/GraphView.tsx
import { useEffect, useRef } from 'react'
import ForceGraph2D from 'react-force-graph-2d'

function GraphView() {
  const [graphData, setGraphData] = useState({ nodes: [], links: [] })
  
  useEffect(() => {
    // Fetch graph data
    fetch('http://localhost:8000/api/graph')
      .then(res => res.json())
      .then(data => {
        setGraphData({
          nodes: data.nodes,
          links: data.edges.map(e => ({
            source: e.source,
            target: e.target
          }))
        })
      })
  }, [])
  
  return (
    <ForceGraph2D
      graphData={graphData}
      nodeLabel="label"
      nodeColor={node => node.type === 'entry' ? 'blue' : 'green'}
    />
  )
}
```

**✅ Milestone:** Knowledge graph visualization!

---

## Phase 5: JARVIS AI Assistant (Week 9-12)

### Step 15: Set Up OpenAI

```bash
pip install openai
```

```python
# backend/app/services/jarvis_agent.py
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="your-api-key")

async def chat_with_jarvis(user_query: str, context: dict):
    # Build prompt with context
    prompt = f"""You are JARVIS, an AI assistant with access to the user's knowledge base.

User Query: {user_query}

Relevant Entries:
{context['entries']}

Provide a helpful, contextual response."""
    
    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_query}
        ]
    )
    
    return response.choices[0].message.content
```

### Step 16: Add WebSocket for Real-Time

```bash
pip install websockets
```

```python
# backend/app/api/jarvis.py
from fastapi import WebSocket

@router.websocket("/ws/jarvis/{client_id}")
async def jarvis_websocket(websocket: WebSocket, client_id: str):
    await websocket.accept()
    
    while True:
        # Receive message
        data = await websocket.receive_text()
        message = json.loads(data)
        
        # Get context
        context = await build_context(message['query'])
        
        # Chat with JARVIS (streaming)
        async for chunk in chat_with_jarvis_streaming(message['query'], context):
            await websocket.send_json({
                "type": "partial",
                "content": chunk
            })
        
        # Send complete
        await websocket.send_json({
            "type": "complete"
        })
```

### Step 17: Build Chat UI

```typescript
// frontend/src/pages/JARVISView.tsx
function JARVISView() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const ws = useRef<WebSocket>()
  
  useEffect(() => {
    // Connect to WebSocket
    ws.current = new WebSocket('ws://localhost:8000/api/ws/jarvis/123')
    
    ws.current.onmessage = (event) => {
      const data = JSON.parse(event.data)
      
      if (data.type === 'partial') {
        // Append to current message
        setMessages(prev => {
          const last = prev[prev.length - 1]
          if (last && last.role === 'assistant') {
            return [
              ...prev.slice(0, -1),
              { ...last, content: last.content + data.content }
            ]
          } else {
            return [...prev, { role: 'assistant', content: data.content }]
          }
        })
      }
    }
  }, [])
  
  const sendMessage = () => {
    // Add user message
    setMessages(prev => [...prev, { role: 'user', content: input }])
    
    // Send to WebSocket
    ws.current?.send(JSON.stringify({
      query: input
    }))
    
    setInput('')
  }
  
  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            {msg.content}
          </div>
        ))}
      </div>
      
      <div className="input-area">
        <input 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Ask JARVIS anything..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  )
}
```

**✅ Milestone:** JARVIS works with streaming responses!

---

## Phase 6: Polish & Deploy (Week 13-14)

### Step 18: Add Authentication

```bash
pip install python-jose passlib python-multipart
```

```python
# backend/app/core/auth.py
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def create_access_token(user_id: str) -> str:
    return jwt.encode(
        {"sub": user_id},
        "secret-key",
        algorithm="HS256"
    )

def verify_token(token: str) -> str:
    payload = jwt.decode(token, "secret-key", algorithms=["HS256"])
    return payload["sub"]
```

### Step 19: Set Up Docker

```dockerfile
# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```dockerfile
# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json .
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./backend:/app
  
  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    depends_on:
      - backend
```

### Step 20: Deploy

```bash
# Local deployment
docker-compose up

# Production deployment (example with Railway)
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/you/coherence
git push -u origin main

# 2. Deploy on Railway
# - Connect GitHub repo
# - Set environment variables
# - Deploy
```

**✅ Milestone:** Production-ready application!

---

## Complete Build Timeline

| Phase | Duration | What You Build | Complexity |
|-------|----------|----------------|------------|
| Phase 1 | 2 weeks | Basic backend + frontend, database | ⭐ Easy |
| Phase 2 | 2 weeks | AI processing (NER, sentiment) | ⭐⭐ Moderate |
| Phase 3 | 2 weeks | Semantic search with embeddings | ⭐⭐⭐ Advanced |
| Phase 4 | 2 weeks | Knowledge graph visualization | ⭐⭐⭐ Advanced |
| Phase 5 | 4 weeks | JARVIS multi-agent system | ⭐⭐⭐⭐ Expert |
| Phase 6 | 2 weeks | Auth, deployment, polish | ⭐⭐ Moderate |

**Total: 14 weeks (3.5 months)**

---

<a name="advanced-features"></a>
# 12. 🚀 Advanced Features Explained

## Feature 1: Pre-Processor Background Service

**What it does:** Runs continuously in the background, pre-computing insights

**Why it's powerful:**
- Makes JARVIS responses instant (< 1 second)
- Reduces OpenAI API costs (cache results)
- Discovers patterns you wouldn't ask about

**How it works:**

```python
# Runs every 5 minutes
async def background_processor():
    while True:
        # For each user
        for user in get_active_users():
            # Get recent data
            entries = get_recent_entries(user, days=7)
            
            # Pre-compute common queries
            insights = {
                "summary": summarize(entries),
                "priorities": extract_priorities(entries),
                "trends": identify_trends(entries),
                "suggestions": generate_suggestions(entries)
            }
            
            # Cache in Redis
            await cache.set(f"insights:{user.id}", insights, ex=1800)
        
        # Wait 5 minutes
        await asyncio.sleep(300)
```

**Result:** When user asks "What are my priorities?" → Redis cache hit → instant response

## Feature 2: Multi-Level Caching Strategy

**Level 1: In-Memory Cache (Fastest)**
```python
# Python dictionary
memory_cache = {}

def get_entry(entry_id: str):
    if entry_id in memory_cache:
        return memory_cache[entry_id]  # Instant!
    # ... fetch from database
```

**Level 2: Redis Cache (Very Fast)**
```python
# Distributed cache
async def get_user_insights(user_id: str):
    cached = await redis.get(f"insights:{user_id}")
    if cached:
        return json.loads(cached)  # ~1ms
    # ... compute fresh
```

**Level 3: Database (Fast)**
```python
# SQLite with indexes
await db.execute("SELECT * FROM entries WHERE id = ?", (entry_id,))
# ~10ms with indexes
```

**Level 4: Re-compute (Slowest)**
```python
# Only if all caches miss
result = await ai_processor.process_entry(content)
# ~1000ms (1 second)
```

**Performance:**
- 90% of requests: Level 1/2 (< 10ms)
- 9% of requests: Level 3 (< 50ms)
- 1% of requests: Level 4 (< 1000ms)

## Feature 3: Incremental Graph Updates

**Problem:** Re-building entire knowledge graph is slow (O(n²))

**Solution:** Incremental updates (O(1))

```python
async def add_entry_to_graph(new_entry):
    # Step 1: Add new node (O(1))
    graph.add_node(new_entry.id, **new_entry.data)
    
    # Step 2: Find similar entries (O(log n) with vector index)
    similar = await semantic_search.find_similar(new_entry.content, limit=5)
    
    # Step 3: Add edges (O(1) per edge)
    for similar_entry in similar:
        graph.add_edge(new_entry.id, similar_entry.id, weight=calculate_similarity())
    
    # Total: O(log n) instead of O(n²)
```

## Feature 4: Intelligent Embeddings

**Not all text is equal:**

```python
# Standard approach (wasteful)
embedding = model.encode(entire_document)  # Slow, loses detail

# Our approach (smart)
def create_hybrid_embedding(entry):
    # Separate embeddings for different parts
    title_emb = model.encode(entry.title, normalize=True)
    content_emb = model.encode(entry.content, normalize=True)
    entities_emb = model.encode(", ".join(entry.entities), normalize=True)
    
    # Weighted combination
    hybrid = (
        title_emb * 0.4 +      # Title is important
        content_emb * 0.5 +    # Content is most important
        entities_emb * 0.1     # Entities add context
    )
    
    return hybrid

# Result: Better search accuracy
```

## Feature 5: Adaptive Learning

**The system learns your patterns:**

```python
async def learn_user_patterns(user_id: str):
    entries = await db.get_all_entries(user_id)
    
    # Learn writing style
    avg_length = mean([len(e.content) for e in entries])
    common_categories = Counter([e.category for e in entries])
    active_times = [e.created_at.hour for e in entries]
    
    # Store user profile
    profile = {
        "avg_length": avg_length,
        "preferred_categories": common_categories.most_common(3),
        "most_active_hour": mode(active_times),
        "writing_style": analyze_style(entries)
    }
    
    # Use for better suggestions
    await cache.set(f"profile:{user_id}", profile)
```

**Example usage:**
```python
# When user writes short note at 2 PM
if len(current_entry) < user_profile["avg_length"]:
    suggest("This note is shorter than usual. Want to add more detail?")

if current_time.hour == user_profile["most_active_hour"]:
    pre_warm_cache()  # They'll likely be active soon
```

## Feature 6: Smart Notifications

**Not just reminders - context-aware:**

```python
async def check_for_notifications(user_id: str):
    entries = await get_recent_entries(user_id)
    
    # Detect patterns
    for entry in entries:
        # Deadline approaching
        if entry.has_deadline and entry.deadline_in_days <= 2:
            notify(user_id, f"⚠️ {entry.action} due in {entry.deadline_in_days} days")
        
        # Recurring topic not addressed
        if entry.topic in get_recurring_topics(user_id):
            last_mention = get_last_mention(entry.topic)
            if days_since(last_mention) > 7:
                notify(user_id, f"💡 It's been a week since you mentioned {entry.topic}")
        
        # Related entry you might have forgotten
        similar = await find_similar_entries(entry.id)
        for sim in similar:
            if days_since(sim.created_at) > 30 and sim.relevance_score > 0.9:
                notify(user_id, f"📚 Remember this related note from {sim.date}?")
```

---

<a name="deployment"></a>
# 13. 🌐 Deployment & Scaling

## Local Development

```bash
# Terminal 1: Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm install
npm run dev

# Terminal 3: Redis (optional)
docker run -p 6379:6379 redis
```

## Docker Deployment

```bash
# Build and run
docker-compose up --build

# Production mode
docker-compose -f docker-compose.prod.yml up -d
```

## Cloud Deployment Options

### Option 1: Railway (Easiest)

1. Push to GitHub
2. Connect Railway to repo
3. Set environment variables:
   - `OPENAI_API_KEY`
   - `DATABASE_URL`
   - `REDIS_URL`
4. Deploy automatically

**Cost:** ~$10-20/month

### Option 2: AWS (Most Flexible)

**Architecture:**
```
                    Internet
                       │
                       ▼
                 CloudFront (CDN)
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
   S3 (Frontend)              ALB (Load Balancer)
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                    │
                    ▼                                    ▼
              ECS Task 1                           ECS Task 2
           (Backend Container)                (Backend Container)
                    │                                    │
                    └─────────────────┬──────────────────┘
                                      │
                           ┌──────────┴──────────┐
                           │                     │
                           ▼                     ▼
                    RDS (PostgreSQL)      ElastiCache (Redis)
```

**Services:**
- **Frontend:** S3 + CloudFront
- **Backend:** ECS Fargate (containers)
- **Database:** RDS PostgreSQL
- **Cache:** ElastiCache Redis
- **Vector DB:** Self-hosted ChromaDB on ECS

**Cost:** ~$100-200/month

### Option 3: Vercel + Railway (Recommended)

**Frontend:** Vercel (free tier)
**Backend:** Railway ($20/month)

```bash
# Frontend deployment
npm install -g vercel
cd frontend
vercel deploy

# Backend deployment
# Push to GitHub, connect to Railway
```

## Scaling Strategy

### Phase 1: 0-1,000 users
**Setup:** Single server
- **Backend:** 1 container (2 GB RAM)
- **Database:** SQLite
- **Cache:** Redis (512 MB)

**Cost:** $20/month

### Phase 2: 1,000-10,000 users
**Setup:** Horizontal scaling
- **Backend:** 3 containers behind load balancer
- **Database:** PostgreSQL (managed)
- **Cache:** Redis cluster
- **Vector DB:** Dedicated ChromaDB instance

**Cost:** $200/month

### Phase 3: 10,000-100,000 users
**Setup:** Microservices
```
Load Balancer
├─ API Gateway (3 instances)
├─ AI Processing Service (5 instances)
├─ Search Service (3 instances)
├─ Graph Service (2 instances)
└─ JARVIS Service (5 instances with GPU)

Database Layer
├─ PostgreSQL (Multi-AZ)
├─ Redis Cluster (3 nodes)
└─ Vector DB (Dedicated cluster)
```

**Cost:** $2,000-5,000/month

### Phase 4: 100,000+ users
**Setup:** Full distributed system
- **CDN:** CloudFlare
- **Backend:** Kubernetes cluster (auto-scaling)
- **Database:** Sharded PostgreSQL
- **Cache:** Redis cluster (10+ nodes)
- **Vector DB:** Pinecone or Weaviate (managed)
- **AI:** Dedicated GPU instances

**Cost:** $10,000+/month

## Performance Optimization

### Database Optimization

```sql
-- Essential indexes
CREATE INDEX idx_user_created ON entries(user_id, created_at DESC);
CREATE INDEX idx_category ON entries(category);
CREATE INDEX idx_entities ON entries USING GIN(entities);  -- PostgreSQL

-- Partitioning for scale
CREATE TABLE entries_2024_q1 PARTITION OF entries
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');
```

### Caching Strategy

```python
# Cache expensive operations
@cache(expire=1800)  # 30 minutes
async def get_user_insights(user_id: str):
    # Expensive computation
    return compute_insights(user_id)

# Cache invalidation
async def create_entry(entry):
    await db.save(entry)
    # Invalidate relevant caches
    await cache.delete(f"insights:{entry.user_id}")
    await cache.delete(f"timeline:{entry.user_id}")
```

### Query Optimization

```python
# Bad: N+1 query problem
for entry in entries:
    related = await db.get_related(entry.id)  # Query for each entry!

# Good: Batch query
entry_ids = [e.id for e in entries]
all_related = await db.get_related_batch(entry_ids)  # Single query
```

---

<a name="business"></a>
# 14. 💰 Business Model & Startup Potential

## Market Opportunity

**Total Addressable Market (TAM):**
- Knowledge workers globally: 1 billion+
- Students: 300 million+
- Researchers: 10 million+

**Serviceable Addressable Market (SAM):**
- Tech-savvy professionals: 100 million
- Current note-taking app users: 50 million

**Serviceable Obtainable Market (SOM):**
- Year 1: 10,000 users
- Year 3: 500,000 users
- Year 5: 5 million users

## Pricing Strategy

### Tier 1: Free (Freemium)
- 100 entries/month
- Basic AI processing
- 30-day history
- Community support

**Target:** Students, casual users
**Conversion goal:** 10% to paid

### Tier 2: Pro ($12/month or $120/year)
- Unlimited entries
- Advanced AI (JARVIS)
- Unlimited history
- API access
- Priority support

**Target:** Professionals, power users
**Expected:** 70% of paid users

### Tier 3: Team ($25/user/month)
- Everything in Pro
- Shared knowledge base
- Team collaboration
- Admin controls
- SSO/SAML

**Target:** Small teams (5-50 people)
**Expected:** 25% of paid users

### Tier 4: Enterprise (Custom)
- Everything in Team
- On-premise deployment
- Custom AI models
- Dedicated support
- SLA guarantees

**Target:** Large organizations
**Expected:** 5% of paid users

## Revenue Projections

**Conservative Scenario:**

| Year | Free Users | Paid Users | Monthly Revenue | Annual Revenue |
|------|-----------|------------|-----------------|----------------|
| 1 | 5,000 | 500 | $6,000 | $72,000 |
| 2 | 25,000 | 2,500 | $30,000 | $360,000 |
| 3 | 100,000 | 10,000 | $120,000 | $1.44M |
| 4 | 500,000 | 50,000 | $600,000 | $7.2M |
| 5 | 2,000,000 | 200,000 | $2.4M | $28.8M |

**Optimistic Scenario:** 2-3x these numbers

## Competitive Advantages

### 1. AI-First Design
**Competitors (Notion, Evernote):** Added AI as afterthought
**Coherence:** Built around AI from day one

### 2. Knowledge Graph
**Competitors:** Hierarchical organization (folders, tags)
**Coherence:** Automatic relationship discovery

### 3. JARVIS Multi-Agent System
**Competitors:** Single AI assistant
**Coherence:** 7 specialized agents working together

### 4. Semantic Search
**Competitors:** Keyword search
**Coherence:** Meaning-based search

### 5. Privacy-First
**Competitors:** Cloud-only, data mining
**Coherence:** Local-first option, no data mining

## Go-To-Market Strategy

### Phase 1: Early Adopters (Month 1-6)
- **Launch on Product Hunt**
  - Prepare video demo
  - Build waitlist pre-launch
  - Target: Top 5 product of the day

- **Content Marketing**
  - Blog: "How JARVIS remembers everything you don't"
  - YouTube: Tutorial videos
  - Twitter: AI demos and tips

- **Communities**
  - Hacker News (Show HN)
  - Reddit (r/productivity, r/ai, r/SideProject)
  - Indie Hackers

**Goal:** 1,000 users

### Phase 2: Growth (Month 7-18)
- **SEO Content**
  - "Best note-taking apps for AI"
  - "How to build a second brain"
  - "Personal knowledge management"

- **Influencer Partnerships**
  - Productivity YouTubers
  - Tech reviewers
  - AI thought leaders

- **Viral Features**
  - Share knowledge graphs publicly
  - Social proof (X uses Coherence)
  - Referral program (both get 1 month free)

**Goal:** 50,000 users

### Phase 3: Scale (Month 19+)
- **Paid Advertising**
  - Google Ads (productivity keywords)
  - LinkedIn Ads (professionals)
  - Twitter Ads (AI enthusiasts)

- **Enterprise Sales**
  - Hire sales team
  - Target: Law firms, consulting, research

- **Strategic Partnerships**
  - Integrate with Slack, Teams
  - Academic partnerships (universities)
  - Corporate pilots

**Goal:** 500,000+ users

## Fundraising Strategy

### Bootstrap Phase (Month 1-12)
- **Investment needed:** $0-50,000 (founder money)
- **Use:** Development, hosting, initial marketing
- **Goal:** Product-market fit, 5,000 users

### Seed Round (Month 12-18)
- **Investment target:** $500,000-1M
- **Valuation:** $4-8M
- **Use:** Hiring (2-3 engineers, 1 marketer), scaling infrastructure
- **Goal:** 50,000 users, $50K MRR

### Series A (Month 24-30)
- **Investment target:** $5-10M
- **Valuation:** $30-50M
- **Use:** Team expansion (20+ people), enterprise features, international expansion
- **Goal:** 500,000 users, $500K MRR

## Exit Scenarios

### Acquisition Targets:
1. **Notion** - Add AI-first knowledge management
2. **Microsoft** - Integrate into Microsoft 365
3. **Google** - Enhance Google Workspace
4. **Atlassian** - Complement Confluence
5. **Salesforce** - Add to Einstein AI

**Expected valuation at acquisition:** $100M-500M (after Series B)

### IPO Path:
- Achieve: $50M+ ARR
- Timeline: 7-10 years
- Market cap target: $1B+

---

# 🎉 Conclusion

You now understand:
- ✅ What Coherence is and why it's revolutionary
- ✅ Every technical component in detail
- ✅ How to build it from scratch
- ✅ Real-world use cases and workflows
- ✅ Advanced features and optimizations
- ✅ Deployment and scaling strategies
- ✅ Business model and market opportunity

**This is a startup-grade product worth $100M+**

The technology exists. The market is ready. The problem is real.

**What's stopping you from building the next big thing?**

---

# 📚 Additional Resources

## Learning Paths

**If you're weak in backend:**
1. FastAPI Tutorial (fastapi.tiangolo.com)
2. Python Async/Await (realpython.com)
3. Database Design (postgresqltutorial.com)

**If you're weak in AI/ML:**
1. Sentence Transformers (sbert.net)
2. Vector Databases (pinecone.io/learn)
3. LangChain (langchain.com)

**If you're weak in frontend:**
1. React Docs (react.dev)
2. TypeScript Handbook (typescriptlang.org)
3. Tailwind CSS (tailwindcss.com)

## Tools & Libraries

**Backend:**
- FastAPI: https://fastapi.tiangolo.com
- SQLAlchemy: https://www.sqlalchemy.org
- spaCy: https://spacy.io
- Sentence Transformers: https://sbert.net

**Frontend:**
- React: https://react.dev
- Vite: https://vitejs.dev
- Zustand: https://zustand-demo.pmnd.rs
- Framer Motion: https://www.framer.com/motion

**AI:**
- OpenAI: https://platform.openai.com
- ChromaDB: https://www.trychroma.com
- LangChain: https://langchain.com

**Deployment:**
- Docker: https://www.docker.com
- Railway: https://railway.app
- Vercel: https://vercel.com

## Research Papers

1. "Attention Is All You Need" (Transformers)
2. "BERT: Pre-training of Deep Bidirectional Transformers"
3. "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
4. "DS-STAR: A Framework for LLM-Driven Data Science"

---

**Built with ❤️ by the Coherence Team**

*This guide is a living document. Contribute on GitHub!*
