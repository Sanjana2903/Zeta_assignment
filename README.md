# Zeta_assignment
# Problem -1:
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

# Future Roadmap
To continue improving this project:
- Replace keyword matching with fine-tuned AI models (OpenAI, Huggingface Transformers).
- Connect disputes to a PostgreSQL database for historical tracking and analysis.
- Add user authentication (OAuth, JWT) to secure endpoints.
- Introduce retry logic and failover mechanisms for robustness.
-Containerize the app using Docker for easy cloud deployment.
---
# Final Thoughts
- I built this project carefully to mimic a real-world backend that:
- Starts simple,
- Follows professional standards,
- Leaves room to plug in stronger AI and analytics later.

---
# Problem 2 - Zeta Assignment

---

## Overview

This project is part of the Zeta assignment and focuses on building a basic API-based application.  
The application consists of two main components:
- `app.py`: Core application logic
- `api.py`: API endpoints built using FastAPI

It demonstrates how to structure a simple Python project involving APIs and modular application logic.

---

## Project Structure

- **`app.py`**:  
  Houses the main functions or services that perform core business operations.

- **`api.py`**:  
  Connects the external world to the internal logic via FastAPI routes. Acts as the interface between the client and server.

- **`requirements.txt`**:  
  Lists all necessary Python libraries required to run the project.

---
When designing this project, I focused on maintaining clean separation of concerns:

Instead of mixing business logic and API routes into a single file, I separated them:
- app.py deals only with application logic (calculation, processing, etc.).
- api.py handles request parsing, response generation, and connects user requests to the core logic.

This separation ensures that:

- The project is easy to maintain.
- Logic can evolve independently without affecting API structure.
- Future testing (unit testing for app.py) becomes much easier.
- New routes or logic can be added without messy refactoring.

Additionally, using FastAPI gives the project:

- Automatic documentation through Swagger UI (/docs).
- Pydantic data validation support.
- Asynchronous capabilities if needed in future enhancements.

## Future Improvements

- Add unit tests for the core logic in app.py using pytest.
- Implement input validation using Pydantic models.
- Expand the project to support database integration.

---
# Problem 3 - Zeta Assignment

---

## Overview

This project demonstrates a basic full-stack setup where a Python application interacts with a PostgreSQL database through SQL queries, and provides a simple user interface (UI) for interaction.  
It is part of the Zeta assignment aimed at showcasing backend, database, and containerization skills.

The project covers:
- Database setup using PostgreSQL
- Backend application built with Python
- Docker and Docker Compose for containerization
- Clean separation between logic (`db.py`, `models.py`), API endpoints (`main.py`), and user interface (`ui.py`)


---

## How It Works

1. **Database Setup** (`queries.sql`, `db.py`)
   - A PostgreSQL database is used to store and retrieve information.
   - `queries.sql` defines the database schema and tables.
   - `db.py` manages database connection and query execution.

2. **Backend Service** (`main.py`)
   - Built using FastAPI.
   - Exposes REST API endpoints to perform CRUD operations on the database.

3. **Frontend User Interface** (`ui.py`)
   - Built using Streamlit.
   - Provides a simple web interface for users to interact with the system without directly using APIs.

4. **Containerization** (`Dockerfile`, `docker-compose.yml`)
   - `Dockerfile` sets up the backend service.
   - `docker-compose.yml` orchestrates running both the PostgreSQL database and the FastAPI backend together.

---

Start services using Docker Compose:
`docker-compose up --build`
This will:
- Start the PostgreSQL database container
- Build and run the FastAPI backend

Access the API Documentation: After the backend is running, open:
`http://localhost:8000/docs`
Access the UI: To launch the Streamlit UI separately:
`streamlit run ui.py`
Then visit:
`http://localhost:8501/`
When designing this project, I made sure to separate concerns cleanly:


| **Component** | **Purpose** |
|:--------------|:------------|
| `db.py`       | Manages the direct communication with the PostgreSQL database (connection, queries). |
| `models.py`   | Defines strict Pydantic data models ensuring input/output consistency and validation. |
| `main.py`     | Bridges external API requests to internal database operations (via FastAPI routes). |
| `ui.py`       | Simplifies user interaction through a frontend web application built with Streamlit. |

## Future Improvements:

- Implement authentication and authorization (OAuth/JWT).
- Add error handling and input validations.
- Expand UI for better UX (update/delete operations, better forms).
- Add unit tests for backend API endpoints.
- Dockerize the Streamlit UI as well into the same Compose setup.
  
##Conclusion:

- This project simulates a real-world full-stack setup where the backend, database, and user-facing interface work together.
- It is structured to allow easy extension, scalability, and maintainability for future enhancements.

# Problem 4 - Zeta Assignment

---

## Overview

This project implements two types of **rate limiting algorithms**:

- **Sliding Window Log** (`rate_limiter.py`)
- **Token Bucket Algorithm** (`token_bucket_limiter.py`)

Both algorithms aim to **control the rate** at which actions (like API requests) are allowed, protecting systems from being overwhelmed by high traffic.

The code demonstrates:
- How different rate limiting strategies work.
- The trade-offs between precision, memory efficiency, and scalability.

---
## 🔁 Trade-Offs: Sliding Window vs Token Bucket

| Feature              | Sliding Window Log               | Token Bucket                            |
|----------------------|----------------------------------|------------------------------------------|
| Precision            | High (tracks exact timestamps)   | Approximate (token-based)               |
| Memory Efficiency    | Lower (stores timestamps)        | Higher (stores only token count & time) |
| Burst Handling       | Harsh cut-off                    | Smooth burst tolerance                  |
| Scalability          | Less scalable at high traffic    | More scalable for large user base       |
| Implementation Ease  | Simple and intuitive             | Slightly more complex (timing logic)    |

---

## 🧪 Run Both

python rate_limiter.py         # Sliding Window


python token_bucket_limiter.py # Token Bucket

Thought Process and Design

When solving this problem, I wanted to showcase both:

- A simple, precise way to rate limit using a sliding window of request timestamps.
- A more scalable and efficient way using a token-based system.


Sliding Window Log:

- Great when precision matters (like preventing exactly 100 logins per minute).
- But memory grows linearly with traffic (because it stores every timestamp).


Token Bucket:

- Allows more flexible handling of bursts.
- Memory is constant regardless of traffic (just tokens and refill logic).
- Used in real-world systems like Google Cloud APIs, AWS throttling, etc.


Thus, both were implemented to compare ease, efficiency, and scalability.

## Conclusion

This project provides a hands-on demonstration of two popular rate limiting techniques.
Understanding their behavior, trade-offs, and design patterns is crucial for building resilient, scalable backend systems.





