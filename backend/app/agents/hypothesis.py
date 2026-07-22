async def hypothesis_agent(analysis_output: dict):
    hypotheses = [
        {
            "id": "H1",
            "description": "Service account compromise likely.",
            "evidence": analysis_output["keyIndicators"]
        },
        {
            "id": "H2",
            "description": "Backup job misconfiguration.",
            "evidence": ["backup anomalies"]
        }
    ]

    return {
        "step": "Hypothesis",
        "output": {
            "hypotheses": hypotheses,
            "primaryHypothesisId": "H1",
            "impactedScope": ["server-42", "backup subsystem"]
        },
        "reasoning": "Generated hypotheses and selected most likely.",
        "toolsUsed": ["incident-graph-builder"],
        "riskScore": 0.7
    }