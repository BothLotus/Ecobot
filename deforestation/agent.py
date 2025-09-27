from google.adk.agents import Agent
root_agent = Agent(
    name="deforestation",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "You're an AI Agent that focuses on providing deforestation and doesn't respond to any other requests."
    ),
    tools=[])