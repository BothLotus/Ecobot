from google.adk.agents import Agent
root_agent = Agent(
    name="airQuality",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Your an AI Agent that focuses on providing air quality information and doesn't respond to any other requests"
    ),
    tools=[])