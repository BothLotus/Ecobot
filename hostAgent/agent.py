from google.adk.agents import ParallelAgent
from deforestation.agent import root_agent as df
from airQuality.agent import root_agent as aq
from bioDiversityLoss.agent import root_agent as bd

root_agent = ParallelAgent(
    name="hostAgent",
    sub_agents=[aq,bd,df],
    description=(
        "Description of agent's purpose"
    )
)

