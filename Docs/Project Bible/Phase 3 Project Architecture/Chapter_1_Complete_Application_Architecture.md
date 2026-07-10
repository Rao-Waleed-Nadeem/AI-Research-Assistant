# Phase 3 — Project Architecture

# Chapter 1 — Complete Application Architecture

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 3 — Project Architecture  
> **Chapter:** 1 — Complete Application Architecture

---

# Objective

By this stage of the project, we have already built:

- Backend foundation
- Authentication
- Database layer
- Repository architecture
- Service layer
- AI provider architecture (planned)

Now it is important to understand **how all these components work together as one application**.

This chapter serves as the architectural blueprint of the backend. It explains how requests move through the system, the responsibility of every component, and how different modules interact without violating the project's architecture.

---

# Chapter Deliverable

After completing this chapter:

- ✅ Entire backend architecture is understood.
- ✅ Every backend component has a clearly defined responsibility.
- ✅ Request flow is standardized.
- ✅ AI flow is standardized.
- ✅ Database flow is standardized.
- ✅ Authentication flow is standardized.
- ✅ Folder responsibilities are finalized.

---

# Complete Backend Architecture

The backend follows a layered architecture where each layer has exactly one responsibility.

```text
                    Frontend
                        │
                        ▼
                 FastAPI Route
                        │
                        ▼
                Dependencies
                        │
                        ▼
                 Service Layer
               ┌────────┴────────┐
               ▼                 ▼
       Repository Layer     AI Service
               │                 │
               ▼                 ▼
         PostgreSQL        AI Provider
                                 │
                                 ▼
                     Gemini / OpenAI / Groq
                     OpenRouter / Ollama
```

Every request follows this architecture.

No layer is allowed to bypass another layer.

---

# High-Level Component Overview

The backend consists of several independent modules.

```text
Application

├── API Layer
├── Service Layer
├── Repository Layer
├── Database Layer
├── AI Layer
├── Core Layer
├── Middleware
├── Dependencies
├── Schemas
└── Models
```

Each module solves a specific problem.

Together they create a scalable backend.

---

# Component Responsibilities

---

## 1. API Layer

Location

```text
app/api/
```

Purpose

Acts as the entry point of every request.

Responsibilities

- Receive HTTP requests
- Validate request structure
- Call Services
- Return responses
- Apply authentication dependencies

The API layer should remain extremely lightweight.

It should **never** contain:

- Business logic
- Database queries
- AI calls

---

## API Flow

```text
Client

↓

API Route

↓

Service

↓

Response
```

---

# 2. Service Layer

Location

```text
app/services/
```

Purpose

Contains all business logic of the application.

Responsibilities

- Process application logic
- Coordinate repositories
- Coordinate AI providers
- Validate business rules
- Prepare responses

Services are the "brain" of the backend.

---

## Service Example

Authentication

```text
Login Request

↓

Verify Credentials

↓

Generate JWT

↓

Return Token
```

Chat

```text
User Prompt

↓

Store Message

↓

Call AI

↓

Save Response

↓

Return Chat
```

Everything happens inside Services.

---

# 3. Repository Layer

Location

```text
app/repositories/
```

Purpose

Handle communication with PostgreSQL.

Responsibilities

- Read data
- Insert data
- Update data
- Delete data
- Execute queries

Repositories know **how** to access data.

They do not know **why**.

---

## Repository Flow

```text
Service

↓

Repository

↓

SQLAlchemy

↓

PostgreSQL
```

---

# 4. Database Layer

Location

```text
app/db/
```

Purpose

Provide database infrastructure.

Responsibilities

- Database connection
- Session management
- Transactions
- Database initialization
- Migration support

The database layer is shared by every repository.

---

# Database Communication

```text
Repository

↓

Session

↓

SQLAlchemy

↓

PostgreSQL
```

Repositories never create their own database connections.

Everything is centralized.

---

# 5. AI Layer

Location

```text
app/providers/

app/services/
```

Purpose

Provide AI functionality while remaining independent from specific providers.

Responsibilities

- Send prompts
- Receive responses
- Handle provider errors
- Switch providers
- Retry requests

Business logic never communicates directly with Gemini or OpenAI.

Everything passes through providers.

---

## AI Architecture

```text
Service

↓

AI Service

↓

Provider

↓

Gemini
```

Future:

```text
Provider

↓

OpenAI

Groq

OpenRouter

Ollama
```

No business logic changes when switching providers.

---

# 6. Schema Layer

Location

```text
app/schemas/
```

Purpose

Validate data entering and leaving the backend.

Responsibilities

- Validate request body
- Validate query parameters
- Validate responses

Schemas protect Services from invalid input.

---

## Validation Flow

```text
Request

↓

Schema Validation

↓

Service
```

Invalid requests never reach the Service layer.

---

# 7. Model Layer

Location

```text
app/models/
```

Purpose

Define database tables.

Responsibilities

- Database columns
- Relationships
- Constraints

Models do not contain business logic.

---

# Model Flow

```text
Repository

↓

Model

↓

Database
```

Models describe the database structure only.

---

# 8. Dependency Layer

Location

```text
app/dependencies/
```

Purpose

Provide reusable dependencies.

Examples

- Current User
- Database Session
- Authentication

Instead of repeating the same logic across multiple routes, dependencies are injected where required.

---

## Dependency Flow

```text
Request

↓

Dependency

↓

Route
```

Example

```text
JWT

↓

Current User

↓

Route
```

---

# 9. Middleware

Location

```text
app/middleware/
```

Purpose

Handle application-wide processing before and after requests.

Responsibilities

Examples include:

- Logging
- CORS
- Request timing
- Exception handling

Middleware runs automatically for every request.

---

## Middleware Flow

```text
Incoming Request

↓

Middleware

↓

Route

↓

Response

↓

Middleware
```

---

# 10. Core Layer

Location

```text
app/core/
```

Purpose

Contains shared application utilities.

Responsibilities

- Configuration
- Security
- Logging
- Constants
- Shared utilities

The Core layer supports every other module.

---

# Folder Responsibility Summary

| Folder | Responsibility |
|----------|----------------|
| **api/** | HTTP endpoints |
| **services/** | Business logic |
| **repositories/** | Database operations |
| **models/** | Database tables |
| **schemas/** | Request/Response validation |
| **providers/** | External AI providers |
| **middleware/** | Request processing |
| **dependencies/** | Shared dependencies |
| **core/** | Configuration & utilities |
| **db/** | Database infrastructure |

Each folder has one responsibility.

No folder should perform another folder's job.

---

# End-to-End Request Flow

A normal authenticated request follows this sequence.

```text
Frontend

↓

HTTP Request

↓

Middleware

↓

API Route

↓

Authentication Dependency

↓

Schema Validation

↓

Service

↓

Repository

↓

SQLAlchemy

↓

PostgreSQL

↓

Repository

↓

Service

↓

Standard Response

↓

Frontend
```

Every standard backend request follows this architecture.

---

# End-to-End AI Request Flow

An AI request introduces the AI layer.

```text
Frontend

↓

API Route

↓

Authentication

↓

Validation

↓

Chat Service

↓

Conversation Repository

↓

Store User Message

↓

AI Service

↓

Provider

↓

Gemini

↓

Receive AI Response

↓

Store AI Response

↓

Repository

↓

Response

↓

Frontend
```

Notice:

The Route never knows which AI provider generated the response.

---

# End-to-End Authentication Flow

```text
Frontend

↓

Login Route

↓

Authentication Service

↓

User Repository

↓

Database

↓

Password Verification

↓

JWT Generation

↓

Frontend

↓

Future Requests

↓

Current User Dependency

↓

Protected Routes
```

This authentication flow is reused by every secured endpoint.

---

# Architectural Rules

Every component must follow these rules.

### API Layer

- Only receives requests.
- Never contains business logic.

---

### Service Layer

- Controls application behavior.
- Never accesses SQLAlchemy directly.

---

### Repository Layer

- Only communicates with the database.
- Never calls AI providers.

---

### AI Layer

- Only communicates with external AI services.
- Never contains HTTP route logic.

---

### Database Layer

- Only manages persistence.
- Never processes business rules.

---

### Schema Layer

- Only validates data.
- Never queries the database.

---

# Architecture Principles

Throughout the project we follow these principles:

- One responsibility per layer.
- One direction of communication.
- No layer bypasses another.
- Business logic stays centralized.
- Database access stays centralized.
- AI access stays centralized.
- Configuration stays centralized.
- Shared logic is reusable.

These principles keep the application modular and maintainable as it grows.

---

# Architecture Checklist

Before implementing any new feature, verify:

- ✅ Feature follows layered architecture.
- ✅ Routes remain lightweight.
- ✅ Services contain business logic.
- ✅ Repositories handle data access.
- ✅ Models define database structure.
- ✅ Schemas validate requests.
- ✅ Providers handle external AI communication.
- ✅ Dependencies are reused.
- ✅ Middleware handles global concerns.
- ✅ No architectural rules are violated.

---

# Chapter Summary

The backend architecture is now fully defined.

Every request—whether it's authentication, chat, database access, or AI communication—follows the same predictable workflow.

This consistency makes the project:

- Easier to understand
- Easier to maintain
- Easier to scale
- Easier to test
- Easier for AI agents to extend

Future features will integrate into this architecture instead of creating new patterns.

---

# Deliverable

At the completion of Chapter 1:

- ✅ Complete backend architecture is documented.
- ✅ Every component has a defined responsibility.
- ✅ Standard request, database, authentication, and AI flows are established.
- ✅ The architectural foundation for the remainder of the project is complete.

---

## End of Chapter 1 — Complete Application Architecture

**Next:** **Chapter 2 — Backend Communication & Data Flow**, where we will document how requests, responses, validation, authentication, database operations, AI communication, logging, and error handling move through the application from start to finish.