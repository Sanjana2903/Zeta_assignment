from fastapi import FastAPI, HTTPException
from app.models import TransactionRequest
from app.db import get_connection
from datetime import datetime

app = FastAPI()

@app.get("/balance/{user_id}")
def get_balance(user_id: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id,))
            row = cur.fetchone()
            if row:
                return {"user_id": user_id, "balance": row[0]}
            raise HTTPException(status_code=404, detail="User not found")

@app.post("/credit")
def credit(req: TransactionRequest):
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("BEGIN")
            cur.execute("INSERT INTO accounts (user_id, balance) VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE SET balance = accounts.balance + %s",
                        (req.user_id, req.amount, req.amount))
            cur.execute("INSERT INTO transactions (user_id, amount, type) VALUES (%s, %s, 'credit')",
                        (req.user_id, req.amount))
            cur.execute("COMMIT")
    return {"message": "Credit successful"}

@app.post("/debit")
def debit(req: TransactionRequest):
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("BEGIN")
            cur.execute("SELECT balance FROM accounts WHERE user_id = %s FOR UPDATE", (req.user_id,))
            row = cur.fetchone()
            if not row:
                cur.execute("ROLLBACK")
                raise HTTPException(status_code=404, detail="Account not found")
            if row[0] < req.amount:
                cur.execute("ROLLBACK")
                raise HTTPException(status_code=400, detail="Insufficient funds")
            new_balance = row[0] - req.amount
            cur.execute("UPDATE accounts SET balance = %s, last_updated = %s WHERE user_id = %s",
                        (new_balance, datetime.utcnow(), req.user_id))
            cur.execute("INSERT INTO transactions (user_id, amount, type) VALUES (%s, %s, 'debit')",
                        (req.user_id, req.amount))
            cur.execute("COMMIT")
    return {"message": "Debit successful"}
