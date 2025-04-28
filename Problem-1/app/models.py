from pydantic import BaseModel

class Dispute(BaseModel):
    customer_id: str
    transaction_id: str
    dispute_reason: str
    amount: float
    date: str

class DisputeResponse(BaseModel):
    category: str
    priority: str
    recommendation: str
