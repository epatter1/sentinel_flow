from .policies import containment_requires_approval, high_risk_sandbox

def evaluate_governance(step_output):
    decisions = []

    if high_risk_sandbox(step_output["riskScore"]):
        decisions.append({"type": "sandbox", "mode": "dry-run"})

    if step_output["step"] == "Action":
        if containment_requires_approval(step_output["output"]):
            decisions.append({"type": "approval-required"})

    return decisions