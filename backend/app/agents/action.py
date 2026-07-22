async def action_agent(hypothesis_output: dict):
    primary = next(
        h for h in hypothesis_output["hypotheses"]
        if h["id"] == hypothesis_output["primaryHypothesisId"]
    )

    return {
        "step": "Action",
        "output": {
            "type": "containment",
            "environment": "prod",
            "steps": [
                "Disable svc-backup account",
                "Block server-42 lateral movement",
                "Rotate credentials"
            ],
            "justification": primary["description"]
        },
        "reasoning": "Proposed containment plan.",
        "toolsUsed": ["edr-api", "identity-service"],
        "riskScore": 0.85
    }