from fastapi import FastAPI
from app.models import Dispute, DisputeResponse
from app.services import classify_dispute, assign_priority, generate_recommendation

app = FastAPI(
    title="Banking Dispute Automation API",
    description="An API to automate banking transaction disputes using simple AI-based logic.",
    version="1.0.0"
)

@app.post("/submit_dispute", response_model=DisputeResponse)
def submit_dispute(dispute: Dispute):
    category = classify_dispute(dispute.dispute_reason)
    priority = assign_priority(dispute.customer_id, dispute.amount, category)
    recommendation = generate_recommendation(category, dispute.amount)

    return DisputeResponse(
        category=category,
        priority=priority,
        recommendation=recommendation
    )
