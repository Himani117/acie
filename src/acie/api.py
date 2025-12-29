from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from acie.crew import Acie

app = FastAPI(title="ACIE API", description="Autonomous Competitive Intelligence Engine API")

class ResearchRequest(BaseModel):
    topic: str

@app.get("/greet")
async def greet():
    return {"message": "Hello, World!"}

@app.post("/research")
async def research(request: ResearchRequest):
    try:
        inputs = {
            'topic': request.topic,
            'current_year': str(datetime.now().year)
        }
        # Kickoff the crew
        result = Acie().crew().kickoff(inputs=inputs)
        return {"result": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}
