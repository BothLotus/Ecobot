from google.adk.agents import SequentialAgent
from hostAgent.agent import root_agent as ha
from mergerAgent.agent import merger_agent as ma

root_agent = SequentialAgent(
     name="ResearchAndSynthesisPipeline",
     # Run parallel research first, then merge
     sub_agents=[ha, ma],
     description="Coordinates parallel research and synthesizes the results.",
    #  instruction=(
    #     "First, call the host agent to gather results from all specialized agents "
    #     "(air quality, biodiversity loss, deforestation). "
    #     "Then pass all of these results into the merger agent. "
    #     "The merger agent must produce a single, coherent response that integrates "
    #     "and summarizes the information clearly and concisely for the user. "
    #     "The final answer should avoid repeating redundant details and instead weave "
    #     "the points together into a unified narrative."
    # )
 )