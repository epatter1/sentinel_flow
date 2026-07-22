async def analysis_agent(recon_output: dict):
    return {
        "step": "Analysis",
        "output": {
            "incidentType": "potential lateral movement",
            "severity": "high",
            "confidence": 0.85,
            "asset": recon_output["asset"],
            "user": recon_output["user"],
            "keyIndicators": recon_output["indicators"]
        },
        "reasoning": "Correlated indicators to classify incident.",
        "toolsUsed": ["correlation-engine"],
        "riskScore": 0.6
    }