from google.adk.agents import SequentialAgent
from hostAgent.agent import root_agent as ha
from mergerAgent.agent import merger_agent as ma

from google.adk.a2a.executor.a2a_agent_executor import AgentExecutor

def make_ha():
    # If ParallelAgent supports cloning:
    return ha.clone()
    # OR, if not, recreate a fresh ParallelAgent instance

def make_ma():
    # If LlmAgent supports cloning:
    return ma.clone()
    # OR, rebuild a new LlmAgent instance

root_agent = SequentialAgent(
    name="SynthesisAgent",
    sub_agents=[make_ha(), make_ma()],
    description="Combines research findings from parallel agents into a structured, cited report."
)
#