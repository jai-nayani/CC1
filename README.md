# Coherence - AI-Powered Universal Personal Intelligence System

<div align="center">

**The world's first truly AI-native personal knowledge and action system**

[Features](#-key-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [API Docs](#-api-documentation)

</div>

---

## 🌟 What is Coherence?

Coherence is a revolutionary personal intelligence system that transforms how you capture, organize, and interact with information. Unlike traditional note-taking apps, Coherence uses advanced AI to:

- **Understand** your information deeply through multi-modal AI processing
- **Connect** disparate pieces of knowledge automatically
- **Surface** relevant information proactively before you search
- **Act** by converting your thoughts into actionable tasks
- **Evolve** your personal knowledge graph over time

## 🚀 Why Coherence is Revolutionary

### The Problem
Knowledge workers waste **30% of their day** searching for information scattered across multiple apps. Notes never become actions. Context is constantly lost. Information doesn't compound into knowledge.

### The Solution
Coherence is the first AI-first personal operating system that:

1. **Universal Capture** - Capture anything instantly: text, voice, images, PDFs
2. **Automatic Understanding** - AI processes and categorizes every input
3. **Semantic Search** - Find information by meaning, not just keywords
4. **Knowledge Graphs** - Visualize how your ideas interconnect
5. **Action Intelligence** - Automatically extracts tasks, deadlines, and priorities
6. **Proactive Retrieval** - Surfaces relevant info before you need it
7. **Privacy-First** - Local processing option, your data stays yours

## ✨ Key Features

### 🧠 AI-Powered Processing
- **Multi-Modal Understanding**: Process text, voice, images, and PDFs with deep semantic analysis
- **Automatic Categorization**: AI automatically tags and organizes every piece of information
- **Entity Extraction**: Identifies people, places, organizations, dates, and concepts
- **Sentiment Analysis**: Understands emotional context and priority

### 🕸️ Dynamic Knowledge Graph
- **Automatic Linking**: Discovers connections between related information
- **Visual Exploration**: Interactive graph visualization of your knowledge
- **Temporal Context**: Time-aware connections and relevance scoring
- **Emergent Insights**: Surfaces unexpected connections and patterns

### ⚡ Action Intelligence
- **Smart Task Extraction**: Converts thoughts to actionable items automatically
- **Priority Detection**: AI determines urgency and importance
- **Deadline Recognition**: Extracts and schedules time-sensitive items
- **Context Preservation**: Tasks maintain links to source information

### 🔍 Proactive Intelligence
- **Contextual Surfacing**: Shows relevant information based on what you're working on
- **Smart Suggestions**: Recommends related notes and resources
- **Pattern Recognition**: Learns from your usage patterns
- **Predictive Retrieval**: Anticipates information needs

### 🔒 Privacy-First Design
- **Local Processing**: Option to run embeddings and processing locally
- **Encrypted Storage**: All data encrypted at rest
- **No Vendor Lock-in**: Export your data anytime in standard formats
- **Transparent AI**: See exactly how AI processes your information

## 🎯 Startup Potential

### Market Opportunity
- **Market Size**: $50B+ productivity software market
- **Target Users**: 500M+ knowledge workers globally
- **Growth Rate**: 15% CAGR in productivity tools

### Competitive Advantages
1. **First-mover**: No other AI-native personal intelligence system exists
2. **Network Effects**: Learns from aggregate patterns (privacy-preserving)
3. **Proprietary AI**: Custom models trained on knowledge work patterns
4. **Sticky Product**: Becomes more valuable with usage

### Business Model
- **Freemium**: Free tier with basic features
- **Premium**: $15/month for advanced AI and unlimited storage
- **Teams**: $30/user/month with collaboration features
- **Enterprise**: Custom pricing with SSO and advanced security

## 🏗️ Architecture

```
coherence/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Core configuration
│   │   ├── models/         # Data models
│   │   ├── services/       # Business logic
│   │   │   ├── ai_processor.py      # AI processing engine
│   │   │   ├── knowledge_graph.py   # Graph generation
│   │   │   ├── semantic_search.py   # Vector search
│   │   │   └── action_intelligence.py # Task extraction
│   │   └── db/             # Database layer
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API clients
│   │   ├── store/          # State management
│   │   └── utils/          # Utilities
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml      # Multi-container setup
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose (recommended)
- OR: Python 3.11+, Node.js 18+
- Optional: OpenAI API key for advanced features

### Installation with Docker (Recommended)

1. **Clone the repository**
```bash
git clone <repository-url>
cd CC1
```

2. **Set up environment variables**
```bash
# Create .env file in backend directory
echo "OPENAI_API_KEY=your_key_here_optional" > backend/.env
```

3. **Start the application**
```bash
docker-compose up -d
```

4. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Manual Setup (Development)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

## 📚 Usage Examples

### Capture Information
```bash
curl -X POST http://localhost:8000/api/v1/entries \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Meeting with investors next Tuesday at 3pm to discuss Series A funding",
    "type": "note"
  }'
```

AI automatically:
- Extracts task: "Meeting with investors"
- Identifies date: "next Tuesday at 3pm"
- Categorizes as: business, funding
- Links to related: previous investor notes

### Semantic Search
```bash
curl "http://localhost:8000/api/v1/search?query=funding%20discussions&limit=10"
```

Returns relevant entries even if they don't contain exact words.

### Explore Knowledge Graph
```bash
curl "http://localhost:8000/api/v1/graph?entry_id=123&depth=2"
```

Returns interconnected nodes and relationships.

## 🔧 API Documentation

Full interactive API documentation available at `http://localhost:8000/docs` when running the backend.

### Key Endpoints

**Entries**
- `POST /api/v1/entries` - Create new entry
- `GET /api/v1/entries` - List entries with filters
- `GET /api/v1/entries/{id}` - Get specific entry
- `PUT /api/v1/entries/{id}` - Update entry
- `DELETE /api/v1/entries/{id}` - Delete entry

**Search**
- `GET /api/v1/search` - Semantic search
- `POST /api/v1/search/advanced` - Advanced search with filters

**Knowledge Graph**
- `GET /api/v1/graph` - Get knowledge graph
- `GET /api/v1/graph/nodes/{id}` - Get node details
- `GET /api/v1/graph/connections` - Get suggested connections

**Actions**
- `GET /api/v1/actions` - List extracted actions
- `PUT /api/v1/actions/{id}` - Update action status
- `POST /api/v1/actions/{id}/complete` - Mark action complete

**Intelligence**
- `GET /api/v1/intelligence/suggestions` - Get contextual suggestions
- `POST /api/v1/intelligence/analyze` - Analyze entry for insights

## 🎨 Frontend Features

### Modern UI/UX
- **Clean Interface**: Minimalist design focused on content
- **Dark Mode**: Easy on the eyes for extended use
- **Keyboard Shortcuts**: Power-user friendly
- **Mobile Responsive**: Works on all devices

### Key Views
1. **Capture View**: Quick input for any type of information
2. **Timeline View**: Chronological feed of all entries
3. **Graph View**: Interactive knowledge graph visualization
4. **Actions View**: Task list with AI-extracted items
5. **Search View**: Powerful semantic search interface
6. **Insights View**: AI-generated patterns and suggestions

## 🔬 Technical Deep Dive

### AI Processing Pipeline

1. **Ingestion**: Entry received via API
2. **Preprocessing**: Text normalization, cleaning
3. **Embedding**: Generate vector representation (sentence-transformers)
4. **Entity Extraction**: NER for people, places, dates
5. **Classification**: Auto-categorize by topic
6. **Action Detection**: Identify tasks and deadlines
7. **Graph Update**: Add nodes and edges
8. **Semantic Indexing**: Store in ChromaDB

### Tech Stack
- **Backend**: FastAPI, Python 3.11+
- **AI/ML**: Sentence-Transformers, spaCy, OpenAI (optional)
- **Vector DB**: ChromaDB
- **Graph**: NetworkX
- **Frontend**: React 18, TypeScript, TailwindCSS
- **Visualization**: React Flow, D3.js
- **State**: Zustand
- **Storage**: SQLite + JSON

## 🚢 Deployment

### Docker Deployment (Recommended)
```bash
docker-compose up -d
```

### Environment Variables
```bash
# Backend (.env)
OPENAI_API_KEY=sk-xxx  # Optional
DATABASE_URL=sqlite:///./coherence.db
CHROMA_PERSIST_DIR=./chroma_db
CORS_ORIGINS=http://localhost:3000
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

Built with modern AI/ML tools to augment human intelligence and productivity.

---

<div align="center">

**Built for knowledge workers who want to think better, not just work faster**

</div>
