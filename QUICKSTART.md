# Coherence - Quick Start Guide

Get up and running with Coherence in 5 minutes!

## 🚀 Fastest Way: Docker Compose (Recommended)

### Prerequisites
- Docker and Docker Compose installed
- 4GB RAM minimum
- 2GB disk space

### Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd CC1
```

2. **Start the application**
```bash
docker-compose up -d
```

3. **Wait for initialization** (30-60 seconds)
The backend will download AI models on first run.

4. **Open your browser**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

5. **Start capturing!**
Click "Capture" and start writing. AI will automatically:
- Organize your content
- Extract action items
- Build knowledge connections
- Enable semantic search

### Stop the application
```bash
docker-compose down
```

### View logs
```bash
# All services
docker-compose logs -f

# Backend only
docker-compose logs -f backend

# Frontend only
docker-compose logs -f frontend
```

---

## 💻 Manual Setup (Development)

### Backend

1. **Navigate to backend**
```bash
cd backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download spaCy model**
```bash
python -m spacy download en_core_web_sm
```

5. **Create .env file** (optional)
```bash
cp .env.example .env
# Edit .env if you want to add OpenAI API key
```

6. **Run the backend**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at http://localhost:8000

### Frontend

1. **Navigate to frontend** (in new terminal)
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Run development server**
```bash
npm run dev
```

Frontend will be available at http://localhost:3000

---

## 🎯 First Steps

### 1. Capture Your First Entry
- Click "Capture" in the sidebar
- Write anything: a note, idea, or task
- Click "Capture" button
- AI processes it in seconds!

### 2. Explore Your Timeline
- Click "Timeline" to see all entries
- Filter by type (note, task, idea, etc.)
- See AI-generated categories and summaries

### 3. Search Semantically
- Click "Search"
- Try: "ideas about AI" or "meetings last week"
- Search understands meaning, not just keywords!

### 4. Visualize Knowledge Graph
- Click "Knowledge Graph"
- See how your ideas connect
- Adjust depth and similarity thresholds

---

## 🔧 Configuration

### Optional: OpenAI Integration

For advanced features (better summaries, insights):

1. Get an OpenAI API key from https://platform.openai.com
2. Add to backend/.env:
```
OPENAI_API_KEY=sk-your-key-here
```
3. Restart backend

**Note**: Core features work without OpenAI using local models!

---

## 📊 System Requirements

### Minimum
- **RAM**: 4GB
- **Disk**: 2GB
- **CPU**: 2 cores
- **OS**: Linux, macOS, Windows (with WSL2)

### Recommended
- **RAM**: 8GB+
- **Disk**: 5GB+
- **CPU**: 4 cores+

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Python version (need 3.11+)
python --version

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Download spaCy model again
python -m spacy download en_core_web_sm
```

### Frontend won't start
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Docker issues
```bash
# Rebuild containers
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Port conflicts
Edit docker-compose.yml to use different ports:
```yaml
ports:
  - "8001:8000"  # Backend
  - "3001:80"    # Frontend
```

---

## 💡 Tips

1. **Keyboard Shortcuts**: Coming soon!
2. **Batch Import**: You can import existing notes via API
3. **Export Data**: All data is yours - export anytime
4. **Dark Mode**: Toggle in header
5. **Mobile**: Responsive design works on mobile

---

## 🆘 Need Help?

- **Issues**: Open a GitHub issue
- **Docs**: Check README.md
- **API Docs**: http://localhost:8000/docs

---

## 🎉 You're All Set!

Start capturing your thoughts and let AI organize them for you.

**Remember**: The more you use it, the smarter it gets!
