### 1. Project Overview

- Project objective
- Tech stack
- High-level architecture
- Features completed so far
- Current progress (completed through Phase 4 / Day 6)

---

### 2. Folder Structure

A complete production-ready folder tree, for example:

```text
AI-Knowledge-Assistant/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── services/
│   ├── types/
│   └── ...
│
├── backend/
│   ├── app/
│   │
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── auth/
│   ├── utils/
│   ├── migrations/
│   ├── main.py
│   └── ...
│
├── docker-compose.yml
├── README.md
└── .env
```

---

### 3. Complete Backend Architecture

Explain every layer.

```
Client

↓

FastAPI Route

↓

Authentication

↓

Pydantic Validation

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy

↓

PostgreSQL

↓

Response
```

---

### 4. Request Lifecycle

Exactly the workflow we learned.

```
User

↓

Next.js

↓

POST /chat

↓

JWT

↓

Validation

↓

AI Service

↓

Repository

↓

Database

↓

OpenAI

↓

Response

↓

Frontend
```

---

### 5. Database Design

ER Diagram

Users

Chats

Messages

Relationships

Foreign Keys

Responsibilities

---

### 6. SQLAlchemy Models

Explain

User

Chat

Message

Relationships

---

### 7. Pydantic Schemas

Request schemas

Response schemas

Validation

Serialization

Deserialization

---

### 8. Authentication

JWT Flow

Password Hashing

Dependencies

Protected Routes

---

### 9. OpenAI Integration

Client

Environment Variables

Chat Completion

Messages

Roles

System Prompt

Temperature

Structured Output

---

### 10. AI Service

Responsibilities

Conversation Builder

Prompt Builder

OpenAI Client

Response Parser

Error Handling

Retry Strategy

---

### 11. Repository Layer

Responsibilities

CRUD

Transactions

Commit

Rollback

Session Management

---

### 12. API Endpoints

For each endpoint:

```
POST /register

Purpose

Request

Response

Validation

Flow
```

Same for

```
POST /login

GET /me

POST /chat
```

---

### 13. Dependency Injection

Database Session

Current User

AI Service

Repositories

---

### 14. Environment Variables

Every variable

Purpose

Example

```
OPENAI_API_KEY

DATABASE_URL

SECRET_KEY

ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES
```

---

### 15. Complete Folder Explanation

Every folder

Every file

Why it exists

Responsibilities

Example

```
services/

Contains business logic.

Should never communicate directly with frontend.

Calls repositories.

Calls OpenAI.
```

---

### 16. Development Workflow

How to build new features.

```
Requirement

↓

Model

↓

Schema

↓

Repository

↓

Service

↓

Route

↓

Test

↓

Frontend
```

---

### 17. Coding Standards

Naming

Error handling

Validation

Repository rules

Service rules

Route rules

---

### 18. AI Agent Instructions

A dedicated section telling any AI assistant exactly how to work on this project.

Example:

```
Never put database logic inside routes.

Never call OpenAI directly from routes.

Always create schemas.

Always use repositories.

Always use dependency injection.

Follow layered architecture.

Never skip validation.
```

---

### 19. Commands

Every command used until now.

Python

Virtual Environment

FastAPI

Alembic

PostgreSQL

Run Server

Migration

Install Packages

---

### 20. Current Progress

Checklist

```
✅ Phase 0

✅ Phase 1

✅ Phase 2

✅ Phase 3

✅ Phase 4

⬜ Phase 5
```

---

### 21. Future Roadmap

Exactly where we stopped.

```
Day 7

Embeddings

↓

Day 8

RAG

↓

Day 10

Agents

↓

Docker

↓

AWS
```

---

### 22. Common Errors

Everything we've discussed.

422

401

500

JWT

OpenAI

Database

Migration

Alembic

---

### 23. Debugging Guide

Layer-by-layer debugging.

---

### 24. Mini Project Status

Current completed features.

```
✅ Authentication

✅ PostgreSQL

✅ SQLAlchemy

✅ JWT

✅ OpenAI Integration

✅ AI Service

✅ Repository Layer

✅ Chat Endpoint

⬜ Embeddings

⬜ RAG

⬜ Agents
```
