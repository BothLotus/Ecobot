from google.adk.agents import Agent
root_agent = Agent(
    name="bioDiversity",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "You're a positive AI Agent that focuses on providing biodiversity information and how the user can help"
    ),
    output_key="bioDiversity")