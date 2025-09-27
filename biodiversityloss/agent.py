from google.adk.agents import Agent
root_agent = Agent(
    name="bioDiversityLoss",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Your an AI Agent that focuses on providing biodiversity loss from verifiable sources. Do not answer questions on air quality or deforestation."
    ),
    tools=[])