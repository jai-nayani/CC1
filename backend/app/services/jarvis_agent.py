"""
JARVIS - Advanced Conversational AI Research Agent for Coherence

This module implements a state-of-the-art conversational AI agent inspired by DS-STAR
that provides JARVIS-like intelligent assistance with:
- Real-time streaming responses
- Multi-agent orchestration
- Context-aware analysis
- Research and planning capabilities
"""

from typing import List, Dict, Any, AsyncGenerator, Optional
from dataclasses import dataclass
from enum import Enum
import asyncio
import json
from datetime import datetime
import openai
from pydantic import BaseModel


class AgentRole(str, Enum):
    """Agent roles in the multi-agent system."""
    ROUTER = "router"
    CONTEXT = "context"
    ANALYZER = "analyzer"
    PLANNER = "planner"
    CODER = "coder"
    VERIFIER = "verifier"
    SYNTHESIZER = "synthesizer"


class MessageType(str, Enum):
    """Types of messages in the system."""
    THINKING = "thinking"
    PROGRESS = "progress"
    PARTIAL = "partial"
    COMPLETE = "complete"
    ERROR = "error"
    ACTION = "action"


@dataclass
class AgentMessage:
    """Message passed between agents."""
    role: AgentRole
    message_type: MessageType
    content: str
    metadata: Dict[str, Any]
    timestamp: datetime

    def to_dict(self) -> Dict[str, Any]:
        return {
            "role": self.role.value,
            "type": self.message_type.value,
            "content": self.content,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat()
        }


class UserContext(BaseModel):
    """Context extracted from user's knowledge base."""
    user_id: str
    relevant_entries: List[Dict[str, Any]]
    knowledge_graph_summary: Dict[str, Any]
    user_preferences: Dict[str, Any]
    recent_activity: List[Dict[str, Any]]
    active_goals: List[str]
    conversation_history: List[Dict[str, Any]]


class AgentResponse(BaseModel):
    """Structured response from an agent."""
    agent: AgentRole
    status: str
    data: Dict[str, Any]
    next_agent: Optional[AgentRole] = None
    confidence: float = 1.0


class JARVISAgent:
    """
    Main JARVIS conversational AI agent.

    Orchestrates multiple specialized agents to provide intelligent,
    context-aware responses with minimal latency.
    """

    def __init__(
        self,
        openai_api_key: str,
        model: str = "gpt-4-turbo-preview",
        temperature: float = 0.7,
        streaming: bool = True
    ):
        """Initialize JARVIS agent."""
        self.client = openai.AsyncOpenAI(api_key=openai_api_key)
        self.model = model
        self.temperature = temperature
        self.streaming = streaming

        # Agent instances
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
        Process user query through multi-agent system with streaming.

        Args:
            user_query: User's question or request
            user_context: Context from user's knowledge base

        Yields:
            AgentMessage objects for streaming to UI
        """
        try:
            # Stage 1: Route the query
            yield AgentMessage(
                role=AgentRole.ROUTER,
                message_type=MessageType.THINKING,
                content="Understanding your request...",
                metadata={"stage": "routing"},
                timestamp=datetime.utcnow()
            )

            routing = await self.router.route(user_query, user_context)

            # Stage 2: Build context
            yield AgentMessage(
                role=AgentRole.CONTEXT,
                message_type=MessageType.PROGRESS,
                content="Analyzing your knowledge base...",
                metadata={"stage": "context", "entries_found": len(user_context.relevant_entries)},
                timestamp=datetime.utcnow()
            )

            enriched_context = await self.context.enrich(user_query, user_context)

            # Stage 3: Analyze based on routing
            if routing.data["needs_research"]:
                yield AgentMessage(
                    role=AgentRole.ANALYZER,
                    message_type=MessageType.PROGRESS,
                    content="Performing deep analysis...",
                    metadata={"stage": "analysis"},
                    timestamp=datetime.utcnow()
                )

                analysis = await self.analyzer.analyze(user_query, enriched_context)

                # Stage 4: Create plan if needed
                if routing.data["needs_plan"]:
                    yield AgentMessage(
                        role=AgentRole.PLANNER,
                        message_type=MessageType.PROGRESS,
                        content="Creating action plan...",
                        metadata={"stage": "planning"},
                        timestamp=datetime.utcnow()
                    )

                    plan = await self.planner.create_plan(user_query, analysis, enriched_context)

                    # Stage 5: Generate code if needed
                    if routing.data["needs_code"]:
                        yield AgentMessage(
                            role=AgentRole.CODER,
                            message_type=MessageType.PROGRESS,
                            content="Generating implementation...",
                            metadata={"stage": "coding"},
                            timestamp=datetime.utcnow()
                        )

                        code = await self.coder.generate(plan, enriched_context)

                        # Stage 6: Verify the solution
                        yield AgentMessage(
                            role=AgentRole.VERIFIER,
                            message_type=MessageType.PROGRESS,
                            content="Verifying solution...",
                            metadata={"stage": "verification"},
                            timestamp=datetime.utcnow()
                        )

                        verification = await self.verifier.verify(code, plan, user_query)

                        if not verification.data["is_sufficient"]:
                            # Refinement loop (DS-STAR iterative approach)
                            max_iterations = 3
                            for iteration in range(max_iterations):
                                yield AgentMessage(
                                    role=AgentRole.PLANNER,
                                    message_type=MessageType.PROGRESS,
                                    content=f"Refining solution (iteration {iteration + 1})...",
                                    metadata={"stage": "refinement", "iteration": iteration + 1},
                                    timestamp=datetime.utcnow()
                                )

                                plan = await self.planner.refine_plan(
                                    plan,
                                    verification.data["feedback"]
                                )
                                code = await self.coder.generate(plan, enriched_context)
                                verification = await self.verifier.verify(code, plan, user_query)

                                if verification.data["is_sufficient"]:
                                    break

            # Final Stage: Synthesize response
            yield AgentMessage(
                role=AgentRole.SYNTHESIZER,
                message_type=MessageType.THINKING,
                content="Preparing response...",
                metadata={"stage": "synthesis"},
                timestamp=datetime.utcnow()
            )

            # Stream the final response
            async for chunk in self.synthesizer.synthesize_streaming(
                user_query,
                enriched_context,
                analysis if routing.data["needs_research"] else None,
                plan if routing.data.get("needs_plan") else None,
                code if routing.data.get("needs_code") else None
            ):
                yield AgentMessage(
                    role=AgentRole.SYNTHESIZER,
                    message_type=MessageType.PARTIAL,
                    content=chunk,
                    metadata={"stage": "response"},
                    timestamp=datetime.utcnow()
                )

            # Mark as complete
            yield AgentMessage(
                role=AgentRole.SYNTHESIZER,
                message_type=MessageType.COMPLETE,
                content="",
                metadata={"stage": "complete"},
                timestamp=datetime.utcnow()
            )

        except Exception as e:
            yield AgentMessage(
                role=AgentRole.SYNTHESIZER,
                message_type=MessageType.ERROR,
                content=f"I encountered an issue: {str(e)}",
                metadata={"error": str(e)},
                timestamp=datetime.utcnow()
            )


class RouterAgent:
    """Determines the execution path for a query."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def route(self, query: str, context: UserContext) -> AgentResponse:
        """Route query to appropriate processing path."""

        prompt = f"""You are a routing agent. Analyze this query and determine:
1. Does it need research/analysis? (search through knowledge base)
2. Does it need a plan? (multi-step solution)
3. Does it need code? (implementation)

Query: {query}

User has {len(context.relevant_entries)} relevant entries.

Respond in JSON:
{{
    "needs_research": bool,
    "needs_plan": bool,
    "needs_code": bool,
    "complexity": "simple|medium|complex",
    "reasoning": "brief explanation"
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )

        data = json.loads(response.choices[0].message.content)

        return AgentResponse(
            agent=AgentRole.ROUTER,
            status="success",
            data=data,
            next_agent=AgentRole.CONTEXT
        )


class ContextAgent:
    """Enriches context from user's knowledge base."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def enrich(self, query: str, context: UserContext) -> Dict[str, Any]:
        """Enrich context with relevant information."""

        # Extract key insights from relevant entries
        entries_summary = []
        for entry in context.relevant_entries[:10]:  # Top 10 most relevant
            entries_summary.append({
                "content": entry.get("content", "")[:200],  # First 200 chars
                "categories": entry.get("ai_categories", []),
                "created_at": entry.get("created_at"),
                "key_phrases": entry.get("ai_key_phrases", [])
            })

        # Build enriched context
        enriched = {
            "query": query,
            "relevant_entries": entries_summary,
            "total_entries": len(context.relevant_entries),
            "user_goals": context.active_goals,
            "preferences": context.user_preferences,
            "recent_activity": context.recent_activity[:5],
            "graph_summary": context.knowledge_graph_summary
        }

        return enriched


class AnalyzerAgent:
    """Performs deep analysis using DS-STAR approach."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def analyze(self, query: str, context: Dict[str, Any]) -> AgentResponse:
        """Analyze query in context of user's knowledge."""

        prompt = f"""You are an expert data analyst. Analyze this query based on the user's knowledge.

Query: {query}

User's Context:
- {context['total_entries']} relevant entries found
- Active goals: {', '.join(context['user_goals'])}
- Recent topics: {', '.join([e['categories'] for e in context['relevant_entries'][:3]])}

Relevant Information:
{json.dumps(context['relevant_entries'], indent=2)}

Provide analysis in JSON:
{{
    "key_insights": ["insight1", "insight2", ...],
    "patterns": ["pattern1", "pattern2", ...],
    "recommendations": ["rec1", "rec2", ...],
    "related_topics": ["topic1", "topic2", ...],
    "confidence": 0.0-1.0
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.3
        )

        data = json.loads(response.choices[0].message.content)

        return AgentResponse(
            agent=AgentRole.ANALYZER,
            status="success",
            data=data,
            confidence=data.get("confidence", 0.8)
        )


class PlannerAgent:
    """Creates execution plans using DS-STAR sequential planning."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def create_plan(
        self,
        query: str,
        analysis: AgentResponse,
        context: Dict[str, Any]
    ) -> AgentResponse:
        """Create a step-by-step plan."""

        prompt = f"""You are a planning expert. Create a detailed action plan.

Query: {query}

Analysis Results:
{json.dumps(analysis.data, indent=2)}

Create a plan in JSON:
{{
    "goal": "clear goal statement",
    "steps": [
        {{
            "step_number": 1,
            "action": "what to do",
            "reasoning": "why this step",
            "expected_output": "what you'll get",
            "dependencies": []
        }}
    ],
    "estimated_time": "time estimate",
    "success_criteria": ["criterion1", "criterion2"]
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.2
        )

        data = json.loads(response.choices[0].message.content)

        return AgentResponse(
            agent=AgentRole.PLANNER,
            status="success",
            data=data
        )

    async def refine_plan(self, plan: AgentResponse, feedback: str) -> AgentResponse:
        """Refine plan based on verifier feedback."""

        prompt = f"""Refine this plan based on feedback.

Current Plan:
{json.dumps(plan.data, indent=2)}

Feedback:
{feedback}

Provide refined plan in same JSON format."""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.2
        )

        data = json.loads(response.choices[0].message.content)

        return AgentResponse(
            agent=AgentRole.PLANNER,
            status="refined",
            data=data
        )


class CoderAgent:
    """Generates implementation code."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def generate(self, plan: AgentResponse, context: Dict[str, Any]) -> AgentResponse:
        """Generate code based on plan."""

        prompt = f"""You are an expert developer. Generate clean, production-ready code.

Plan:
{json.dumps(plan.data, indent=2)}

User's Tech Stack (from context):
{context.get('preferences', {}).get('tech_stack', 'Not specified')}

Generate code with:
1. Clear comments
2. Error handling
3. Type hints (if Python)
4. Best practices

Provide in JSON:
{{
    "language": "python|javascript|etc",
    "code": "full code",
    "explanation": "what the code does",
    "dependencies": ["dep1", "dep2"],
    "setup_instructions": "how to run"
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )

        data = json.loads(response.choices[0].message.content)

        return AgentResponse(
            agent=AgentRole.CODER,
            status="success",
            data=data
        )


class VerifierAgent:
    """Verifies if solution is sufficient (DS-STAR judge)."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def verify(
        self,
        code: AgentResponse,
        plan: AgentResponse,
        original_query: str
    ) -> AgentResponse:
        """Verify if code satisfies the plan and query."""

        prompt = f"""You are a verification expert. Verify if this solution is sufficient.

Original Query: {original_query}

Plan:
{json.dumps(plan.data, indent=2)}

Generated Code:
{json.dumps(code.data, indent=2)}

Verify and provide in JSON:
{{
    "is_sufficient": bool,
    "passes_criteria": {{
        "criterion1": bool,
        "criterion2": bool
    }},
    "issues_found": ["issue1", "issue2"],
    "feedback": "specific feedback for improvement",
    "confidence": 0.0-1.0
}}"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.1
        )

        data = json.loads(response.choices[0].message.content)

        return AgentResponse(
            agent=AgentRole.VERIFIER,
            status="verified",
            data=data,
            confidence=data.get("confidence", 0.8)
        )


class SynthesizerAgent:
    """Synthesizes final response in conversational tone."""

    def __init__(self, client: openai.AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def synthesize_streaming(
        self,
        query: str,
        context: Dict[str, Any],
        analysis: Optional[AgentResponse],
        plan: Optional[AgentResponse],
        code: Optional[AgentResponse]
    ) -> AsyncGenerator[str, None]:
        """Generate streaming conversational response."""

        # Build context for response
        response_context = {
            "query": query,
            "entries_analyzed": context.get("total_entries", 0),
            "insights": analysis.data if analysis else {},
            "plan": plan.data if plan else {},
            "code": code.data if code else {}
        }

        prompt = f"""You are JARVIS, an intelligent AI assistant. Provide a helpful, conversational response.

User asked: "{query}"

You analyzed:
- {response_context['entries_analyzed']} of their entries
- Found key insights: {response_context.get('insights', {}).get('key_insights', [])}
- Created a plan: {response_context.get('plan', {}).get('goal', 'N/A')}

Respond in a friendly, JARVIS-like tone:
1. Acknowledge what you found in their knowledge base
2. Provide clear, actionable insights
3. Reference specific entries/notes when relevant
4. Offer next steps
5. Be concise but thorough

Make it feel like talking to a smart friend who knows everything about their work."""

        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            temperature=0.7
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
