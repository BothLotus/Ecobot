from google.adk.agents import Agent
root_agent = Agent(
    name="airQuality",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Your an AI Agent that focuses on providing Air quality from verifiable sources. Do not answer questions on biodiversity loss or deforestation."
    ),
    tools=[])