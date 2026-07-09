# Backend (FastAPI)

This folder contains the FastAPI backend.

## Prerequisites

- Python 3.11+
- PostgreSQL (local or via Docker)

## Setup (local)

```bash
cd backend
python -m venv .venv
# Windows
.\.venv\Scripts\activate

pip install -r requirements.txt

# Copy env example
cp .env.example .env

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload --port 8000
```

## Docker

Docker Compose will be added in a later milestone. For now, the repository is structured so that it can run locally once dependencies are installed.
