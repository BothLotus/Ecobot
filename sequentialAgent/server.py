from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from .agent import root_agent  # SequentialAgent

app = FastAPI()

# Allow frontend (HTML/JS) to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper to invoke the agent
async def get_agent_response(query: str) -> str:
    # SequentialAgent.invoke is async
    response = await root_agent.invoke(query)
    return response


# Compute absolute path to frontend folder
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")

# Check if folder exists
if not os.path.isdir(frontend_path):
    raise RuntimeError(f"Frontend folder does not exist at {frontend_path}")

app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

# FastAPI endpoint
@app.get("/synthesis")
async def synthesis(query: str):
    """
    Example request:
    http://localhost:8000/synthesis?query=Tell me about air quality
    """
    result = await get_agent_response(query)
    return {"response": result}


if __name__ == "__main__":
    uvicorn.run("sequentialAgent.server:app", host="0.0.0.0", port=440, reload=True)
