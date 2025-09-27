from google.adk.agents import LlmAgent
root_agent = LlmAgent(
    name="airQuality",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Your an AI Agent that focuses on providing air quality information on what the user requests"
    ),
    tools=[],
    output_key="airQuality")