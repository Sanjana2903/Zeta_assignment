from pydantic import BaseModel

class TransactionRequest(BaseModel):
    user_id: str
    amount: float
