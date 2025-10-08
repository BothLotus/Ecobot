from google.adk.agents import LlmAgent
from subagents.agents import airqualityAgent as aq, biodiversityAgent as bd, soilQualityAgent as sq
root_agent = LlmAgent(
    name="CoordinatorAgent",
    model="gemini-2.0-flash",
    sub_agents=[aq, bd, sq],
    description=("Combines research findings from parallel agents into a structured report"),
    instruction=("""You are a coordinator agent that is capable of taking the user's request and tranferring it to one of your subagents if necessary. 
    According to their question, you will call one of your subagents to answer the question."""),    
)