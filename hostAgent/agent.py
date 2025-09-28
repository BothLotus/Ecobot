from google.adk.agents import ParallelAgent
from soilHealth.agent import root_agent as sh
from airQuality.agent import root_agent as aq
from bioDiversity.agent import root_agent as bd

root_agent = ParallelAgent(
    name="hostAgent",
    sub_agents=[aq,bd,sh],
    description=(
        "Description of agent's purpose"
    )
)

