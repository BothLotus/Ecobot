# sequentialAgent/agent_executor.py
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from a2a.server.agent_execution import AgentExecutor, RequestContext

class EcoResponseAdapter:
    """Adapter to wrap SequentialAgent for A2A execution."""
    def __init__(self, agent):
        self.agent = agent

    async def invoke(self, user_query: str) -> str:
        # SequentialAgent API expects dict inputs
        result = await self.agent.run(inputs={"user_query": user_query})
        return result

class EcoResponseExecutor(AgentExecutor):
    """A2A Executor for SequentialAgent that returns JSON text."""
    def __init__(self, agent_adapter: EcoResponseAdapter):
        self.agent = agent_adapter

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        user_query = context.message.text  # text from incoming request
        result = await self.agent.invoke(user_query)
        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, event_queue: EventQueue):
        raise Exception("cancel not supported")
        