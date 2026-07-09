# AI Knowledge Assistant - Project README

## Overview

This project is a production-style AI SaaS built while learning Full Stack AI Engineering.

### Updated Technology Stack

- **Frontend:** Next.js, TypeScript, Tailwind CSS, shadcn/ui
- **Backend:** FastAPI
- **Database:** PostgreSQL (Docker)
- **ORM:** SQLAlchemy + Alembic
- **Authentication:** JWT
- **AI Layer:** Provider abstraction (`AIService`)
- **AI Providers:**
  - ✅ Gemini (Primary - Free)
  - ✅ OpenRouter
  - ✅ Groq
  - ✅ Ollama (Local)
  - 🔄 OpenAI (Optional)

## Architecture

```text
User
  │
Next.js
  │
FastAPI
  │
AI Service
 ├── Gemini
 ├── Groq
 ├── OpenRouter
 ├── Ollama
 └── OpenAI
  │
PostgreSQL (Docker)
```

## Why this architecture?

- AI provider can be swapped without changing routes.
- Docker runs PostgreSQL consistently on every machine.
- Clean layered architecture.
- Ready for production deployment.

## Folder Structure

```text
project/
├── frontend/
├── backend/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   │    ├── ai/
│   │    │    ├── base.py
│   │    │    ├── gemini.py
│   │    │    ├── groq.py
│   │    │    ├── openrouter.py
│   │    │    ├── ollama.py
│   │    │    └── openai.py
│   ├── auth/
│   └── main.py
├── docker-compose.yml
├── .env
└── README.md
```

## Request Flow

```text
User
 ↓
Next.js
 ↓
FastAPI Route
 ↓
JWT
 ↓
Validation
 ↓
Service
 ↓
Repository
 ↓
PostgreSQL
 ↓
AI Provider
 ↓
Response
```

## Docker

Docker will be introduced before deployment and will be used to run:

- Backend
- PostgreSQL
- (Later) Frontend

Run everything with:

```bash
docker compose up
```

No local PostgreSQL installation required.

## Environment Variables

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=

AI_PROVIDER=gemini

GEMINI_API_KEY=
OPENAI_API_KEY=
GROQ_API_KEY=
OPENROUTER_API_KEY=

OLLAMA_BASE_URL=http://localhost:11434
```

## AI Agent Rules

- Never call an AI provider directly from routes.
- Always use AIService abstraction.
- Keep business logic inside services.
- Keep database logic inside repositories.
- Validate using Pydantic.
- Use dependency injection.
- Store secrets only in .env.
- Docker manages PostgreSQL.

## Current Progress

- ✅ Phase 0
- ✅ Phase 1
- ✅ Phase 2
- ✅ Phase 3
- ⬜ AI Integration (Gemini first)
- ⬜ Embeddings
- ⬜ RAG
- ⬜ Agents
- ⬜ Docker Compose
- ⬜ AWS Deployment

## Planned Improvements

- Vector database
- Chat history
- PDF upload
- Semantic search
- RAG
- AI agents
- Logging
- Rate limiting
- Production deployment
