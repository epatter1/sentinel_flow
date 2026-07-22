async def recon_agent(alert_text: str):
    return {
        "step": "Recon",
        "output": {
            "alertText": alert_text,
            "asset": "server-42",
            "user": "svc-backup",
            "indicators": [
                "multiple failed logins",
                "privilege escalation attempt",
                "suspicious backup job"
            ]
        },
        "reasoning": "Enriched alert with asset + user context.",
        "toolsUsed": ["asset-db", "user-directory"],
        "riskScore": 0.3
    }