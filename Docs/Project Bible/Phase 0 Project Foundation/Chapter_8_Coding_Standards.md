# Phase 0 — Project Foundation

# Chapter 8 — Coding Standards

> Version: 1.0
>
> Status: Completed
>
> Phase: 0 — Project Foundation
>
> Chapter: 8 — Coding Standards

---

# Table of Contents

1. Introduction
2. Coding Philosophy
3. General Principles
4. Naming Conventions
5. Folder Organization Standards
6. File Organization
7. Import Standards
8. Code Formatting
9. Function Standards
10. Class Standards
11. API Route Standards
12. Service Layer Standards
13. Repository Standards
14. Database Model Standards
15. Schema Standards
16. Error Handling Standards
17. Logging Standards
18. Documentation & Comments
19. Clean Code Principles
20. SOLID Principles
21. DRY, KISS & YAGNI
22. Security Standards
23. Testing Standards
24. Common Mistakes
25. Chapter Summary

---

# 1. Introduction

Writing code that works is only the first step.

Professional software engineering focuses on writing code that is:

- Easy to read
- Easy to understand
- Easy to maintain
- Easy to test
- Easy to extend

Good coding standards ensure that every developer writes code in a consistent way, making the project easier to manage as it grows.

---

# 2. Coding Philosophy

Our codebase follows these principles:

- Readability over cleverness.
- Simplicity over unnecessary complexity.
- Consistency over personal preference.
- Reusability over duplication.
- Maintainability over shortcuts.
- Explicit code over implicit behavior.

Code is written for humans first and computers second.

---

# 3. General Principles

Every piece of code should:

- Have a single responsibility.
- Be easy to understand.
- Avoid duplication.
- Handle errors gracefully.
- Follow the project architecture.
- Be reusable where appropriate.
- Be secure by default.

Before writing code, always ask:

> "Does this belong here?"

---

# 4. Naming Conventions

Consistent naming makes the project predictable.

## Python Files

Use:

```text
snake_case.py
```

Examples:

```text
user_service.py

chat_repository.py

auth_router.py
```

---

## TypeScript Files

Use:

```text
kebab-case.ts

kebab-case.tsx
```

Examples:

```text
chat-service.ts

auth-provider.tsx

login-form.tsx
```

---

## Python Classes

Use:

```python
UserService

ChatRepository

GeminiProvider

JWTManager
```

Always use **PascalCase**.

---

## React Components

Use PascalCase.

Examples:

```text
ChatWindow.tsx

Sidebar.tsx

LoginForm.tsx
```

---

## Variables

Python:

```python
user_name

current_user

access_token
```

TypeScript:

```typescript
userName

currentUser

accessToken
```

Choose descriptive names. Avoid abbreviations unless they are industry-standard.

---

## Constants

Python:

```python
MAX_RETRIES

DEFAULT_TIMEOUT
```

TypeScript:

```typescript
MAX_RETRIES

API_TIMEOUT
```

Use uppercase with underscores.

---

## Functions

Python:

```python
create_user()

send_message()

verify_password()
```

TypeScript:

```typescript
createUser()

sendMessage()

verifyPassword()
```

Function names should describe an action.

---

# 5. Folder Organization Standards

Each folder must have a single responsibility.

| Folder | Responsibility |
|---------|----------------|
| api | HTTP endpoints |
| services | Business logic |
| repositories | Database operations |
| models | Database tables |
| schemas | Request/Response validation |
| providers | AI provider implementations |
| middleware | Request pipeline |
| dependencies | Dependency Injection |
| utils | Small reusable helper functions |

Never mix responsibilities between folders.

---

# 6. File Organization

A file should focus on one concept.

Good:

```text
user_service.py

chat_service.py

auth_service.py
```

Avoid:

```text
all_services.py

helpers.py

misc.py
```

Large files with unrelated logic become difficult to maintain.

---

# 7. Import Standards

Organize imports consistently.

Python order:

```python
# Standard library

import os
from datetime import datetime

# Third-party libraries

from fastapi import APIRouter

# Local modules

from app.services.user_service import UserService
```

TypeScript order:

```typescript
// External libraries

import React from "react";

// Internal modules

import { Button } from "@/components/ui/button";

// Local imports

import "./styles.css";
```

Avoid circular dependencies.

---

# 8. Code Formatting

Formatting should be automated.

Python:

- Black
- Ruff

TypeScript:

- Prettier
- ESLint

Never manually debate spacing or indentation.

Use automated formatters.

---

# 9. Function Standards

A function should:

- Perform one task.
- Have a clear name.
- Be concise.
- Return predictable results.
- Handle errors appropriately.

Prefer:

```python
create_user()

authenticate_user()

save_chat()
```

Avoid functions that perform multiple unrelated operations.

---

# 10. Class Standards

Each class should represent one responsibility.

Examples:

```text
UserService

ChatService

AIService

GeminiProvider
```

Avoid "God Classes" that manage authentication, database access, AI communication, and logging all at once.

---

# 11. API Route Standards

Routes should remain thin.

Responsibilities:

- Receive request
- Validate input
- Call service
- Return response

Routes should **not** contain:

- Business logic
- SQL queries
- AI calls
- Complex calculations

Example:

```text
Client
   ↓
Route
   ↓
Service
   ↓
Repository
```

---

# 12. Service Layer Standards

The Service Layer is the heart of the application.

Responsibilities:

- Business rules
- Workflow coordination
- Validation beyond schema checks
- Calling repositories
- Calling AI providers

Services should not know about HTTP request objects or frontend concerns.

---

# 13. Repository Standards

Repositories communicate with the database.

Responsibilities:

- CRUD operations
- Queries
- Transactions

Repositories should not contain business logic.

Example:

Good:

```python
get_user_by_email()
```

Bad:

```python
login_user()
```

Authentication belongs in the service layer.

---

# 14. Database Model Standards

Each model represents one database table.

Examples:

```text
User

Chat

Message
```

Models should define:

- Columns
- Relationships
- Constraints

Avoid placing business logic inside models.

---

# 15. Schema Standards

Schemas define the shape of data entering and leaving the API.

Use separate schemas for:

- Create requests
- Update requests
- Responses

Never expose database models directly through the API.

---

# 16. Error Handling Standards

Never expose internal errors to users.

Good response:

```json
{
    "detail": "Invalid credentials."
}
```

Avoid:

```text
Database connection failed on line 42...
```

Use custom exceptions where appropriate.

Handle expected errors gracefully.

---

# 17. Logging Standards

Log important events, not everything.

Examples:

- Application startup
- User login
- Failed authentication
- AI provider errors
- Database failures
- Unexpected exceptions

Do not log:

- Passwords
- JWT tokens
- API keys
- Sensitive personal information

Logs should assist debugging without compromising security.

---

# 18. Documentation & Comments

Code should generally explain itself through good naming.

Use comments only when they add value.

Comment:

- Why something is done.
- Complex business rules.
- Non-obvious decisions.

Avoid comments that simply repeat the code.

Bad:

```python
# Increment count
count += 1
```

Good:

```python
# Retry once to handle temporary provider rate limits.
```

Public functions and classes should include concise docstrings where helpful.

---

# 19. Clean Code Principles

We follow these Clean Code practices:

- Small functions
- Meaningful names
- Minimal nesting
- Early returns
- Consistent formatting
- No dead code
- No commented-out code
- No magic numbers (use named constants)
- Clear separation of concerns

Readable code is easier to maintain than clever code.

---

# 20. SOLID Principles

Our architecture follows the SOLID principles.

### Single Responsibility Principle (SRP)

Each class or module should have one reason to change.

---

### Open/Closed Principle (OCP)

Code should be open for extension but closed for modification.

Example:

Adding a new AI provider should involve creating a new provider class, not changing existing provider logic.

---

### Liskov Substitution Principle (LSP)

Any AI provider implementation should be interchangeable through the common provider interface.

---

### Interface Segregation Principle (ISP)

Components should depend only on the methods they actually use.

Avoid large interfaces with unrelated responsibilities.

---

### Dependency Inversion Principle (DIP)

High-level modules should depend on abstractions rather than concrete implementations.

For example, the AI service depends on a provider interface, not directly on Gemini or OpenAI.

---

# 21. DRY, KISS & YAGNI

### DRY (Don't Repeat Yourself)

Avoid duplicating logic.

Extract reusable functionality into shared components or services.

---

### KISS (Keep It Simple, Stupid)

Prefer the simplest solution that meets the requirements.

Do not introduce unnecessary complexity.

---

### YAGNI (You Aren't Gonna Need It)

Do not implement features until they are actually required.

Design for future expansion, but avoid building unused functionality prematurely.

---

# 22. Security Standards

Security is part of every layer.

Rules:

- Hash passwords.
- Validate all input.
- Never trust client-side data.
- Store secrets in environment variables.
- Use HTTPS in production.
- Sanitize user input.
- Protect private routes with JWT.
- Never expose internal implementation details in error messages.

Security should never be treated as an afterthought.

---

# 23. Testing Standards

Every important feature should be testable.

Tests should cover:

- Services
- Repositories
- API endpoints
- Authentication
- AI integrations (mocked)
- Validation logic

Testing ensures that future changes do not break existing functionality.

---

# 24. Common Mistakes

Avoid:

- Writing business logic inside API routes.
- Accessing the database directly from the frontend.
- Calling AI providers directly from routes.
- Creating large utility files with unrelated functions.
- Ignoring code formatting.
- Using inconsistent naming.
- Hardcoding configuration values.
- Duplicating logic across multiple files.
- Writing functions that perform too many tasks.
- Leaving unused or commented-out code in the repository.

Following the standards in this chapter helps prevent technical debt.

---

# 25. Chapter Summary

This chapter established the coding standards for the AI Research & Knowledge Assistant.

We defined conventions for naming, folder organization, file structure, formatting, imports, error handling, logging, documentation, security, and testing. We also adopted fundamental software engineering principles such as Clean Code, SOLID, DRY, KISS, and YAGNI.

These standards provide a consistent foundation for the entire codebase, ensuring that every contributor writes code in the same style and follows the same architectural principles. As the project grows, these guidelines will improve readability, reduce maintenance costs, and support the long-term scalability of the application.

---

## End of Chapter 8
