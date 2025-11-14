"""
AI Processing Service - Core AI engine for understanding and processing entries.
"""
from typing import List, Dict, Any, Optional
import re
from datetime import datetime
from sentence_transformers import SentenceTransformer
from app.core.config import settings
from app.models.entry import (
    AIProcessingResult,
    ExtractedEntity,
    ExtractedAction,
    Priority
)


class AIProcessor:
    """Main AI processing engine."""

    def __init__(self):
        """Initialize AI processor."""
        self.embedding_model = None
        self.nlp = None
        self._initialized = False

    async def initialize(self):
        """Initialize models (lazy loading)."""
        if self._initialized:
            return

        # Load embedding model
        if settings.USE_LOCAL_EMBEDDINGS:
            self.embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)

        # Load spaCy for NER
        try:
            import spacy
            self.nlp = spacy.load(settings.SPACY_MODEL)
        except OSError:
            # Model not downloaded, use simple extraction
            self.nlp = None

        self._initialized = True

    async def process_entry(self, content: str) -> AIProcessingResult:
        """
        Process entry content and extract all AI insights.

        Args:
            content: Text content to process

        Returns:
            AIProcessingResult with extracted information
        """
        await self.initialize()

        # Run all processing in parallel
        categories = await self._extract_categories(content)
        entities = await self._extract_entities(content)
        actions = await self._extract_actions(content)
        summary = await self._generate_summary(content)
        sentiment = await self._analyze_sentiment(content)
        key_phrases = await self._extract_key_phrases(content)

        return AIProcessingResult(
            categories=categories,
            entities=entities,
            actions=actions,
            summary=summary,
            sentiment=sentiment,
            key_phrases=key_phrases
        )

    async def generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding vector for text.

        Args:
            text: Input text

        Returns:
            List of floats representing the embedding
        """
        await self.initialize()

        if self.embedding_model:
            embedding = self.embedding_model.encode(text, convert_to_numpy=True)
            return embedding.tolist()
        else:
            # Fallback to simple hash-based embedding (not recommended for production)
            return [float(hash(text) % 1000) / 1000.0] * 384

    async def _extract_categories(self, content: str) -> List[str]:
        """Extract categories based on content analysis."""
        categories = []
        content_lower = content.lower()

        # Rule-based categorization (can be enhanced with ML)
        category_keywords = {
            'work': ['meeting', 'project', 'deadline', 'client', 'presentation', 'report'],
            'personal': ['family', 'friend', 'home', 'health', 'hobby'],
            'finance': ['money', 'budget', 'invoice', 'payment', 'investment', 'cost'],
            'learning': ['course', 'book', 'tutorial', 'study', 'learn', 'research'],
            'health': ['exercise', 'diet', 'doctor', 'medical', 'wellness'],
            'travel': ['flight', 'hotel', 'trip', 'vacation', 'destination'],
            'shopping': ['buy', 'purchase', 'order', 'shopping'],
            'ideas': ['idea', 'concept', 'brainstorm', 'innovation', 'creative'],
        }

        for category, keywords in category_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                categories.append(category)

        # Default category if none found
        if not categories:
            categories.append('general')

        return categories

    async def _extract_entities(self, content: str) -> List[ExtractedEntity]:
        """Extract named entities from text."""
        entities = []

        if self.nlp:
            doc = self.nlp(content)
            for ent in doc.ents:
                entities.append(ExtractedEntity(
                    text=ent.text,
                    label=ent.label_,
                    start=ent.start_char,
                    end=ent.end_char
                ))
        else:
            # Fallback: simple pattern matching for dates and emails
            # Extract dates (simple patterns)
            date_patterns = [
                r'\b\d{1,2}/\d{1,2}/\d{4}\b',
                r'\b\d{4}-\d{2}-\d{2}\b',
                r'\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b',
                r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}\b'
            ]
            for pattern in date_patterns:
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    entities.append(ExtractedEntity(
                        text=match.group(),
                        label='DATE',
                        start=match.start(),
                        end=match.end()
                    ))

            # Extract emails
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            for match in re.finditer(email_pattern, content):
                entities.append(ExtractedEntity(
                    text=match.group(),
                    label='EMAIL',
                    start=match.start(),
                    end=match.end()
                ))

        return entities

    async def _extract_actions(self, content: str) -> List[ExtractedAction]:
        """Extract actionable items from text."""
        actions = []

        # Action indicators
        action_patterns = [
            (r'(?:need to|must|should|have to|todo:|task:)\s+([^.!?\n]+)', Priority.HIGH),
            (r'(?:will|going to|plan to)\s+([^.!?\n]+)', Priority.MEDIUM),
            (r'(?:could|might|maybe)\s+([^.!?\n]+)', Priority.LOW),
            (r'(?:remember to|don\'t forget to)\s+([^.!?\n]+)', Priority.HIGH),
        ]

        for pattern, priority in action_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                description = match.group(1).strip()
                if len(description) > 10:  # Filter out very short matches
                    # Try to extract due date from description
                    due_date = self._extract_due_date(description)

                    actions.append(ExtractedAction(
                        description=description,
                        priority=priority,
                        due_date=due_date,
                        entry_id=""  # Will be set later
                    ))

        return actions

    def _extract_due_date(self, text: str) -> Optional[datetime]:
        """Extract due date from text."""
        # Simple patterns for common date expressions
        text_lower = text.lower()

        # Today/tomorrow
        if 'today' in text_lower:
            return datetime.utcnow()
        if 'tomorrow' in text_lower:
            from datetime import timedelta
            return datetime.utcnow() + timedelta(days=1)

        # Next week
        if 'next week' in text_lower:
            from datetime import timedelta
            return datetime.utcnow() + timedelta(days=7)

        # Specific date patterns (basic)
        date_pattern = r'\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2})\b'
        match = re.search(date_pattern, text)
        if match:
            try:
                from dateutil import parser
                return parser.parse(match.group(1))
            except:
                pass

        return None

    async def _generate_summary(self, content: str) -> Optional[str]:
        """Generate a summary of the content."""
        # For long content, create a simple extractive summary
        if len(content) > 200:
            sentences = content.split('.')
            # Take first 2 sentences as summary
            summary = '. '.join(sentences[:2]).strip()
            if summary and not summary.endswith('.'):
                summary += '.'
            return summary
        return None

    async def _analyze_sentiment(self, content: str) -> Optional[Dict[str, float]]:
        """Analyze sentiment of content."""
        # Simple rule-based sentiment (can be enhanced with ML models)
        positive_words = ['great', 'good', 'excellent', 'happy', 'excited', 'love', 'awesome', 'wonderful']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'angry', 'sad', 'worried', 'frustrated']
        urgent_words = ['urgent', 'asap', 'immediately', 'critical', 'emergency']

        content_lower = content.lower()

        positive_count = sum(1 for word in positive_words if word in content_lower)
        negative_count = sum(1 for word in negative_words if word in content_lower)
        urgent_count = sum(1 for word in urgent_words if word in content_lower)

        total = positive_count + negative_count + 1  # Avoid division by zero

        return {
            'positive': positive_count / total,
            'negative': negative_count / total,
            'neutral': 1 - (positive_count + negative_count) / total,
            'urgency': min(urgent_count / 3, 1.0)
        }

    async def _extract_key_phrases(self, content: str) -> List[str]:
        """Extract key phrases from content."""
        # Simple extraction based on capitalized phrases and noun chunks
        key_phrases = []

        if self.nlp:
            doc = self.nlp(content)
            # Extract noun chunks
            for chunk in doc.noun_chunks:
                if len(chunk.text.split()) >= 2:  # Multi-word phrases
                    key_phrases.append(chunk.text)
        else:
            # Fallback: extract capitalized multi-word phrases
            capitalized_pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b'
            key_phrases = re.findall(capitalized_pattern, content)

        # Remove duplicates and limit
        key_phrases = list(set(key_phrases))[:10]

        return key_phrases


# Global AI processor instance
ai_processor = AIProcessor()
