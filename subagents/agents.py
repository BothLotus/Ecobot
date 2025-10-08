from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
airqualityAgent = LlmAgent(
    name="airQuality",
    model="gemini-2.0-flash",
    description=(
        "Human-read description of agent's purpose"
    ),
    instruction=(
        """You're a positive AI subagent that focuses on providing air quality information and how the user can help to improve this aspect in their own home.
        After, transfer your response back to the coordinator agent."""
    ),
    tools=[],
    #output_key="airQuality"
    )

biodiversityAgent = LlmAgent(
    name="biodiversity",
    model="gemini-2.0-flash",
    description=(
        "Human-read description of agent's purpose"
    ),
    instruction=(
        """You're a positive AI subagent that focuses on providing biodiversity information and how the user can help to improve this aspect in their own home.
        After, transfer your response back to the coordinator agent."""
    ),
    tools=[],
    #output_key="biodiversity"
    )

soilQualityAgent = LlmAgent(
    name="soilQuality",
    model="gemini-2.0-flash",
    description=("Human-read description of agent's purpose"),
    instruction=(
        """You're a positive AI subagent that focuses on providing soil quality information and how the user can help to improve this aspect in their own home.
        After, transfer your response back to the coordinator agent."""
    ),
    tools=[],
    #output_key="soilQuality"
    )

# parallelAgent = ParallelAgent(
#     name="Parallel",
#     sub_agents=(airqualityAgent,biodiversityAgent,soilQualityAgent),
#     description=("Human-read description of agent's purpose")
#     )

# mergerAgent = LlmAgent(
#     name="mergerAgent",
#     model="gemini-2.0-flash",
#     description=(
#         "Human-read description of agent's purpose"
#     ),
#     instruction=(
#         """You're are a synthesis agent. You will be provided information from three subagents that each 
#         has a designated output_key (airQuality, biodiversity, soilQuality) and you are to summarize it 
#         into a small reading in which someone could get quick advice and tips"""
#     ),
#     tools=[],
#     #input_keys=["airQuality", "biodiversity", "soilQuality"],
#     output_key="finalsummary"
#     )