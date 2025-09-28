from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution import *
from a2a.server.events import *
from a2a.utils import *
from sequentialAgent.agent import root_agent
from google.adk.agents import InvocationContext
from google.adk.sessions import Session, in_memory_session_service
from google.adk.memory import InMemoryMemoryService
import uuid


class sequentialAgent:

                #invoke(self, query: str) -> str:
    # async def invoke(self, query: str):
    #     context = InvocationContext(agent=root_agent, input=query)
    #     async for event in root_agent.run_async(context):
    #         yield event
    async def invoke(self, query: str):
        session_service = in_memory_session_service()
        session = Session(id=str(uuid.uuid4()), input=query)
        context = InvocationContext(
            agent=root_agent,
            session_service=session_service,
            session=session,
            invocation_id=str(uuid.uuid4())
        )
        async for event in root_agent.run_async(context):
            yield event


        
class sequentialAgentExecutor(AgentExecutor):

    def __init__(self):
        self.agent = sequentialAgent()

    async def execute(
            self,
            context:RequestContext,
            event_queue:EventQueue,
    )   ->  None:
            query = getattr(context, "query", None)
            if not query:
                query = "(no query provided)"
            invocation_context = InvocationContext(agent=root_agent, input=query)
            # result_texts = []
            # async for event in root_agent.run_async(invocation_context):
            #     if hasattr(event, "text"):
            #         result_texts.append(event.text)

            # await event_queue.enqueue_event(new_agent_text_message("\n".join(result_texts)))
            session_service = in_memory_session_service()
            session = Session(id=str(uuid.uuid4()), input=query)
            invocation_context = InvocationContext(
                agent=root_agent,
                session_service=session_service,
                session=session,
                invocation_id=str(uuid.uuid4())
            )

            result_texts = []
            async for event in root_agent.run_async(invocation_context):
                if hasattr(event, "text"):
                    result_texts.append(event.text)

            await event_queue.enqueue_event(new_agent_text_message("\n".join(result_texts)))


    async def cancel(
            self, context: RequestContext, event_queue: EventQueue
        ) -> None:
            raise Exception('cancel not supported')