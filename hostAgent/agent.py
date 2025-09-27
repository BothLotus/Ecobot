from google.adk.agents import ParallelAgent
from deforestation.agent import root_agent as df
from airQuality.agent import root_agent as aq
from bioDiversityLoss.agent import root_agent as bd

root_agent = ParallelAgent(
    name="hostAgent",

    sub_agents=[aq,bd,df],

    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Your a host agent that calls on sub agents to answer questions regarding air quality, biodiversity loss, and deforestation."
    ),
    tools=[])