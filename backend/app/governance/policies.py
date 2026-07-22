def containment_requires_approval(action):
    return action["type"] == "containment" and action["environment"] == "prod"

def high_risk_sandbox(risk_score):
    return risk_score > 0.7