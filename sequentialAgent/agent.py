# sequentialAgent/agent.py
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from google.adk.agents import SequentialAgent

from a2a.types import AgentSkill, AgentCard, AgentCapabilities
import uvicorn

from hostAgent.agent import root_agent as ha
from mergerAgent.agent import merger_agent as ma
from sequentialAgent.agent_executor import EcoResponseAdapter, EcoResponseExecutor

# Sequential agent pipeline
root_agent = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    sub_agents=[ha, ma],
    description="Coordinates parallel research and synthesizes the results.",
)

# Adapter wraps SequentialAgent for executor
agent_adapter = EcoResponseAdapter(root_agent)

# Define a skill and public agent card
skill = AgentSkill(
    id="eco_response",
    name="Returns JSON response of ecological query",
    description="Responds to ecological queries with JSON output.",
    tags=["ecological response"],
    examples=["The fires of ", "This region has been affected by deforestation"],
)

public_agent_card = AgentCard(
    name="Eco JSON Response Agent",
    description="Forward queries to SequentialAgent and respond with JSON",
    url="http://localhost:10001/",
    version="1.0.0",
    default_input_modes=["text"],
    default_output_modes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
    supports_authenticated_extended_card=True,
)

# Default request handler
request_handler = DefaultRequestHandler(
    agent_executor=EcoResponseExecutor(agent_adapter),
    task_store=InMemoryTaskStore(),
)

# Build server
server = A2AStarletteApplication(
    agent_card=public_agent_card,
    http_handler=request_handler
)

if __name__ == "__main__":
    # Pass import path as string to enable reload
    uvicorn.run("sequentialAgent.agent:server", host="0.0.0.0", port=10001, reload=True)
