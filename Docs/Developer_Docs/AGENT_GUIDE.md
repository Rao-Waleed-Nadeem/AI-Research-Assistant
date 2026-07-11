# AGENT_GUIDE.md

# AI Research Assistant

## Agent Development Guide

> Version: 1.0
>
> This document is the primary instruction manual for any AI coding agent working on this project.
>
> Read this document completely before writing or modifying any code.
>
> If any instruction here conflicts with another document, this document takes precedence unless explicitly overridden by the Project Bible.

---

# 1. Project Overview

This project is an industry-standard AI SaaS application built to learn and implement modern AI engineering practices while producing a production-ready product.

The objective is not only to make the application functional but to build it using clean architecture, scalable design, reusable components, and production-ready development practices.

The project follows a layered backend architecture using FastAPI and a provider-independent AI layer.

Future phases include:

- Authentication
- Chat
- AI Providers
- Conversations
- Document Upload
- Embeddings
- Vector Database
- RAG
- AI Agents
- Multi-Agent Workflows
- Docker
- AWS Deployment
- Production Engineering

The architecture must remain extensible throughout all phases.

---

# 2. Source of Truth

The documentation hierarchy is:

1. AGENT_GUIDE.md (Current document)
2. Feature Specification
3. Project Bible
4. Existing Source Code

Never assume project behavior.

If information is missing:

- Check the Project Bible.
- Follow existing architecture.
- Never invent a new architecture.

---

# 3. Project Philosophy

Always optimize for:

- Readability
- Scalability
- Maintainability
- Reusability
- Simplicity
- Industry standards

Do not optimize for writing the fewest lines of code.

Do not introduce shortcuts that reduce maintainability.

---

# 4. Architecture Rules

The project follows layered architecture.

Request Flow

Frontend

↓

Route

↓

Service

↓

Repository

↓

Database

AI Flow

Frontend

↓

Route

↓

Chat Service

↓

AI Service

↓

Provider Factory

↓

Provider

↓

LLM

No layer may bypass another layer.

---

# 5. Layer Responsibilities

## Routes

Responsible for:

- Receiving requests
- Authentication
- Validation
- Calling Services
- Returning responses

Routes must never contain:

- SQL
- Business logic
- AI logic

---

## Services

Responsible for:

- Business logic
- Application workflow
- Coordination between repositories and providers

Services must never:

- Write SQL
- Access external APIs directly
- Return raw database models

---

## Repositories

Responsible for:

- Database communication only

Repositories must never:

- Call AI
- Implement business logic
- Perform authentication

---

## Providers

Responsible for:

- Communicating with external AI providers

Providers must never:

- Access database
- Implement business rules

---

## Schemas

Responsible for:

- Validation
- Serialization
- API contracts

---

# 6. Folder Rules

Every file must have one responsibility.

Never place unrelated logic inside a file.

Prefer creating a new module over making an existing file excessively large.

---

# 7. Coding Rules

Always

- Use type hints
- Validate input
- Return standardized responses
- Handle exceptions
- Write reusable functions
- Use dependency injection
- Follow existing project structure

Never

- Duplicate code
- Hardcode secrets
- Skip validation
- Skip services
- Skip repositories
- Skip providers

---

# 8. Development Workflow

Every new feature must follow this order.

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

Registration

↓

Testing

Never change this order.

---

# 9. Feature Development Workflow

Before implementing any new feature:

Step 1

Read:

- AGENT_GUIDE.md
- IMPLEMENTATION_ORDER.md
- PROJECT_STATUS.md

Step 2

Determine the current feature.

Step 3

If a Feature Specification does not exist:

Automatically generate

FEATURE\_<FEATURE_NAME>.md

using:

- Project Bible
- Existing code
- Current architecture

The Feature Specification should contain:

- Objective
- Folder structure
- Files to create
- Dependencies
- Database changes
- API endpoints
- Schemas
- Models
- Repositories
- Services
- Routes
- Validation
- Testing checklist

Save the specification before implementing code.

Step 4

Implement only that feature.

Step 5

Update PROJECT_STATUS.md.

Stop.

Never continue implementing unrelated features.

---

# 10. Feature Boundaries

Implement only the requested feature.

Do not begin another feature.

Do not refactor unrelated modules unless required.

Do not modify existing architecture without explanation.

---

# 11. Code Quality Standards

Code should be:

- Modular
- Readable
- Consistent
- Typed
- Testable

Avoid:

- Large functions
- Large classes
- Circular dependencies
- Duplicate logic

---

# 12. AI Provider Rules

All AI communication must pass through:

AI Service

↓

Provider Factory

↓

Provider

Never call providers directly.

---

# 13. Database Rules

All database access must pass through repositories.

Routes never access database.

Services never execute SQL.

---

# 14. Documentation Rules

Whenever a feature is completed:

Update:

PROJECT_STATUS.md

Include:

- Completed files
- Remaining work
- Notes
- Known issues
- Next feature

If architecture changes:

Update the relevant Project Bible chapter.

---

# 15. Git Rules

Commit only after a logical unit of work.

Examples

Good

feat(auth): implement login endpoint

Good

feat(chat): add conversation repository

Bad

update

Bad

changes

---

# 16. Before Finishing Any Task

Verify:

- Architecture followed
- Coding standards followed
- Folder structure maintained
- Validation implemented
- Errors handled
- Documentation updated
- PROJECT_STATUS.md updated

Only then consider the task complete.

---

# 17. Current Project Status

The implementation order is defined in:

IMPLEMENTATION_ORDER.md

The current progress is defined in:

PROJECT_STATUS.md

Always consult these documents before implementing code.

---

# 18. Final Rule

This project prioritizes long-term maintainability over rapid implementation.

Whenever uncertain:

Choose the solution that is:

- Simpler
- More reusable
- Easier to extend
- Consistent with existing architecture

Never sacrifice architecture for convenience.
