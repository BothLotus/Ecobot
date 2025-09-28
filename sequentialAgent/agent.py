from google.adk.agents import SequentialAgent

from hostAgent.agent import root_agent as ha
from mergerAgent.agent import merger_agent as ma

root_agent = SequentialAgent(
     name="SynthesisAgent",
     sub_agents=[ha,ma],
     description="Combines research findings from parallel agents into a structured, cited report, strictly grounded on provided inputs."
     )