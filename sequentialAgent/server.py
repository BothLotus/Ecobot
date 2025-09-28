from google import *
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uvicorn

from sequentialAgent.agent import root_agent  # Your SequentialAgent

#from google.adk.a2a.executor.a2a_agent_executor import AgentExecutor
#executor = AgentExecutor(root_agent)
#from sequentialAgent.agent import agent_executor

from sequentialAgent.agent_executor import sequentialAgent, sequentialAgentExecutor



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
app.mount("/frontend", StaticFiles(directory="sequentialAgent/frontend", html=True), name="frontend")

#from google.adk.agents import AgentInput
@app.post("/synthesis")
async def synthesis(request: Request):
    data = await request.json()
    query = data.get("query")
    if not query:
        return {"response": "(no query provided)"}
    agent = sequentialAgent()
    result_gen = agent.invoke(query)
    result = []
    async for item in result_gen:
        result.append(item)

    return {"response": result}


if __name__ == "__main__":
    uvicorn.run("sequentialAgent.server:app", host="0.0.0.0", port=440, reload=True)

