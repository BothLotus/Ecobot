from google.adk.agents import LlmAgent
root_agent = LlmAgent(
    name="airQuality",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "You're a positive AI Agent that focuses on providing air quality information and how the user can help"
    ),
    tools=[],
    output_key="airQuality")