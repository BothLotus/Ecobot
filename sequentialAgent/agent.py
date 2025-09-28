from google.adk.agents import SequentialAgent
from hostAgent.agent import root_agent as ha
from mergerAgent.agent import merger_agent as ma

root_agent = SequentialAgent(
     name="ResearchAndSynthesisPipeline",
     # Run parallel research first, then merge
     sub_agents=[ha, ma],
     description="Coordinates parallel research and synthesizes the results.",

 )