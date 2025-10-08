import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyCSD0EZ2CxBj87qA1zZjuiwN3Gp3jSFe6Y" #This is Danny API KEY >:(
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uvicorn

################### Important for our demo of non-A2A ###################

from root_agent.agent import root_agent as coordinator_agent #importing the coordinator agent from our root_agent folder
from google.adk.sessions import InMemorySessionService #necessary for agent to respond to query
from google.adk.runners import Runner #necessary for agent to respond to query

from google.genai import types #for establishing query formation (contents of message and whatev)

#Context for interaction content
APP_NAME="EcoBot"
USER_ID="user_1" # Just a demo user id
SESSION_ID= "session_001" #Just a demo session_id


session_service = InMemorySessionService()

runner = Runner(
    agent=coordinator_agent, # The agent we want to run
    app_name=APP_NAME,   # Associates runs with our app
    session_service=session_service # Uses our session manager
)

print(f"Runner created for agent '{runner.agent.name}'.")

async def queries(query:str, runner, user_id, session_id ):
    content= types.Content(role='user',parts=[types.Part(text=query)])
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")
    return (f"{final_response_text}")

################### Important for our demo of non-A2A ###################

app = FastAPI()

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/frontend", StaticFiles(directory="frontend/", html=True), name="frontend")

@app.on_event("startup")
async def startup():
    global session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")
    print("Sessions available:", session_service.sessions)

#from google.adk.agents import AgentInput
@app.post("/")
async def AgentSpeak(request: Request):
    data = await request.json()
    print("Received data:", data) #log statement
    query = data.get("query")
    print("Our Query is:", query) #log statement
    if not query:
        return {"response": "(no query provided)"}
    final_response_text = await queries(query, runner, USER_ID, SESSION_ID)  # ← direct call to the agent logic
    return {"response": final_response_text}

if __name__ == "__main__":
    uvicorn.run("webserver:app", host="0.0.0.0", port=80, reload=True)

    
    