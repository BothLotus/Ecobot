from google.adk.agents import SequentialAgent

from hostAgent.agent import root_agent as pra
from mergerAgent.agent import merger_agent as ma
sequential_pipeline_agent = SequentialAgent(
     name="ResearchAndSynthesisPipeline",
     # Run parallel research first, then merge
     sub_agents=[pra, ma],
     description="Coordinates parallel research and synthesizes the results."
 )