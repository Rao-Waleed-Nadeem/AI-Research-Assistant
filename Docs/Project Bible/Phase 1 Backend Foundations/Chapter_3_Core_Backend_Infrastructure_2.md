# Phase 1 — Backend Foundations

# Chapter 3 — Core Backend Infrastructure

## Part 2 — Shared Backend Infrastructure

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 1 — Backend Foundations  
> **Chapter:** 3 — Core Backend Infrastructure  
> **Part:** 2

---

# Objective

The purpose of this chapter is to build reusable backend components that every feature in our application will use.

Instead of implementing logging, middleware, responses, and exception handling inside each feature, we implement them once and reuse them everywhere.

This keeps the application:

- Consistent
- Maintainable
- Easy to debug
- Easy to extend

---

# Infrastructure Overview

The infrastructure layer sits between the framework and our business logic.

```text
                Request

                   │

                   ▼

            Middleware Layer

                   │

                   ▼

              API Route Layer

                   │

                   ▼

           Dependency Injection

                   │

                   ▼

             Business Services

                   │

        ┌──────────┴──────────┐

        ▼                     ▼

 Repository Layer       AI Service

        │                     │

        ▼                     ▼

 PostgreSQL            AI Provider
```

Every request will pass through this infrastructure.

---

# Infrastructure Components

Our reusable infrastructure consists of:

```text
Logging

↓

Dependency Injection

↓

Middleware

↓

Global Response Format

↓

Global Exception Handler
```

These components are shared by every feature.

---

# Logging

## Purpose

Logging allows us to understand what the application is doing while it is running.

Logs are useful for:

- Debugging
- Monitoring
- Error investigation
- Performance analysis
- Production troubleshooting

Without logs, diagnosing issues becomes significantly more difficult.

---

# Logging Architecture

```text
Application

↓

Logger

↓

Console

↓

(Log File - Future)

↓

Monitoring Platform (Future)
```

Every module should use the same logger.

---

# Logging Location

Project structure:

```text
app/

core/

logging.py
```

This file initializes and configures logging.

No other module should configure logging independently.

---

# What We Log

The following events should be logged:

## Application

- Startup
- Shutdown
- Configuration loaded

---

## Authentication

- Successful login
- Failed login
- Invalid token
- Expired token

---

## AI

- Provider selected
- AI request started
- AI response completed
- AI failure
- Retry attempts

---

## Database

- Connection established
- Connection failure
- Migration status

---

## API

- Incoming request
- Response status
- Processing time

---

## Errors

- Exceptions
- Validation failures
- Unexpected crashes

---

# What We Never Log

Never log sensitive information.

Examples:

❌ Passwords

❌ JWT Tokens

❌ API Keys

❌ Database Passwords

❌ Credit Card Data

❌ Sensitive Personal Information

If sensitive information appears in logs, it becomes a security risk.

---

# Log Levels

Our project follows standard log levels.

| Level | Purpose |
|--------|----------|
| DEBUG | Development details |
| INFO | Normal application events |
| WARNING | Recoverable issues |
| ERROR | Request or operation failed |
| CRITICAL | Application cannot continue |

Development typically uses DEBUG.

Production typically uses INFO or WARNING.

---

# Logging Rules

Always log:

- Application startup
- Application shutdown
- Authentication events
- AI requests
- External API failures
- Database failures
- Unexpected exceptions

Never log normal business logic that creates unnecessary noise.

Logs should be meaningful.

---

# Dependency Injection

## Purpose

Dependency Injection allows shared resources to be reused without recreating them inside every route.

Instead of manually creating objects:

```text
Route

↓

Create Database

↓

Create User

↓

Create Logger
```

We inject them automatically.

---

# Dependencies Used In Our Project

Current dependencies:

```text
Database Session

Authenticated User

Application Settings
```

Future dependencies:

```text
Admin User

Premium User

Current Conversation

Rate Limiter

Permissions

Subscription Validation
```

---

# Dependency Flow

```text
Incoming Request

↓

Resolve Dependencies

↓

Route

↓

Service
```

Dependencies are resolved before the route executes.

If a dependency fails, the request stops immediately.

---

# Why Dependency Injection?

Imagine every protected route verifying JWT manually.

```text
Verify JWT

Verify JWT

Verify JWT

Verify JWT
```

Now imagine changing JWT validation.

Every route must be modified.

Instead:

```text
Dependency

↓

Every Protected Route
```

One implementation.

Unlimited reuse.

---

# Dependency Rules

Dependencies should contain:

- Authentication
- Shared validation
- Database session
- Common request objects

Dependencies should not contain:

- Business logic
- Database queries
- AI communication

---

# Middleware

Middleware processes every request before it reaches the API routes.

Think of middleware as security checkpoints.

```text
Request

↓

Middleware

↓

Route

↓

Response

↓

Middleware

↓

Client
```

---

# Middleware Used In Our Project

Current middleware:

```text
CORS

Logging

Request Timing
```

Future middleware:

```text
Security Headers

Rate Limiting

Compression

Trusted Hosts

Request ID

Monitoring
```

---

# Middleware Execution Order

```text
Client

↓

Request Logging

↓

CORS

↓

Request Timer

↓

API Route

↓

Business Logic

↓

Response

↓

Request Timer

↓

Logging

↓

Client
```

Every request follows the same pipeline.

---

# Middleware Responsibilities

Middleware should perform tasks that apply to every request.

Examples:

- Measure execution time
- Log requests
- Add security headers
- Enable CORS
- Attach request ID

Middleware should never:

- Execute business logic
- Call Gemini
- Execute SQL
- Validate feature-specific rules

---

# Global Response Format

Every API response should follow one consistent structure.

Whether the request succeeds or fails, the frontend should always know what to expect.

---

# Standard Success Response

Every successful request follows:

```json
{
    "success": true,
    "message": "Operation completed successfully.",
    "data": {},
    "errors": null
}
```

---

# Standard Error Response

Every failed request follows:

```json
{
    "success": false,
    "message": "Validation failed.",
    "data": null,
    "errors": [
        "Email already exists."
    ]
}
```

---

# Why Standard Responses?

Without a standard:

```text
Login Response

↓

Different Format

Chat Response

↓

Different Format

User Response

↓

Different Format
```

Frontend becomes complicated.

Instead:

```text
Every Endpoint

↓

Same Response Structure
```

Frontend logic becomes predictable.

---

# Response Rules

Every endpoint should return:

- success
- message
- data
- errors

Avoid returning raw objects directly.

Consistency simplifies frontend development and future API integrations.

---

# Global Exception Handler

Unexpected errors should never crash the application or expose internal implementation details.

Instead, every exception passes through one centralized handler.

---

# Exception Flow

```text
Request

↓

Route

↓

Service

↓

Exception

↓

Global Exception Handler

↓

Standard Error Response
```

The frontend always receives a predictable response.

---

# Exceptions We Handle

Examples include:

- Validation errors
- Authentication errors
- Authorization errors
- Database failures
- AI provider failures
- Resource not found
- Unexpected exceptions

---

# Why Centralized Error Handling?

Without it:

Every route handles errors differently.

Some return:

```text
Error
```

Others return:

```text
Something went wrong
```

Others crash.

Instead:

```text
Every Exception

↓

Global Handler

↓

Same Response Format
```

Consistency improves both user experience and debugging.

---

# Infrastructure Rules

The following rules apply across the entire backend.

### Rule 1

Logging is configured once.

---

### Rule 2

Every module uses the same logger.

---

### Rule 3

Dependencies contain shared functionality only.

---

### Rule 4

Middleware remains independent of business logic.

---

### Rule 5

Every response follows the standard response format.

---

### Rule 6

Every exception is handled centrally.

---

### Rule 7

Sensitive information is never logged or returned in API responses.

---

# Infrastructure Interaction

The shared infrastructure now surrounds every request.

```text
Client

↓

Middleware

↓

Dependencies

↓

Route

↓

Service

↓

Repository / AI Service

↓

Response Formatter

↓

Exception Handler (if needed)

↓

Client
```

Every future feature automatically benefits from this infrastructure without implementing it again.

---

# Verification Checklist

Before continuing, verify:

- ✅ Logging configuration is centralized.
- ✅ All modules use the shared logger.
- ✅ Dependency Injection is used for shared resources.
- ✅ Middleware is registered globally.
- ✅ Every endpoint follows the same response format.
- ✅ Exceptions are handled centrally.
- ✅ Sensitive information is never logged.
- ✅ Infrastructure is reusable across all modules.

---

# Deliverable

At the end of Part 2, the backend contains reusable infrastructure that will support every future feature.

Implemented foundation:

```text
Core Infrastructure

├── Logging
├── Dependency Injection
├── Middleware
├── Global Response Format
└── Global Exception Handling
```

From this point onward, new features only need to focus on business logic because the shared infrastructure is already in place.

---

## End of Chapter 3 — Part 2
