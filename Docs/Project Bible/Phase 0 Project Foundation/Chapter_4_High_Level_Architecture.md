# Phase 0 — Project Foundation

# Chapter 4 — High-Level Architecture

> Version: 1.0
>
> Status: Completed
>
> Phase: 0 — Project Foundation
>
> Chapter: 4 — High-Level Architecture

---

# Table of Contents

1. Introduction
2. What is Software Architecture?
3. Architecture Goals
4. System Overview
5. High-Level System Architecture
6. Component Responsibilities
7. Complete Request Flow
8. Complete Response Flow
9. Authentication Flow
10. AI Request Flow
11. Database Interaction
12. Layer Responsibilities
13. Why This Architecture?
14. Scalability Considerations
15. Security Considerations
16. Future Expansion
17. Chapter Summary

---

# 1. Introduction

Every successful software product is built upon a well-designed architecture.

Architecture is the blueprint of the application. It defines:

- What components exist.
- How they communicate.
- Who is responsible for what.
- How data flows.
- How the application grows over time.

Think of architecture as the blueprint of a house.

Before building walls, windows, or painting rooms, an architect first designs:

- The foundation
- Electrical system
- Plumbing
- Structural support
- Room layout

Software follows exactly the same principle.

Before writing code, we design how the system should work.

---

# 2. What is Software Architecture?

Software architecture is the high-level design of a software system.

It describes:

- Major components
- Communication between components
- Responsibilities
- Data flow
- System boundaries

It does **not** describe individual functions or classes.

Instead, it answers questions like:

- Where does user authentication happen?
- Where is business logic written?
- Which component talks to the database?
- Which component communicates with AI providers?
- How are requests processed?
- How are responses returned?

Architecture provides a common understanding for the entire development team.

---

# 3. Architecture Goals

Our architecture is designed around several key principles.

## Separation of Concerns

Every component has one responsibility.

Examples:

- Frontend handles UI.
- Backend handles business logic.
- Database stores data.
- AI providers generate responses.

No component should perform another component's responsibility.

---

## Scalability

The system should support:

- More users
- More AI providers
- More APIs
- More database tables
- More features

without requiring major redesign.

---

## Maintainability

The codebase should remain:

- Organized
- Readable
- Easy to debug
- Easy to extend

---

## Reusability

Business logic should be reusable.

For example:

The same AI service can be used by:

- Chat
- PDF Chat
- AI Agents
- Summarization
- Future APIs

without duplication.

---

## Security

Sensitive operations must remain inside the backend.

Examples:

- API keys
- JWT validation
- Password hashing
- Database access

The frontend should never have direct access to these resources.

---

# 4. System Overview

Our application consists of six major layers.

```text
                User
                  │
                  ▼
          Next.js Frontend
                  │
          HTTPS / REST API
                  │
                  ▼
          FastAPI Backend
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
Authentication  AI Service  Database Service
                     │
                     ▼
            AI Provider Layer
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
  Gemini          OpenAI           Groq
                     │
                     ▼
                 OpenRouter
                     │
                     ▼
                  Ollama

          PostgreSQL Database
```

Each layer has a clearly defined responsibility.

---

# 5. High-Level System Architecture

The complete architecture can be visualized as follows.

```text
                    ┌──────────────────────────┐
                    │          User            │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     Next.js Frontend     │
                    └────────────┬─────────────┘
                                 │
                     HTTPS / REST API
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     FastAPI Backend      │
                    └────────────┬─────────────┘
                                 │
       ┌───────────────┬─────────┴──────────┬──────────────┐
       ▼               ▼                    ▼              ▼
 Authentication   Chat Service       User Service    AI Service
       │               │                    │              │
       └───────────────┴──────────────┬─────┘              │
                                      ▼                    ▼
                               Repository Layer     Provider Layer
                                      │                    │
                                      ▼                    ▼
                               PostgreSQL        Gemini/OpenAI/
                                                   Groq/OpenRouter/
                                                       Ollama
```

---

# 6. Component Responsibilities

## User

The user interacts with the application through a web browser.

Responsibilities:

- Login
- Register
- Ask questions
- View conversations
- Manage profile

The user never communicates directly with the backend or database.

---

## Next.js Frontend

The frontend is responsible for:

- Displaying pages
- Collecting user input
- Showing AI responses
- Managing authentication state
- Calling backend APIs
- Rendering UI

It does **not**:

- Access databases
- Store API keys
- Perform business logic
- Call AI providers directly

---

## FastAPI Backend

The backend acts as the application's brain.

Responsibilities:

- Authentication
- Validation
- Business logic
- AI communication
- Database operations
- Security
- Error handling

Every request passes through the backend.

---

## Authentication Service

Handles:

- Registration
- Login
- JWT creation
- JWT verification
- Password hashing
- Protected routes

---

## Chat Service

Responsible for:

- Creating chats
- Sending prompts
- Receiving AI responses
- Saving messages
- Managing conversation history

---

## AI Service

Acts as an abstraction layer.

Responsibilities:

- Select provider
- Send prompts
- Retry failed requests
- Standardize responses
- Hide provider-specific implementation

No route should communicate directly with Gemini or OpenAI.

---

## Provider Layer

Contains provider-specific implementations.

Examples:

- Gemini Provider
- OpenAI Provider
- Groq Provider
- OpenRouter Provider
- Ollama Provider

Each provider implements the same interface.

This allows changing providers without modifying business logic.

---

## Repository Layer

The repository layer communicates with PostgreSQL.

Responsibilities:

- CRUD operations
- Queries
- Transactions
- Data persistence

Business logic should never directly write SQL.

---

## PostgreSQL

Stores persistent data.

Examples:

- Users
- Chats
- Messages
- AI Settings
- Future Documents
- Future Embeddings Metadata

---

# 7. Complete Request Flow

Whenever the user interacts with the application, the request follows a predictable path.

```text
User

↓

Next.js UI

↓

API Client

↓

FastAPI Route

↓

Authentication

↓

Validation

↓

Service Layer

↓

Repository / AI Service

↓

Database or AI Provider

↓

Response

↓

Frontend

↓

User
```

Every request follows this architecture.

This consistency improves maintainability and debugging.

---

# 8. Complete Response Flow

The response travels in the opposite direction.

```text
Database / AI Provider

↓

Repository

↓

Service

↓

API Route

↓

JSON Response

↓

Frontend

↓

React Components

↓

User Interface
```

This layered response prevents unnecessary coupling.

---

# 9. Authentication Flow

Authentication follows this process.

```text
User Login

↓

Frontend

↓

POST /login

↓

FastAPI

↓

Validate Credentials

↓

Verify Password

↓

Generate JWT

↓

Return Token

↓

Frontend Stores Token

↓

Future Requests

↓

Authorization Header

↓

JWT Verification

↓

Protected API
```

The JWT token is the user's identity throughout the session.

---

# 10. AI Request Flow

AI interactions follow a dedicated path.

```text
User Prompt

↓

Frontend

↓

FastAPI

↓

JWT Validation

↓

Chat Service

↓

AI Service

↓

Provider Factory

↓

Selected Provider

↓

Gemini
(OpenAI / Groq / Ollama)

↓

AI Response

↓

Chat Service

↓

Save Conversation

↓

Frontend

↓

User
```

Notice that the frontend never communicates directly with an AI provider.

This protects API keys and centralizes AI logic.

---

# 11. Database Interaction

Every database operation follows the same architecture.

```text
Frontend

↓

API Route

↓

Service Layer

↓

Repository

↓

SQLAlchemy

↓

PostgreSQL

↓

SQLAlchemy

↓

Repository

↓

Service

↓

Route

↓

Frontend
```

This ensures:

- Reusable queries
- Easier testing
- Better organization
- Consistent transactions

---

# 12. Layer Responsibilities

| Layer | Responsibility |
|--------|----------------|
| Frontend | User Interface & User Experience |
| API Routes | Receive HTTP requests and return responses |
| Authentication | Identity verification and authorization |
| Validation | Validate incoming data |
| Service Layer | Business logic |
| AI Service | AI provider abstraction |
| Repository | Database communication |
| SQLAlchemy | ORM |
| PostgreSQL | Persistent storage |
| AI Providers | Generate AI responses |

Each layer has one responsibility.

This follows the **Single Responsibility Principle (SRP)**.

---

# 13. Why This Architecture?

Many beginners place all code inside API routes.

Example:

```python
@app.post("/chat")
async def chat():
    # validation
    # authentication
    # AI call
    # database
    # formatting
```

While this may work initially, it quickly becomes difficult to maintain.

Our architecture separates these concerns into dedicated layers.

Benefits:

- Cleaner code
- Easier testing
- Better scalability
- Easier debugging
- Higher reusability
- Team collaboration

---

# 14. Scalability Considerations

Our architecture allows us to grow the application without significant changes.

Examples:

Today:

```text
Chat
```

Tomorrow:

```text
Chat

↓

PDF Chat

↓

Knowledge Base

↓

AI Agents

↓

Research Assistant

↓

Tool Calling
```

The existing AI Service can support all of these features.

Similarly, adding another AI provider only requires creating a new provider implementation.

No changes are required in:

- Frontend
- Routes
- Chat Service

This demonstrates the value of abstraction.

---

# 15. Security Considerations

Security is integrated into the architecture.

Key principles:

- API keys remain on the backend.
- Passwords are hashed before storage.
- JWT tokens protect private routes.
- All requests are validated.
- Sensitive logic never executes in the browser.
- Database access is restricted to the repository layer.
- AI providers are never exposed directly to clients.

These practices reduce the application's attack surface.

---

# 16. Future Expansion

The architecture has been designed with future features in mind.

Planned additions include:

- PDF Upload
- Embeddings
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- AI Agents
- Streaming Responses
- Tool Calling
- Image Understanding
- Voice Support
- Admin Dashboard
- Billing
- Monitoring
- CI/CD
- Multi-user Organizations

Because the architecture is modular, these features can be added without redesigning the existing system.

---

# 17. Chapter Summary

This chapter defined the high-level architecture of the AI Research & Knowledge Assistant.

We established the major system components, their responsibilities, and how they interact. By separating concerns into dedicated layers—frontend, backend, services, repositories, AI providers, and database—we create a system that is easier to understand, maintain, test, and scale.

Every future chapter in this Project Bible will build upon this architectural foundation. Whether we are implementing authentication, database models, AI integration, Retrieval-Augmented Generation (RAG), Docker, or cloud deployment, each component will fit naturally into the structure defined here.

A well-designed architecture ensures that the application can evolve over time without requiring fundamental redesign, making it suitable not only for learning but also for production-quality software development.

---

## End of Chapter 4
