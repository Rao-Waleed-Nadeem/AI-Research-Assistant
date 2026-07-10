# Phase 0 — Project Foundation

# Chapter 5 — Complete Folder Structure

> Version: 1.0
>
> Status: Completed
>
> Phase: 0 — Project Foundation
>
> Chapter: 5 — Complete Folder Structure

---

# Table of Contents

1. Introduction
2. Folder Structure Philosophy
3. Complete Project Structure
4. Root Directory
5. Frontend Structure
6. Backend Structure
7. Infrastructure Files
8. Naming Conventions
9. Folder Responsibilities
10. Growth Strategy
11. Best Practices
12. Common Mistakes
13. Chapter Summary

---

# 1. Introduction

As software projects grow, organizing code becomes just as important as writing it.

A poorly organized project quickly becomes difficult to understand and maintain. Developers waste time searching for files, duplicate logic across the codebase, and introduce bugs because responsibilities are unclear.

A well-designed folder structure provides:

- Clear separation of concerns
- Predictable locations for code
- Easier collaboration
- Better scalability
- Faster onboarding for new developers
- Cleaner architecture

Our goal is to organize the project so that every file has a clear purpose and every developer knows exactly where new code belongs.

---

# 2. Folder Structure Philosophy

Our folder structure follows these principles:

## Separation of Concerns

Each folder represents a single responsibility.

Examples:

- Routes handle HTTP requests.
- Services contain business logic.
- Repositories access the database.
- Models define database tables.
- Schemas validate data.
- Providers communicate with AI models.

No folder should contain unrelated responsibilities.

---

## Feature Scalability

The structure should support future features without major reorganization.

For example:

Today:

- Authentication
- Chat

Tomorrow:

- Documents
- Embeddings
- RAG
- AI Agents
- Billing

These features should integrate naturally into the existing structure.

---

## Predictability

Developers should never wonder where to place new code.

Examples:

New API → api/

New database model → models/

New service → services/

New AI provider → providers/

New validation schema → schemas/

Consistency improves productivity.

---

# 3. Complete Project Structure

```text
AI-Research-Knowledge-Assistant/
│
├── frontend/
│
├── backend/
│
├── docs/
│
├── docker/
│
├── scripts/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
```

The project is divided into independent sections.

---

# 4. Root Directory

## frontend/

Contains the complete Next.js application.

Responsibilities:

- User Interface
- Pages
- Components
- API communication
- Authentication state
- Styling

---

## backend/

Contains the FastAPI application.

Responsibilities:

- APIs
- Authentication
- Business logic
- AI integration
- Database operations

---

## docs/

Contains all documentation.

Examples:

- PROJECT_BIBLE.md
- API Documentation
- Architecture Diagrams
- Database Design
- Deployment Guides

Documentation should evolve alongside the project.

---

## docker/

Contains Docker-related files.

Examples:

- Dockerfiles
- Docker configurations
- Production container settings

Keeping Docker files together improves organization.

---

## scripts/

Contains helper scripts.

Examples:

- Database initialization
- Seed data
- Backup scripts
- Deployment helpers

Scripts automate repetitive tasks.

---

## README.md

Project overview.

Contains:

- Installation
- Features
- Quick Start
- Technologies
- Commands

---

## .env.example

Template for environment variables.

Never contains secrets.

Example:

```env
DATABASE_URL=
JWT_SECRET=
AI_PROVIDER=
GEMINI_API_KEY=
```

---

## .gitignore

Specifies files Git should ignore.

Examples:

- venv/
- node_modules/
- .env
- __pycache__/

Sensitive and generated files should never be committed.

---

## docker-compose.yml

Defines the complete local development environment.

Starts:

- Frontend
- Backend
- PostgreSQL

using one command.

---

# 5. Frontend Structure

```text
frontend/
│
├── public/
│
├── src/
│   │
│   ├── app/
│   │
│   ├── components/
│   │
│   ├── features/
│   │
│   ├── services/
│   │
│   ├── hooks/
│   │
│   ├── lib/
│   │
│   ├── types/
│   │
│   ├── utils/
│   │
│   ├── styles/
│   │
│   └── middleware.ts
│
├── package.json
├── tsconfig.json
└── next.config.ts
```

---

## public/

Contains static assets.

Examples:

- Images
- Icons
- Logos
- Fonts

---

## app/

Contains Next.js App Router pages.

Examples:

- Login
- Register
- Dashboard
- Chat
- Settings

This folder defines application routes.

---

## components/

Reusable UI components.

Examples:

- Button
- Card
- Navbar
- Sidebar
- Modal

Components should remain generic and reusable.

---

## features/

Feature-specific UI.

Examples:

```text
chat/

authentication/

profile/

documents/
```

Each feature owns its components, hooks, and logic.

---

## services/

Communicates with backend APIs.

Examples:

```text
auth.service.ts

chat.service.ts

user.service.ts
```

Frontend never communicates directly with AI providers.

All requests go through the backend.

---

## hooks/

Custom React hooks.

Examples:

```text
useAuth()

useChat()

useUser()
```

Hooks improve code reuse.

---

## lib/

Configuration and third-party integrations.

Examples:

- Axios client
- Authentication helpers
- Utility libraries

---

## types/

TypeScript interfaces.

Examples:

```typescript
User

Chat

Message

LoginResponse
```

Centralizing types improves consistency.

---

## utils/

Pure helper functions.

Examples:

- Date formatting
- String utilities
- Validators

Utilities should contain no business logic.

---

## styles/

Global styling.

Examples:

- globals.css
- theme configuration

---

# 6. Backend Structure

```text
backend/
│
├── app/
│   │
│   ├── api/
│   │
│   ├── core/
│   │
│   ├── db/
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │
│   ├── providers/
│   │
│   ├── dependencies/
│   │
│   ├── middleware/
│   │
│   ├── utils/
│   │
│   ├── exceptions/
│   │
│   └── main.py
│
├── alembic/
│
├── tests/
│
├── requirements.txt
│
└── Dockerfile
```

---

## api/

Contains API routes.

Examples:

```text
auth.py

chat.py

users.py
```

Responsibilities:

- Receive HTTP requests
- Validate request
- Call service layer
- Return response

Routes should remain thin.

---

## core/

Core application configuration.

Contains:

- Settings
- Configuration
- Security
- JWT
- Logging

Anything required by the entire application belongs here.

---

## db/

Database connection.

Contains:

- Database session
- Engine
- Base model

Every database interaction begins here.

---

## models/

Database models.

Each file represents a database table.

Examples:

```text
user.py

chat.py

message.py
```

---

## schemas/

Pydantic schemas.

Used for:

- Request validation
- Response formatting

Schemas are **not** database models.

---

## repositories/

Database access layer.

Responsibilities:

- CRUD operations
- SQL queries
- Transactions

Repositories know SQLAlchemy.

Services do not.

---

## services/

Business logic.

Examples:

```text
AuthService

ChatService

UserService

AIService
```

This is the heart of the backend.

Most application logic belongs here.

---

## providers/

AI provider implementations.

Examples:

```text
GeminiProvider

OpenAIProvider

GroqProvider

OpenRouterProvider

OllamaProvider
```

Every provider implements the same interface.

---

## dependencies/

FastAPI dependency injection.

Examples:

- Current user
- Authentication
- Database session

Keeps routes clean.

---

## middleware/

Application middleware.

Examples:

- Logging
- CORS
- Request timing

Middleware runs before or after requests.

---

## utils/

Small reusable helper functions.

Examples:

- Date helpers
- Token helpers
- Common validators

Should remain independent of business logic.

---

## exceptions/

Custom exception classes.

Instead of raising generic exceptions everywhere, define reusable application-specific exceptions.

Examples:

```text
InvalidCredentials

UserAlreadyExists

ProviderUnavailable
```

---

## main.py

Application entry point.

Responsibilities:

- Create FastAPI app
- Register routes
- Configure middleware
- Start application

Business logic should never be written here.

---

## alembic/

Database migration management.

Tracks schema changes.

---

## tests/

Contains all automated tests.

Examples:

```text
API Tests

Unit Tests

Integration Tests
```

Testing should mirror the project structure.

---

# 7. Infrastructure Files

| File | Purpose |
|-------|---------|
| Dockerfile | Backend container definition |
| docker-compose.yml | Multi-container orchestration |
| requirements.txt | Python dependencies |
| package.json | Frontend dependencies |
| tsconfig.json | TypeScript configuration |
| next.config.ts | Next.js configuration |

---

# 8. Naming Conventions

Consistency is essential.

## Files

Use:

```text
snake_case.py
```

Python examples:

```text
user_service.py

chat_repository.py
```

Frontend:

```text
chat.service.ts

user.types.ts
```

React Components:

```text
ChatWindow.tsx

LoginForm.tsx

Sidebar.tsx
```

---

## Classes

Use PascalCase.

Examples:

```python
UserService

ChatRepository

GeminiProvider
```

---

## Functions

Use snake_case in Python.

```python
create_user()

send_message()
```

Use camelCase in TypeScript.

```typescript
createUser()

sendMessage()
```

---

# 9. Folder Responsibilities

| Folder | Responsibility |
|---------|----------------|
| app | Application source code |
| api | HTTP endpoints |
| services | Business logic |
| repositories | Database access |
| providers | AI integrations |
| schemas | Validation |
| models | Database tables |
| middleware | Request pipeline |
| dependencies | Dependency Injection |
| tests | Testing |
| docs | Documentation |
| docker | Containerization |

Every folder exists for a specific reason. Responsibilities should never overlap.

---

# 10. Growth Strategy

Our structure is designed to grow.

Future additions:

```text
features/

documents/

embeddings/

rag/

agents/

billing/

notifications/

analytics/
```

These can be added without reorganizing existing code.

---

# 11. Best Practices

- Keep files focused on one responsibility.
- Avoid large "utility" files containing unrelated functions.
- Place code where developers naturally expect it.
- Prefer composition over duplication.
- Mirror the architecture in the folder structure.
- Keep business logic out of API routes.
- Keep SQL out of services.
- Keep AI logic inside providers and AI services.
- Document major architectural decisions.

---

# 12. Common Mistakes

Avoid:

- Mixing frontend and backend responsibilities.
- Writing business logic in routes.
- Accessing the database directly from API endpoints.
- Calling AI providers from controllers.
- Storing secrets in source code.
- Creating generic folders like "misc" or "helpers" for unrelated code.
- Deeply nesting directories without clear purpose.

A clean folder structure should make the project easier to navigate, not more complex.

---

# 13. Chapter Summary

This chapter established the production-ready folder structure for the AI Research & Knowledge Assistant.

We defined the organization of the project from the root directory down to individual backend and frontend modules. Every folder has a single responsibility, supporting a clean architecture that promotes maintainability, scalability, and team collaboration.

By following this structure consistently, developers can quickly locate code, introduce new features with minimal friction, and ensure that the project remains organized as it grows from a simple AI chat application into a full-featured AI SaaS platform.

The folder structure defined here will serve as the foundation for every implementation in the chapters that follow.

---

## End of Chapter 5
