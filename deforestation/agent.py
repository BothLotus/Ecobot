from google.adk.agents import Agent
root_agent = Agent(
    name="deforestation",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Your an AI Agent that focuses on providing deforestation from verifiable sources. Do not answer questions on biodiversity loss or air quality."
    ),
    tools=[])