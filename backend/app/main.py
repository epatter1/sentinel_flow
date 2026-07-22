from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.recon import recon_agent
from app.agents.analysis import analysis_agent
from app.agents.hypothesis import hypothesis_agent
from app.agents.action import action_agent
from app.governance.evaluate import evaluate_governance

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Alert(BaseModel):
    text: str

@app.post("/run-pipeline")
async def run_pipeline(alert: Alert):
    timeline = []

    recon = await recon_agent(alert.text)
    timeline.append({**recon, "governance": evaluate_governance(recon)})

    analysis = await analysis_agent(recon["output"])
    timeline.append({**analysis, "governance": evaluate_governance(analysis)})

    hypothesis = await hypothesis_agent(analysis["output"])
    timeline.append({**hypothesis, "governance": evaluate_governance(hypothesis)})

    action = await action_agent(hypothesis["output"])
    timeline.append({**action, "governance": evaluate_governance(action)})

    return timeline