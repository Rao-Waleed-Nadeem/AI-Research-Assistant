# Phase 1 — Backend Foundations

# Chapter 2 — Backend Core Architecture

## Part 3 — Application Bootstrap & Core Initialization

> Version: 1.0
>
> Status: Completed
>
> Phase: 1 — Backend Foundations
>
> Chapter: 2 — Backend Core Architecture
>
> Part: 3

---

# Objective

In the previous parts, we designed the architecture and understood how requests move through the system.

In this part, we will connect everything together by bootstrapping the application.

By the end of this chapter, our backend will have:

- A proper application entry point
- Centralized configuration
- Router registration
- Middleware registration
- Application metadata
- Project initialization flow

This completes the backend architecture and prepares the project for actual feature development.

---

# What is Application Bootstrap?

Bootstrap is the process of preparing the application before it starts accepting requests.

When the backend starts, it needs to know:

- What application to run
- Which routers exist
- Which middleware should execute
- Where configuration comes from
- Which settings are enabled
- How errors should be handled

Instead of placing everything inside one large `main.py`, our project separates these responsibilities into dedicated modules.

---

# Backend Bootstrap Architecture

```text
Start Application

        │

        ▼

Read Configuration

        │

        ▼

Create FastAPI App

        │

        ▼

Register Middleware

        │

        ▼

Register Routers

        │

        ▼

Initialize Shared Resources

        │

        ▼

Application Ready
```

Every time Uvicorn starts, this sequence is executed.

---

# Backend Directory After Bootstrap

```text
backend/

app/

│

├── api/

│      ├── router.py

│      └── endpoints/

│

├── core/

│      ├── config.py

│      ├── settings.py

│      ├── logging.py

│      └── security.py

│

├── middleware/

│      ├── cors.py

│      ├── logging.py

│      └── request_timer.py

│

├── dependencies/

├── providers/

├── repositories/

├── schemas/

├── services/

├── db/

├── models/

├── exceptions/

├── utils/

└── main.py
```

Some files will initially contain minimal implementations and will be expanded as the project grows.

---

# main.py

`main.py` is the application's entry point.

It is responsible for assembling the application, not implementing business logic.

Its responsibilities are limited to:

- Create FastAPI instance
- Load application settings
- Register middleware
- Register routers
- Configure metadata
- Start application

It should **not** contain:

- Authentication logic
- AI logic
- SQL queries
- Business rules
- Utility functions

Think of `main.py` as the project's **orchestrator**, responsible only for wiring components together.

---

# Why Keep main.py Small?

A common beginner mistake is placing the entire backend inside `main.py`.

Example of what **not** to do:

```text
main.py

800+
lines

Authentication

Database

Routes

AI

Logging

Configuration

Utilities
```

This quickly becomes difficult to maintain.

Our goal is different.

```text
main.py

↓

Create App

↓

Register Components

↓

Run Application
```

Business logic belongs elsewhere.

A well-structured `main.py` should remain concise even as the project grows.

---

# Application Metadata

The FastAPI application should define metadata that describes the API.

Examples include:

- Project title
- Description
- Version
- API documentation paths

These values improve generated documentation and provide consistency across environments.

Future updates (such as API version changes) should only require modifying configuration rather than multiple files.

---

# Configuration Architecture

Configuration should never be scattered across the project.

Instead, everything should originate from a central configuration module.

```text
Environment Variables

        │

        ▼

Settings

        │

        ▼

Configuration

        │

        ▼

Entire Application
```

This provides a single source of truth.

---

# Configuration Responsibilities

Configuration includes:

- Application name
- Version
- API prefix
- Debug mode
- Database URL
- JWT settings
- AI provider settings
- Logging configuration
- Environment type

No feature should hardcode these values.

---

# Why Centralized Configuration?

Imagine changing:

```
API Version

v1

↓

v2
```

If the value is hardcoded in ten files:

Ten modifications are required.

If stored centrally:

One modification updates the entire application.

Centralization improves consistency and reduces maintenance.

---

# Environment Variables

Our application will use environment variables for any value that changes between environments.

Examples include:

```text
DATABASE_URL

JWT_SECRET_KEY

GEMINI_API_KEY

OPENROUTER_API_KEY

DEBUG

ENVIRONMENT
```

These values are loaded during application startup.

They should never appear directly in source code.

---

# Router Registration

As the application grows, many API modules will exist.

Examples:

```text
Authentication

Users

Chat

AI

Health

Admin

Documents

Embeddings

RAG

Agents
```

Instead of registering every endpoint inside `main.py`, the project uses a centralized router.

Architecture:

```text
main.py

↓

api/router.py

↓

Auth Router

User Router

Chat Router

Health Router

...
```

This keeps `main.py` clean while making it easy to add new modules.

---

# Why Central Router?

Without a central router:

```text
main.py

↓

100+

router registrations
```

As the project grows, `main.py` becomes cluttered.

Instead:

```text
main.py

↓

Main Router

↓

Feature Routers
```

Each feature manages its own endpoints independently.

---

# Middleware Registration

Middleware affects every request entering the application.

Registration occurs once during startup.

Examples used in our project:

```text
CORS

Logging

Request Timing

Security Headers

Trusted Hosts

Compression (Future)

Rate Limiting (Future)
```

The application startup sequence determines the order in which middleware executes.

---

# Middleware Execution Flow

```text
Incoming Request

↓

Middleware 1

↓

Middleware 2

↓

Middleware 3

↓

API Route

↓

Service

↓

Response

↓

Middleware 3

↓

Middleware 2

↓

Middleware 1

↓

Client
```

Middleware processes both incoming requests and outgoing responses.

---

# Why Register Middleware Centrally?

Middleware should be consistent across the entire application.

Registering middleware in multiple places can lead to:

- Duplicate execution
- Inconsistent behavior
- Difficult debugging

A single registration point ensures predictable request processing.

---

# Logging Initialization

Logging should be initialized during application startup.

This guarantees that every component shares the same logging configuration.

Examples of future log events include:

- Application startup
- User login
- AI request
- Database failure
- Unexpected exception
- Server shutdown

Logging configuration belongs in the `core` package, not inside feature modules.

---

# Future Startup Tasks

As the project evolves, additional initialization steps may be added.

Examples include:

```text
Connect Database

↓

Initialize AI Provider

↓

Load Application Settings

↓

Verify Environment Variables

↓

Create Required Directories

↓

Initialize Monitoring
```

These tasks should be executed during startup, keeping feature modules focused on business logic.

---

# Backend Startup Sequence

Our complete backend initialization process is:

```text
Start Uvicorn

↓

Load Environment Variables

↓

Load Settings

↓

Create FastAPI Application

↓

Initialize Logging

↓

Register Middleware

↓

Register Routers

↓

Initialize Shared Resources

↓

Application Ready

↓

Accept Requests
```

This sequence ensures that every required component is available before the first request is processed.

---

# Startup Checklist

Whenever the application starts, verify that:

- Configuration loads successfully.
- Required environment variables exist.
- FastAPI application initializes.
- Middleware registers without errors.
- Routers register successfully.
- Swagger documentation is available.
- No startup exceptions occur.

Startup errors should be resolved before implementing new features.

---

# Backend Bootstrap Rules

The following rules apply throughout the project:

### Rule 1

`main.py` is responsible only for application assembly.

---

### Rule 2

Configuration must come from centralized settings.

---

### Rule 3

Never hardcode configuration values.

---

### Rule 4

All feature routers must be registered through the central router.

---

### Rule 5

Middleware should be registered only during application startup.

---

### Rule 6

Application startup should remain predictable and easy to understand.

---

# Backend Architecture Summary

The backend is now organized into independent, reusable layers.

```text
Frontend

        │

        ▼

FastAPI Application

        │

        ▼

Middleware

        │

        ▼

API Routes

        │

        ▼

Service Layer

        │

 ┌──────┴─────────┐

 ▼                ▼

Repository      AI Service

 │                │

 ▼                ▼

PostgreSQL     Provider Layer

                   │

                   ▼

                Gemini
```

Every feature implemented in later phases will plug into this architecture without requiring structural changes.

---

# Architecture Verification Checklist

Before moving to the next chapter, verify:

- ✅ Backend folder structure follows the Project Bible.
- ✅ `main.py` acts only as the application entry point.
- ✅ Configuration is centralized.
- ✅ Environment variables are externalized.
- ✅ Routers are registered through a central router.
- ✅ Middleware registration is centralized.
- ✅ Startup flow is clearly defined.
- ✅ No business logic exists in bootstrap files.

If every item above is satisfied, the backend architecture is correctly established.

---

# Chapter Deliverable

At the completion of Chapter 2:

- ✅ Backend architecture is finalized.
- ✅ Folder responsibilities are defined.
- ✅ Request lifecycle is established.
- ✅ AI lifecycle is established.
- ✅ Application bootstrap process is designed.
- ✅ Configuration strategy is defined.
- ✅ Router registration strategy is defined.
- ✅ Middleware registration strategy is defined.

The project now has a stable architectural foundation that every future feature will follow.

---

## End of Chapter 2 — Backend Core Architecture

The backend architecture is now complete.

From this point onward, we no longer need to make architectural decisions for each feature. Instead, every new module—Authentication, Database, AI, RAG, Embeddings, Agents, Billing, or Monitoring—will fit naturally into the structure established in this chapter.

