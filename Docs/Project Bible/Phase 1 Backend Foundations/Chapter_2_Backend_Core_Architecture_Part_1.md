# Phase 1 — Backend Foundations

# Chapter 2 — Backend Core Architecture

## Part 1 — Backend Architecture Overview & Folder Structure

> Version: 1.0
>
> Status: Completed
>
> Phase: 1 — Backend Foundations
>
> Chapter: 2 — Backend Core Architecture
>
> Part: 1

---

# Objective

In Chapter 1, we prepared the backend environment and successfully ran our FastAPI application.

In this chapter, we define the architecture that every future feature in our project will follow.

This architecture is the backbone of the application. Authentication, AI Integration, Chat, RAG, Embeddings, AI Agents, Billing, and every future module will follow the exact same structure.

Changing this architecture later would require significant refactoring, so it is important to establish it correctly before implementing any business features.

---

# Expected Outcome

After completing this part, you should understand:

- The complete backend architecture
- The responsibility of every backend folder
- Where every new file should be placed
- How modules communicate
- Why this architecture was chosen for our project

At the end of this chapter, you should never have to ask:

> "Where should this file go?"

or

> "Where should this logic be written?"

The architecture itself should answer those questions.

---

# Backend Architecture Philosophy

Our project follows a **Layered Architecture** with clear separation of responsibilities.

Instead of putting everything inside a few files, every responsibility has its own dedicated layer.

This provides:

- Better readability
- Easier debugging
- Better testing
- Higher scalability
- Easier maintenance
- Easier AI-assisted development

Every layer has exactly one responsibility.

---

# High-Level Backend Architecture

```text
                Client (Frontend)
                       │
                       ▼
                 API Routes Layer
                       │
                       ▼
                 Service Layer
                  /           \
                 /             \
                ▼               ▼
      Repository Layer      AI Service
             │                   │
             ▼                   ▼
      PostgreSQL Database   AI Providers
                                 │
                                 ▼
                    Gemini / OpenAI / Groq / Ollama
```

Notice something important.

Database operations and AI operations are completely independent.

The Service Layer decides which one is needed.

Sometimes it calls only the database.

Sometimes only AI.

Sometimes both.

This flexibility is one of the reasons we designed the architecture this way.

---

# Complete Backend Folder Structure

Our backend will eventually look like this:

```text
backend/

│
├── app/
│
│   ├── api/
│   │
│   ├── core/
│   │
│   ├── db/
│   │
│   ├── dependencies/
│   │
│   ├── exceptions/
│   │
│   ├── middleware/
│   │
│   ├── models/
│   │
│   ├── providers/
│   │
│   ├── repositories/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── utils/
│   │
│   └── main.py
│
├── tests/
│
├── requirements.txt
│
└── .env
```

Although many folders are currently empty, every one of them exists for a specific reason.

---

# Folder Walkthrough

---

# app/

This is the application package.

Everything related to the backend lives inside this folder.

Think of it as the root of the backend application.

Nothing outside `app/` should contain application logic.

Contains:

- API
- Database
- Services
- Models
- Schemas
- Middleware
- Providers

Every import in the project begins here.

Example:

```python
from app.services.chat_service import ChatService
```

---

# api/

Purpose:

Expose HTTP endpoints.

This folder is responsible only for communicating with the frontend.

Examples:

```text
auth.py

chat.py

user.py

health.py
```

Each file contains routes related to one feature.

Responsibilities:

- Receive requests
- Validate request data
- Call the Service Layer
- Return responses

This folder should never contain business logic.

Think of it as the application's receptionist.

It receives requests and forwards them to the correct department.

---

# core/

Purpose:

Application-wide configuration.

Everything used globally belongs here.

Examples:

```text
config.py

security.py

logging.py

settings.py
```

This folder centralizes project configuration.

Instead of scattering configuration across the project, everything lives in one place.

Examples:

Database URL

JWT settings

Application settings

AI provider configuration

Logging configuration

Security configuration

---

# db/

Purpose:

Database initialization.

This folder connects the application to PostgreSQL.

Examples:

```text
database.py

base.py

session.py
```

Responsibilities:

- Database engine
- Session creation
- Base model registration
- Connection management

No SQL queries belong here.

Only database configuration.

---

# dependencies/

Purpose:

Reusable FastAPI dependencies.

Dependencies are shared components required by multiple routes.

Examples:

```text
current_user.py

database.py

permissions.py
```

Typical responsibilities:

- Database session
- Authenticated user
- Admin validation
- Shared request objects

Keeping dependencies here avoids repeating the same code in every route.

---

# exceptions/

Purpose:

Centralize exception handling.

Instead of handling errors differently everywhere, the project defines exceptions in one place.

Examples:

```text
auth_exception.py

database_exception.py

ai_exception.py
```

Benefits:

- Consistent API responses
- Cleaner services
- Easier debugging

---

# middleware/

Purpose:

Intercept requests before they reach the routes.

Examples:

```text
logging.py

cors.py

request_timer.py
```

Responsibilities:

- Logging
- Request timing
- Security headers
- CORS
- Future rate limiting

Middleware affects every request automatically.

---

# models/

Purpose:

Database models.

Every table inside PostgreSQL has exactly one model.

Examples:

```text
user.py

chat.py

message.py
```

Models define:

- Columns
- Data types
- Relationships
- Constraints

Models describe how data is stored.

They do not describe API requests.

---

# schemas/

Purpose:

Define request and response data.

Examples:

```text
user_schema.py

chat_schema.py

auth_schema.py
```

Schemas control:

- Input validation
- Response serialization
- API documentation

Schemas protect the application from invalid input.

Models describe the database.

Schemas describe the API.

These are different responsibilities and should never be mixed.

---

# services/

Purpose:

Business logic.

This is the heart of the application.

Examples:

```text
auth_service.py

chat_service.py

user_service.py

ai_service.py
```

Every important decision happens here.

Examples:

- Register user
- Login user
- Create chat
- Ask AI
- Save conversation
- Generate title

Services coordinate all other layers.

Most of the project's code will live here.

---

# repositories/

Purpose:

Database communication.

Repositories know how to talk to PostgreSQL.

Examples:

```text
user_repository.py

chat_repository.py

message_repository.py
```

Responsibilities:

- CRUD
- Queries
- Transactions
- Pagination

Repositories never contain business rules.

They simply fetch or store data.

---

# providers/

Purpose:

AI provider implementations.

This folder makes our project AI-provider independent.

Examples:

```text
gemini_provider.py

openai_provider.py

groq_provider.py

ollama_provider.py

openrouter_provider.py
```

Every provider implements the same interface.

The rest of the project never communicates with Gemini directly.

Instead it communicates with:

```text
AI Service

↓

Provider

↓

Gemini
```

This abstraction allows us to switch providers without changing the rest of the application.

---

# utils/

Purpose:

Small reusable helper functions.

Examples:

```text
datetime.py

strings.py

validators.py
```

Rules:

Utilities should be:

- Small
- Generic
- Stateless

Never put business logic inside utilities.

If a helper becomes feature-specific, move it to the appropriate Service.

---

# tests/

Purpose:

Project testing.

Eventually contains:

```text
unit/

integration/

api/
```

Every important feature should eventually have tests.

Testing is isolated from application code.

---

# requirements.txt

Lists every Python dependency required to run the backend.

Any developer can recreate the backend environment using:

```bash
pip install -r requirements.txt
```

This file should always remain synchronized with installed packages.

---

# .env

Stores configuration values that change between environments.

Examples:

- Database URL
- JWT Secret
- Gemini API Key
- OpenRouter API Key
- Logging Level

Sensitive information must never be hardcoded in source files.

---

# Architectural Responsibility Matrix

| Folder | Primary Responsibility | Should Contain |
|---------|------------------------|----------------|
| `api/` | HTTP communication | Routes only |
| `services/` | Business logic | Application workflows |
| `repositories/` | Database access | CRUD & queries |
| `models/` | Database structure | SQLAlchemy models |
| `schemas/` | API contracts | Pydantic models |
| `providers/` | AI integrations | Provider implementations |
| `middleware/` | Request pipeline | Middleware |
| `dependencies/` | Shared dependencies | FastAPI dependencies |
| `core/` | Global configuration | Settings, security, logging |
| `db/` | Database configuration | Engine, session, base |
| `exceptions/` | Custom errors | Exception classes |
| `utils/` | Generic helpers | Small reusable functions |

---

# Architecture Rules

The following rules are **non-negotiable** throughout the project:

### Rule 1

Every folder has one responsibility.

Never mix responsibilities.

---

### Rule 2

Never place business logic inside `api/`.

---

### Rule 3

Never access PostgreSQL outside the Repository Layer.

---

### Rule 4

Never call Gemini (or any AI provider) directly from routes.

Always go through the AI Service.

---

### Rule 5

Never expose SQLAlchemy models directly to the frontend.

Always use Schemas.

---

### Rule 6

Keep files focused.

One feature.

One responsibility.

---

# Checkpoint

At this stage, you should understand:

- Why every folder exists.
- What code belongs in each folder.
- What code must **not** be placed in each folder.
- How the backend is organized before implementing any features.

The physical folder structure is no longer just a collection of directories—it is the blueprint that enforces the project's architecture.

---

## End of Chapter 2 — Part 1
