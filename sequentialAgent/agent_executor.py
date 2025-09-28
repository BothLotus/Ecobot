from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from a2a.server.agent_execution import AgentExecutor, RequestContext

class EcoResponseAdapter:
    def __init__(self, agent):
        self.agent = agent  # SequentialAgent

    async def invoke(self, user_query: str) -> str:
        # This is pseudocode; adjust based on SequentialAgent API
        # SequentialAgent might need input dict or messages
        result = await self.agent.run(inputs={'user_query': user_query})
        return result
    
class EcoResponseExecutor(AgentExecutor):
    def __init__(self, agent):
        self.agent = agent  # instance of EcoResponseAdapter

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        user_query = context.message.text
        result = await self.agent.invoke(user_query)
        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, event_queue: EventQueue):
        raise Exception('cancel not supported')