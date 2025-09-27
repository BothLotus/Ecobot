from google.adk.agents import Agent
root_agent = Agent(
    name="bioDiversityLoss",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "You're an AI Agent that focuses on providing biodiversity loss information on what the user requests"
    ),
    output_key="bioDiversityLoss")