from google.adk.agents import Agent
root_agent = Agent(
    name="soilHealth",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "You're positive AI Agent that focuses on providing soil health information and how the user can help"
    ),
    tools=[],
    output_key="soilHealth")