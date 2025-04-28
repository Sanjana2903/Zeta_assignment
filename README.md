# Zeta_assignment
#Problem -1:
# Banking Dispute Automation (AI + API)

---

## Overview

This project aims to automate the manual review process for banking transaction disputes by building a lightweight, extensible API with simple AI-based decision-making. 

It simulates how a real-world bank would handle hundreds of daily disputes efficiently by:
- Collecting customer dispute inputs.
- Auto-classifying the type of dispute.
- Assigning a priority level based on customer importance and dispute risk.
- Recommending an action for the support team to take.

The project is designed using **FastAPI**, following clean architecture principles for easy scaling and extension in the future.

---

## Why This Solution?

When I approached this problem, I broke it down into core needs:
- The bank needs to handle **high volume** efficiently → Solution must be lightweight and fast.
- **Categorizing** disputes manually wastes time → Build an AI classifier (even a simple keyword-based one to start).
- Some customers/disputes are more **urgent** than others → Add **priority assignment** logic.
- **Actionable insights** are needed to reduce back-and-forth between teams → Generate a recommended action.
- Code must be **modular** so business logic can evolve separately from API endpoints.

Thus, I designed the system in a **modular, extensible, clean** manner that is simple but production-ready.

---

## Workflow: How It Works

Here’s the end-to-end flow:

1. **Customer Dispute Submission**
   - Customer fills out a basic form (could be on a website or mobile app).
   - Form collects fields like: `customer_id`, `transaction_id`, `reason`, `amount`, `date`.

2. **API Receives Input**
   - FastAPI handles a `POST` request to `/submit_dispute`.
   - Payload is validated using Pydantic models.

3. **Dispute Classification**
   - The system analyzes the `dispute_reason` text.
   - Based on simple keyword matching, it assigns one of the following categories:
     - Fraud
     - Duplicate Charge
     - Billing Error
     - Service Not Rendered
     - Other

4. **Priority Assignment**
   - Priority is assigned based on:
     - If the customer is "VIP" (IDs starting with `VIP`),
     - If the dispute amount is greater than $1000,
     - If the category is “Fraud.”
   - If any of these are true → Priority = "High"; otherwise, "Normal".

5. **AI-Generated Recommendation**
   - Based on category and amount:
     - For Fraud → Escalate to Fraud Investigation
     - For small amounts (<$50) → Refund Immediately
     - Otherwise → Request Additional Documentation

6. **Response**
   - API returns a structured JSON response containing:
     - `category`
     - `priority`
     - `recommendation`

7. **Next Steps (Future Enhancements)**
   - Can route the dispute automatically to the correct support queue.
   - Can integrate notification systems (Slack, email).
   - Can expand the classification system using a real NLP model like BERT.

---

#Future Roadmap
To continue improving this project:
- Replace keyword matching with fine-tuned AI models (OpenAI, Huggingface Transformers).
- Connect disputes to a PostgreSQL database for historical tracking and analysis.
- Add user authentication (OAuth, JWT) to secure endpoints.
- Introduce retry logic and failover mechanisms for robustness.
-Containerize the app using Docker for easy cloud deployment.
#Final Thoughts
I built this project carefully to mimic a real-world backend that:
- Starts simple,
- Follows professional standards,
- Leaves room to plug in stronger AI and analytics later.


