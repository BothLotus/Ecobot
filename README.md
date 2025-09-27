# ShellHacks2025
Project for Shellhacks 2025

For each agent other than host_agent copy the following with relevant changes according to agent:
root_agent = ParallelAgent(
    name="name of agent",
    model="gemini-2.0-flash",
    description=(
        "Description of agent's purpose"
    ),
    instruction=(
        "Prompt that explains purpose of ai example: you are agent that does do and doesnt do this."
    ),
    tools=[],