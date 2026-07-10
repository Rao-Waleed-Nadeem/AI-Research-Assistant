# Phase 3 — Project Architecture

# Chapter 2 — Backend Communication & Data Flow

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 3 — Project Architecture  
> **Chapter:** 2 — Backend Communication & Data Flow

---

# Objective

A well-structured backend is not only about folder organization—it is also about how data flows through the application.

Every request in our project follows a predefined path. Whether it is:

- User Login
- User Registration
- AI Chat
- Load Conversations
- Create Messages
- Future Document Upload
- Future RAG Search

the communication flow remains consistent.

This chapter documents how data moves throughout the backend and how different components interact while maintaining clean architecture.

---

# Chapter Deliverable

After completing this chapter:

- ✅ Complete request lifecycle is documented.
- ✅ Response lifecycle is standardized.
- ✅ Authentication flow is finalized.
- ✅ Validation flow is established.
- ✅ Database communication flow is documented.
- ✅ AI communication flow is documented.
- ✅ Error handling flow is standardized.
- ✅ Logging flow is standardized.

---

# Backend Communication Philosophy

Every request should move through predictable layers.

A request should never jump directly from one component to another.

Correct communication:

```text
Frontend

↓

Route

↓

Service

↓

Repository

↓

Database
```

Incorrect communication:

```text
Frontend

↓

Route

↓

Database
```

or

```text
Frontend

↓

Route

↓

Gemini
```

Keeping communication structured makes the application easier to maintain and extend.

---

# Complete Request Lifecycle

Every incoming request follows the same sequence.

```text
Frontend

↓

HTTP Request

↓

Middleware

↓

API Route

↓

Authentication (If Required)

↓

Schema Validation

↓

Service

↓

Repository / AI Service

↓

Database / AI Provider

↓

Service

↓

Standard Response

↓

Frontend
```

Every request in the application follows this lifecycle.

---

# Request Processing Stages

Each stage performs one responsibility.

| Stage | Responsibility |
|--------|----------------|
| Frontend | Sends request |
| Middleware | Global processing |
| Route | Receives request |
| Dependency | Authentication |
| Schema | Validate data |
| Service | Business logic |
| Repository | Database operations |
| Provider | AI communication |
| Response | Return standardized response |

---

# Authentication Flow

Protected endpoints require authentication before reaching business logic.

```text
Frontend

↓

JWT Token

↓

Authorization Header

↓

Authentication Dependency

↓

Verify Token

↓

Load Current User

↓

Route

↓

Service
```

If authentication fails:

```text
Invalid Token

↓

Authentication Dependency

↓

Unauthorized Response

↓

Frontend
```

The request stops immediately.

Business logic is never executed.

---

# Validation Flow

Every request is validated before reaching the Service layer.

```text
Request

↓

Pydantic Schema

↓

Validation

↓

Valid Data

↓

Service
```

If validation fails:

```text
Request

↓

Schema

↓

Validation Error

↓

422 Response

↓

Frontend
```

Invalid requests never reach the database or AI provider.

---

# Standard API Request Flow

Example:

Load User Conversations.

```text
Frontend

↓

GET /conversations

↓

Authentication

↓

Conversation Service

↓

Conversation Repository

↓

Database

↓

Conversation Repository

↓

Service

↓

Response

↓

Frontend
```

This flow applies to every CRUD endpoint.

---

# User Registration Flow

```text
Frontend

↓

POST /register

↓

Validate Request

↓

Auth Service

↓

Check Existing Email

↓

User Repository

↓

Database

↓

Create User

↓

Hash Password

↓

Save User

↓

Success Response

↓

Frontend
```

---

# User Login Flow

```text
Frontend

↓

POST /login

↓

Validate Credentials

↓

Auth Service

↓

User Repository

↓

Database

↓

Verify Password

↓

Generate JWT

↓

Return Access Token

↓

Frontend
```

The frontend stores the JWT and uses it for future requests.

---

# Authenticated Request Flow

Once logged in:

```text
Frontend

↓

JWT

↓

Protected Route

↓

Current User Dependency

↓

Authenticated User

↓

Service

↓

Repository

↓

Database

↓

Response
```

Every protected API follows this process.

---

# Database Communication Flow

Services never communicate directly with PostgreSQL.

Instead:

```text
Service

↓

Repository

↓

SQLAlchemy

↓

Database
```

Benefits:

- Reusable queries
- Cleaner Services
- Easier maintenance
- Better testing

---

# Database Read Flow

Example:

```text
Service

↓

Repository

↓

Find Record

↓

Database

↓

Return Entity

↓

Service
```

---

# Database Write Flow

```text
Service

↓

Repository

↓

Insert Record

↓

Commit Transaction

↓

Database

↓

Return Entity

↓

Service
```

---

# AI Communication Flow

AI communication is isolated from business logic.

```text
Frontend

↓

Chat Route

↓

Chat Service

↓

AI Service

↓

Provider

↓

Gemini

↓

Provider

↓

AI Service

↓

Chat Service

↓

Response

↓

Frontend
```

The Chat Service never knows which AI provider generated the response.

---

# AI Conversation Flow

Complete chat processing:

```text
User Prompt

↓

Validate Request

↓

Authentication

↓

Store User Message

↓

AI Service

↓

Provider

↓

Gemini

↓

Receive Response

↓

Store AI Response

↓

Return Chat Response
```

Both user and AI messages are saved to maintain conversation history.

---

# Future AI Provider Flow

Adding a new provider should not change business logic.

```text
Chat Service

↓

AI Service

↓

Provider Interface

├── Gemini
├── OpenAI
├── Groq
├── OpenRouter
└── Ollama
```

Switching providers only changes the selected implementation.

---

# Response Lifecycle

Every successful request follows the same response process.

```text
Database / AI

↓

Service

↓

Standard Response

↓

Route

↓

Frontend
```

Responses should always use the project's standard response format.

Example:

```json
{
  "success": true,
  "message": "Operation completed successfully.",
  "data": {}
}
```

---

# Error Handling Flow

Unexpected errors should follow one centralized path.

```text
Exception

↓

Service

↓

Raise Exception

↓

Global Exception Handler

↓

Standard Error Response

↓

Frontend
```

Individual routes should not implement custom error formatting.

---

# Common Error Sources

Errors may originate from:

- Validation
- Authentication
- Database
- AI Provider
- Internal Server

Regardless of the source, they should return a consistent error response.

---

# Logging Flow

Logging provides visibility into application behavior.

Every request follows this process:

```text
Incoming Request

↓

Request Log

↓

Business Processing

↓

Database / AI

↓

Response Log

↓

Request Completed
```

If an error occurs:

```text
Request

↓

Exception

↓

Error Log

↓

Global Exception Handler

↓

Response
```

Logging should help developers diagnose issues without exposing sensitive information.

---

# Middleware Communication Flow

Middleware surrounds every request.

```text
Incoming Request

↓

Middleware

↓

Authentication

↓

Route

↓

Service

↓

Response

↓

Middleware

↓

Frontend
```

Examples of middleware responsibilities:

- Request logging
- CORS
- Response timing
- Global exception handling

---

# Dependency Flow

Dependencies provide reusable functionality before the Route executes.

```text
Request

↓

Dependency

↓

Authenticated User

↓

Route
```

Common dependencies:

- Current User
- Database Session
- Permissions (future)

---

# Future Feature Communication

Every future module follows the same architecture.

## Document Upload

```text
Frontend

↓

Route

↓

Document Service

↓

Repository

↓

Database
```

---

## RAG Search

```text
Frontend

↓

Route

↓

RAG Service

↓

Embedding Repository

↓

Vector Database (Future)

↓

AI Provider

↓

Response
```

---

## AI Agent

```text
Frontend

↓

Agent Route

↓

Agent Service

↓

AI Provider

↓

Response
```

No new communication pattern is introduced.

Every feature integrates into the existing architecture.

---

# Communication Rules

All modules must follow these rules.

### Rule 1

Requests always enter through API Routes.

---

### Rule 2

Routes never contain business logic.

---

### Rule 3

Services coordinate all operations.

---

### Rule 4

Repositories handle all database access.

---

### Rule 5

AI Providers handle all external AI communication.

---

### Rule 6

Schemas validate every request.

---

### Rule 7

Middleware handles global concerns.

---

### Rule 8

Responses always follow the standard response format.

---

### Rule 9

Errors are handled centrally.

---

### Rule 10

No component bypasses another layer.

---

# Communication Architecture Summary

```text
Frontend
    │
    ▼
Middleware
    │
    ▼
API Route
    │
    ▼
Dependencies
    │
    ▼
Schema Validation
    │
    ▼
Service Layer
   ├───────────────┐
   ▼               ▼
Repository     AI Service
   │               │
   ▼               ▼
Database      AI Provider
                   │
                   ▼
             Gemini/OpenAI/Groq
```

This architecture represents every request handled by the backend.

---

# Chapter Checklist

Before proceeding to the next chapter, verify:

- ✅ Request lifecycle documented.
- ✅ Authentication flow documented.
- ✅ Validation flow documented.
- ✅ Database flow documented.
- ✅ AI flow documented.
- ✅ Response lifecycle standardized.
- ✅ Error handling centralized.
- ✅ Logging flow established.
- ✅ Communication rules finalized.

---

# Deliverable

At the completion of Chapter 2:

- ✅ Every backend communication path is documented.
- ✅ Request and response lifecycles are standardized.
- ✅ Authentication, validation, database, AI, logging, and error flows are fully defined.
- ✅ The backend communication architecture is complete and ready to support all current and future features.

---

## End of Chapter 2 — Backend Communication & Data Flow

**Next:** **Chapter 3 — Engineering Standards & Feature Development**, where we establish project-wide implementation rules, feature development workflow, scalability strategy, and engineering standards that every future module must follow.