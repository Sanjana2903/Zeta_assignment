def classify_dispute(reason: str) -> str:
    keywords = {
        "fraud": "Fraud",
        "duplicate": "Duplicate Charge",
        "service": "Service Not Rendered",
        "billing": "Billing Error"
    }
    for keyword, category in keywords.items():
        if keyword in reason.lower():
            return category
    return "Other"

def assign_priority(customer_id: str, amount: float, category: str) -> str:
    if customer_id.startswith('VIP') or amount > 1000 or category == "Fraud":
        return "High"
    return "Normal"

def generate_recommendation(category: str, amount: float) -> str:
    if category == "Fraud":
        return "Escalate to Fraud Investigation"
    if amount < 50:
        return "Refund Immediately"
    return "Request Additional Documentation"
