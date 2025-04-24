from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# --------- MODELS ---------
class LoanRequest(BaseModel):
    name: str
    age: int
    annual_income: float
    credit_score: int

class Dispute(BaseModel):
    id: int
    title: str
    description: str
    status: str  
    raised_on: str

class UserBalance(BaseModel):
    username: str
    balance: float

# --------- MOCK DATA ---------
balances = {
    "john": 15720.75,
    "alice": 4899.00,
    "sanjana": 12500.00,
}

disputes = {
    "john": [
        Dispute(id=1, title="Incorrect Charge", description="Charged twice for Netflix", status="Resolved", raised_on="2024-10-02"),
        Dispute(id=2, title="ATM Error", description="Cash not dispensed", status="Pending", raised_on="2024-11-20")
    ],
    "sanjana": [
        Dispute(id=3, title="Loan EMI extra debit", description="Extra EMI debited", status="Resolved", raised_on="2025-01-15")
    ]
}

# --------- ROUTES ---------
@app.post("/loan-eligibility/")
def check_eligibility(data: LoanRequest):
    score = 0
    if data.annual_income > 50000:
        score += 40
    if data.credit_score > 700:
        score += 40
    if 21 <= data.age <= 60:
        score += 20

    if score >= 80:
        recommendation = "Highly Eligible"
    elif score >= 60:
        recommendation = "Eligible"
    else:
        recommendation = "Not Eligible"

    return {
        "name": data.name,
        "score": score,
        "recommendation": recommendation
    }

@app.get("/balance/{username}")
def get_balance(username: str):
    balance = balances.get(username.lower())
    if balance is None:
        return {"error": "User not found"}
    return {"username": username, "balance": balance}

@app.get("/disputes/{username}", response_model=List[Dispute])
def get_disputes(username: str):
    return disputes.get(username.lower(), [])
