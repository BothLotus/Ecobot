from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from google.adk.agents import SequentialAgent

from a2a.types import AgentSkill, AgentCard, AgentCapabilities
import uvicorn
from hostAgent.agent import root_agent as ha
from mergerAgent.agent import merger_agent as ma

from sequentialAgent.agent_executor import EcoResponseExecutor, EcoResponseAdapter

# --- Sequential pipeline ---
root_agent = SequentialAgent(
     name="ResearchAndSynthesisPipeline",
     sub_agents=[ha, ma],
     description="Coordinates parallel research and synthesizes the results.",
)

# --- Agent skill / card ---
skill = AgentSkill(
    id='eco_response',
    name='Returns json response of ecological query',
    description='When user makes an ecological query, it will be forwarded to our Gemini agents for response and sent back in JSON.',
    tags=['ecological response'],
    examples=['The fires of ', 'This region has been affected by deforestation'],
)
public_agent_card = AgentCard(
    name='Returns json response of ecological query',
    description='Forwards ecological queries to Gemini agents and returns JSON.',
    url='http://localhost:10001/',
    version='1.0.0',
    default_input_modes=['text'],
    default_output_modes=['text'],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
    supports_authenticated_extended_card=True,
)

# --- Executor adapter ---
adapter = EcoResponseAdapter(root_agent)  # Wrap SequentialAgent
executor = EcoResponseExecutor(adapter)  # Wrap adapter in executor

# --- Request handler & server ---
request_handler = DefaultRequestHandler(
    agent_executor=executor,
    task_store=InMemoryTaskStore(),
)
server = A2AStarletteApplication(
    agent_card=public_agent_card,
    http_handler=request_handler
)

# --- Run server ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        server.build(),   # your A2AStarletteApplication instance
        host="0.0.0.0",
        port=10001
    )