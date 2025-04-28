Rapidly Automating a Banking Process (AI + API)

This project automates a banking dispute process using Python FastAPI and simple AI-based decision logic.

## Features
- Accepts customer dispute input via API.
- Auto-classifies disputes into categories.
- Assigns priority based on customer status and dispute amount.
- Generates AI-powered recommended actions.
- Provides clean, extensible API endpoints.

## Project Structure
- `app/main.py`: API endpoints (FastAPI app).
- `app/models.py`: Pydantic models (input/output).
- `app/services.py`: Business logic (classification, priority, recommendations).

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
