from root_agent.agent import root_agent
import os
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
import google.generativeai as genai

#genai.configure(api_key="AIzaSyCSD0EZ2CxBj87qA1zZjuiwN3Gp3jSFe6Y")
os.environ["GOOGLE_API_KEY"] = "Put Your Own API KEY here"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

#GOOGLE_GENAI_USE_VERTEXAI=FALSE


from google.genai import types

# GOOGLE_API_KEY='AIzaSyCSD0EZ2CxBj87qA1zZjuiwN3Gp3jSFe6Y'

session_service = InMemorySessionService()

APP_NAME = "EcoBotApp"
USER_ID = "user_1"
SESSION_ID = "session_001"

# session = await session_service.create_session(
#     app_name=APP_NAME,
#     user_id=USER_ID,
#     session_id=SESSION_ID
# )
# print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)
print(f"Runner created for agent '{runner.agent.name}'.")

async def call_agent_async(query: str, runner, user_id, session_id):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")

  # Prepare the user's message in ADK format
  content = types.Content(role='user', parts=[types.Part(text=query)])

  final_response_text = "Agent did not produce a final response." # Default

  # Key Concept: run_async executes the agent logic and yields Events.
  # We iterate through events to find the final answer.
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # You can uncomment the line below to see *all* events during execution
      # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

      # Key Concept: is_final_response() marks the concluding message for the turn.
      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")

async def run_conversation():
    session = await session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

    await call_agent_async("Tell me about air quality.",
                                       runner=runner,
                                       user_id=USER_ID,
                                       session_id=SESSION_ID)

    await call_agent_async("Tell me about biodiversity.",
                                       runner=runner,
                                       user_id=USER_ID,
                                       session_id=SESSION_ID) # Expecting the tool's error message

    await call_agent_async("Tell me about soil quality",
                                       runner=runner,
                                       user_id=USER_ID,
                                       session_id=SESSION_ID)

# Execute the conversation using await in an async context (like Colab/Jupyter)
# await run_conversation()

# --- OR ---

# Uncomment the following lines if running as a standard Python script (.py file):
import asyncio
if __name__ == "__main__":
    try:
        asyncio.run(run_conversation())
    except Exception as e:
        print(f"An error occurred: {e}")