---

# Phase 1 — Backend Foundations

# Chapter 1 — Backend Project Setup

> Version: 1.0
>
> Status: Completed
>
> Phase: 1 — Backend Foundations
>
> Chapter: 1 — Backend Project Setup

---

# Objective

The objective of this chapter is to prepare the backend development environment for the AI Research & Knowledge Assistant.

By the end of this chapter, we will have:

* Backend project created
* Python virtual environment configured
* All required dependencies installed
* Initial folder structure created
* FastAPI application running successfully
* Development server configured
* Backend verified and ready for implementation

No business logic will be written in this chapter. We are only preparing the foundation that every future feature will build upon.

---

# Prerequisites

Before starting, ensure the following software is already installed (covered in Phase 0):

* Python 3.12+
* Node.js LTS
* Git
* Docker Desktop
* VS Code or Antigravity IDE

Verify installations:

```bash
python --version
```

```bash
node --version
```

```bash
git --version
```

```bash
docker --version
```

Each command should return a valid version.

---

# Expected Outcome

After completing this chapter, the backend should:

* Start without errors.
* Expose the FastAPI application.
* Display Swagger documentation.
* Automatically reload after code changes.
* Be ready for authentication, database integration, and AI features.

---

# Step 1 — Project Structure

Create the project root.

```text
AI-Research-Knowledge-Assistant/
```

Inside it:

```text
AI-Research-Knowledge-Assistant/

frontend/

backend/

docs/

docker/

scripts/

README.md

docker-compose.yml

.env.example

.gitignore
```

At this stage we will only work inside:

```text
backend/
```

The frontend will be implemented later.

---

# Step 2 — Create Backend Directory

Navigate to the project root.

```bash
cd AI-Research-Knowledge-Assistant
```

Create backend folder if it doesn't already exist.

```bash
mkdir backend
```

Enter backend.

```bash
cd backend
```

Everything in this phase will be developed inside this directory.

---

# Step 3 — Create Virtual Environment

Create the virtual environment.

```bash
python -m venv venv
```

This creates:

```text
backend/

venv/
```

### Why We Use a Virtual Environment

Our project depends on many Python packages.

Examples:

* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* Uvicorn
* python-jose
* passlib
* google-generativeai (or Gemini SDK)
* psycopg

Installing them globally would:

* Mix dependencies across projects.
* Cause version conflicts.
* Make the project difficult to reproduce.

Using `venv` isolates our project's dependencies.

**Rule:** Every Python command in this project should run with the virtual environment activated.

---

# Step 4 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

After activation, your terminal should display:

```text
(venv)
```

This indicates that Python and pip now point to the isolated environment.

Verify:

```bash
python --version
```

```bash
pip --version
```

Both should reference the virtual environment.

---

# Step 5 — Install Dependencies

Install the core packages.

```bash
pip install \
fastapi \
uvicorn[standard] \
sqlalchemy \
alembic \
psycopg[binary] \
pydantic \
pydantic-settings \
python-jose[cryptography] \
passlib[bcrypt] \
python-multipart \
httpx \
python-dotenv \
structlog
```

> **Note:** Package names may evolve over time. Always pin versions before production (covered later). During initial development, installing compatible latest versions is acceptable.

---

# Why Each Dependency Exists in Our Project

| Package           | Purpose in Our Project                                                             |
| ----------------- | ---------------------------------------------------------------------------------- |
| fastapi           | Core backend framework that exposes our REST API.                                  |
| uvicorn           | ASGI server used to run the FastAPI application during development and production. |
| sqlalchemy        | ORM used by the Repository Layer to communicate with PostgreSQL.                   |
| alembic           | Tracks and applies database schema migrations.                                     |
| psycopg           | PostgreSQL database driver used by SQLAlchemy.                                     |
| pydantic          | Validates all request and response data.                                           |
| pydantic-settings | Loads application configuration from environment variables.                        |
| python-jose       | Creates and verifies JWT access tokens.                                            |
| passlib           | Hashes and verifies user passwords securely.                                       |
| python-multipart  | Handles form data (useful for authentication and future file uploads).             |
| httpx             | Makes HTTP requests to AI providers such as Gemini or OpenRouter.                  |
| python-dotenv     | Loads values from `.env` during local development.                                 |
| structlog         | Provides structured, production-friendly logging.                                  |

Every dependency listed above will be used later in the project. Avoid installing packages that are not required.

---

# Step 6 — Save Dependencies

Generate the dependency file.

```bash
pip freeze > requirements.txt
```

Project now contains:

```text
backend/

requirements.txt
```

This file allows any developer to recreate the exact backend environment.

Install later using:

```bash
pip install -r requirements.txt
```

**Rule:** Whenever a new dependency is added, update `requirements.txt`.

---

# Step 7 — Create Initial Backend Structure

Create the following folders.

```text
backend/

app/

api/

core/

db/

dependencies/

exceptions/

middleware/

models/

providers/

repositories/

schemas/

services/

utils/

tests/

main.py

requirements.txt
```

At this stage, most folders will be empty. They establish the architecture defined in Phase 0 and prevent future restructuring.

---

# Step 8 — Create the Initial FastAPI Application

Create `app/main.py`.

Initial responsibilities:

* Create the FastAPI application instance.
* Register routers (currently none).
* Configure metadata (title, version, description).
* Expose the root application.

Keep `main.py` minimal. It should act only as the application's entry point. As features are added, configuration will be delegated to dedicated modules under `core/`.

---

# Step 9 — Run the Development Server

Start the server from the `backend` directory.

```bash
uvicorn app.main:app --reload
```

Command breakdown:

* `uvicorn` — Starts the ASGI server.
* `app.main` — Points to `app/main.py`.
* `app` — Refers to the FastAPI application instance inside `main.py`.
* `--reload` — Automatically restarts the server whenever source files change.

Use `--reload` only during development.

---

# Step 10 — Verify the Backend

If startup succeeds, you should see output similar to:

```text
Application startup complete.

Uvicorn running on http://127.0.0.1:8000
```

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI should load successfully.

Also verify:

```text
http://127.0.0.1:8000/redoc
```

This confirms:

* FastAPI application loads.
* Uvicorn is working.
* Routing system is initialized.
* OpenAPI documentation is generated.

At this point, no functional endpoints are expected beyond the default application setup.

---

# Backend Verification Checklist

Before moving to the next chapter, verify:

* ✅ Project root created.
* ✅ Backend directory created.
* ✅ Virtual environment activated.
* ✅ Required packages installed.
* ✅ `requirements.txt` generated.
* ✅ Initial folder structure created.
* ✅ `main.py` exists.
* ✅ Uvicorn starts successfully.
* ✅ Swagger UI opens.
* ✅ ReDoc opens.
* ✅ No startup errors appear in the terminal.

Do not continue until every item above is confirmed.

---

# Common Mistakes

Avoid the following issues:

* Running commands outside the `backend` directory.
* Forgetting to activate the virtual environment before installing packages.
* Installing packages globally instead of inside the virtual environment.
* Committing the `venv/` directory to Git (it should be ignored).
* Forgetting to regenerate `requirements.txt` after adding new packages.
* Launching the application with an incorrect module path (for example, `main:app` instead of `app.main:app`).

---

# Best Practices

* Keep the virtual environment isolated to the project.
* Install only dependencies that are actually required.
* Update `requirements.txt` whenever dependencies change.
* Start the server with `--reload` during development only.
* Keep `main.py` lightweight; application logic belongs in dedicated modules.
* Validate the application startup after every significant structural change.

---

# Chapter Deliverable

At the end of this chapter, the backend foundation is ready.

Current status:

```text
AI-Research-Knowledge-Assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── dependencies/
│   │   ├── exceptions/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── providers/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── venv/
├── frontend/
├── docs/
├── docker/
└── scripts/
```

The backend is now running and prepared for implementing the project's architecture.

---

## End of Chapter 1

