"""
Pre-Processor Service - Keeps analysis ready for instant JARVIS responses.

This service runs in the background and:
1. Analyzes user's knowledge base periodically
2. Pre-computes common patterns and insights
3. Caches frequently accessed data
4. Updates indexes for faster retrieval

Think of it as JARVIS "thinking ahead" about what you might ask.
"""

from typing import Dict, List, Any, Optional
import asyncio
from datetime import datetime, timedelta
from collections import Counter
import json
from redis import asyncio as aioredis

from app.db.database import db
from app.services.semantic_search import semantic_search
from app.services.knowledge_graph import knowledge_graph


class PreProcessor:
    """
    Background service that pre-processes user data for instant JARVIS responses.

    This implements a "warm cache" strategy where common analyses are
    ready before the user even asks.
    """

    def __init__(self, redis_url: str = "redis://localhost:6379"):
        """Initialize pre-processor."""
        self.redis_url = redis_url
        self.redis_client: Optional[aioredis.Redis] = None
        self.is_running = False

    async def initialize(self):
        """Initialize Redis connection."""
        self.redis_client = await aioredis.from_url(
            self.redis_url,
            encoding="utf-8",
            decode_responses=True
        )

    async def start(self):
        """Start background processing loop."""
        self.is_running = True

        while self.is_running:
            try:
                # Run all preprocessing tasks
                await asyncio.gather(
                    self.update_user_summaries(),
                    self.pre_compute_insights(),
                    self.refresh_hot_data(),
                    self.update_trending_topics(),
                    return_exceptions=True
                )

                # Wait before next iteration (every 5 minutes)
                await asyncio.sleep(300)

            except Exception as e:
                print(f"PreProcessor error: {e}")
                await asyncio.sleep(60)  # Wait 1 min on error

    async def stop(self):
        """Stop background processing."""
        self.is_running = False
        if self.redis_client:
            await self.redis_client.close()

    async def update_user_summaries(self):
        """
        Generate and cache summaries of user's knowledge base.

        This allows JARVIS to quickly answer "what have I been working on?"
        """
        try:
            # Get all entries
            entries = await db.list_entries(limit=1000)

            # Group by time period
            summaries = {
                "today": [],
                "this_week": [],
                "this_month": [],
                "all_time": []
            }

            now = datetime.utcnow()
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            week_start = today_start - timedelta(days=now.weekday())
            month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

            for entry in entries:
                created_at = datetime.fromisoformat(entry["created_at"])

                summary_item = {
                    "id": entry["id"],
                    "type": entry["type"],
                    "categories": entry.get("ai_categories", []),
                    "created_at": entry["created_at"]
                }

                if created_at >= today_start:
                    summaries["today"].append(summary_item)
                if created_at >= week_start:
                    summaries["this_week"].append(summary_item)
                if created_at >= month_start:
                    summaries["this_month"].append(summary_item)

                summaries["all_time"].append(summary_item)

            # Cache in Redis
            await self.redis_client.setex(
                "user_summaries",
                3600,  # 1 hour TTL
                json.dumps(summaries)
            )

        except Exception as e:
            print(f"Error updating summaries: {e}")

    async def pre_compute_insights(self):
        """
        Pre-compute common insights that users frequently ask about.

        Examples:
        - "What are my top priorities?"
        - "What patterns do you see?"
        - "What should I focus on?"
        """
        try:
            entries = await db.list_entries(limit=500)

            # Compute insights
            insights = {
                "top_categories": self._get_top_categories(entries),
                "recurring_topics": self._get_recurring_topics(entries),
                "action_items_summary": await self._get_action_summary(),
                "productivity_patterns": self._get_productivity_patterns(entries),
                "suggestions": self._generate_suggestions(entries)
            }

            # Cache insights
            await self.redis_client.setex(
                "pre_computed_insights",
                1800,  # 30 min TTL
                json.dumps(insights)
            )

        except Exception as e:
            print(f"Error computing insights: {e}")

    def _get_top_categories(self, entries: List[Dict]) -> List[Dict[str, Any]]:
        """Get most frequent categories."""
        all_categories = []
        for entry in entries:
            all_categories.extend(entry.get("ai_categories", []))

        category_counts = Counter(all_categories)
        return [
            {"category": cat, "count": count}
            for cat, count in category_counts.most_common(10)
        ]

    def _get_recurring_topics(self, entries: List[Dict]) -> List[Dict[str, Any]]:
        """Identify topics that appear repeatedly."""
        # Get all key phrases
        all_phrases = []
        for entry in entries:
            all_phrases.extend(entry.get("ai_key_phrases", []))

        phrase_counts = Counter(all_phrases)

        # Filter to recurring (appears 3+ times)
        recurring = [
            {"topic": phrase, "frequency": count}
            for phrase, count in phrase_counts.items()
            if count >= 3
        ]

        return sorted(recurring, key=lambda x: x["frequency"], reverse=True)[:10]

    async def _get_action_summary(self) -> Dict[str, Any]:
        """Summarize action items."""
        try:
            all_actions = await db.list_actions()

            summary = {
                "total": len(all_actions),
                "by_status": {},
                "by_priority": {},
                "overdue": 0
            }

            now = datetime.utcnow()

            for action in all_actions:
                # By status
                status = action.get("status", "pending")
                summary["by_status"][status] = summary["by_status"].get(status, 0) + 1

                # By priority
                priority = action.get("priority", "medium")
                summary["by_priority"][priority] = summary["by_priority"].get(priority, 0) + 1

                # Overdue
                if action.get("due_date"):
                    due_date = datetime.fromisoformat(action["due_date"])
                    if due_date < now and status != "completed":
                        summary["overdue"] += 1

            return summary

        except:
            return {}

    def _get_productivity_patterns(self, entries: List[Dict]) -> Dict[str, Any]:
        """Analyze productivity patterns."""
        # Group entries by day of week and hour
        by_day = Counter()
        by_hour = Counter()

        for entry in entries:
            try:
                created_at = datetime.fromisoformat(entry["created_at"])
                by_day[created_at.strftime("%A")] += 1
                by_hour[created_at.hour] += 1
            except:
                continue

        return {
            "most_productive_day": by_day.most_common(1)[0][0] if by_day else "Unknown",
            "most_productive_hour": by_hour.most_common(1)[0][0] if by_hour else "Unknown",
            "entries_by_day": dict(by_day),
            "entries_by_hour": dict(by_hour)
        }

    def _generate_suggestions(self, entries: List[Dict]) -> List[str]:
        """Generate proactive suggestions."""
        suggestions = []

        # Check for patterns that warrant suggestions
        recent_entries = sorted(
            entries,
            key=lambda x: x.get("created_at", ""),
            reverse=True
        )[:20]

        # Suggestion 1: Too many tasks?
        pending_tasks = sum(
            1 for e in recent_entries
            if e.get("type") == "task"
        )
        if pending_tasks > 10:
            suggestions.append(
                "You have many pending tasks. Consider prioritizing top 3 for this week."
            )

        # Suggestion 2: Recurring topic?
        all_categories = []
        for entry in recent_entries:
            all_categories.extend(entry.get("ai_categories", []))

        most_common = Counter(all_categories).most_common(1)
        if most_common and most_common[0][1] >= 5:
            suggestions.append(
                f"You've mentioned '{most_common[0][0]}' frequently. "
                f"Want to create a dedicated project for it?"
            )

        # Suggestion 3: No entries today?
        today_entries = [
            e for e in recent_entries
            if datetime.fromisoformat(e.get("created_at", "")).date() == datetime.utcnow().date()
        ]
        if not today_entries:
            suggestions.append(
                "No entries today yet. Start with a quick brain dump of what's on your mind."
            )

        return suggestions

    async def refresh_hot_data(self):
        """
        Cache frequently accessed data for instant retrieval.

        "Hot data" = data accessed >10 times in the last hour
        """
        try:
            # Get frequently searched queries (would need analytics tracking)
            # For now, cache the most central nodes in knowledge graph

            central_nodes = await knowledge_graph.get_central_nodes(limit=20)

            # Cache each central node's subgraph
            for node in central_nodes:
                entry_id = node["entry_id"]
                subgraph = await knowledge_graph.get_subgraph(entry_id, depth=2)

                await self.redis_client.setex(
                    f"hot_graph:{entry_id}",
                    1800,  # 30 min
                    json.dumps(subgraph.dict())
                )

        except Exception as e:
            print(f"Error refreshing hot data: {e}")

    async def update_trending_topics(self):
        """
        Identify what's trending in user's recent activity.

        Helps JARVIS proactively surface: "I notice you're focused on X lately..."
        """
        try:
            # Get recent entries (last 7 days)
            all_entries = await db.list_entries(limit=500)

            week_ago = datetime.utcnow() - timedelta(days=7)
            recent_entries = [
                e for e in all_entries
                if datetime.fromisoformat(e.get("created_at", "")) >= week_ago
            ]

            # Extract trending categories
            recent_categories = []
            for entry in recent_entries:
                recent_categories.extend(entry.get("ai_categories", []))

            category_counts = Counter(recent_categories)

            trending = [
                {
                    "topic": cat,
                    "mentions": count,
                    "trend": "up"  # Could calculate actual trend by comparing to previous week
                }
                for cat, count in category_counts.most_common(10)
            ]

            await self.redis_client.setex(
                "trending_topics",
                3600,  # 1 hour
                json.dumps(trending)
            )

        except Exception as e:
            print(f"Error updating trending: {e}")

    async def get_cached_insights(self) -> Optional[Dict[str, Any]]:
        """Retrieve pre-computed insights from cache."""
        try:
            cached = await self.redis_client.get("pre_computed_insights")
            if cached:
                return json.loads(cached)
        except:
            pass
        return None

    async def get_user_summary(self, period: str = "this_week") -> Optional[List[Dict]]:
        """Get cached user summary for a time period."""
        try:
            cached = await self.redis_client.get("user_summaries")
            if cached:
                summaries = json.loads(cached)
                return summaries.get(period, [])
        except:
            pass
        return None


# Global pre-processor instance
pre_processor = PreProcessor()