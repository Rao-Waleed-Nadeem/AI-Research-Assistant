# Phase 1 — Backend Foundations

# Chapter 2 — Backend Core Architecture

## Part 2 — Request Lifecycle & Architectural Layers

> Version: 1.0
>
> Status: Completed
>
> Phase: 1 — Backend Foundations
>
> Chapter: 2 — Backend Core Architecture
>
> Part: 2

---

# Objective

In Part 1, we defined **where code belongs**.

In this part, we will understand **how the code works together**.

This is one of the most important concepts in the entire project because every feature—from Authentication to AI Chat, RAG, Agents, Billing, and Document Processing—will follow the exact same execution flow.

If you understand this chapter, you'll always know:

- Where a request starts.
- What each layer does.
- Which layer owns which responsibility.
- Where new code should be added.
- How the frontend communicates with the backend.
- How the backend communicates with AI providers and the database.

---

# Our Request Lifecycle

Almost every request in our application follows this flow:

```text
                 Frontend
                     │
                     ▼
               API Route Layer
                     │
                     ▼
               Service Layer
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
 Repository Layer          AI Service
         │                       │
         ▼                       ▼
 PostgreSQL Database       AI Provider
                                  │
                                  ▼
                              Gemini
```

Now let's understand every layer.

---

# Step 1 — Frontend

The frontend is the **client**.

Its responsibilities are intentionally limited.

The frontend should:

- Display UI
- Collect user input
- Validate basic input for user experience
- Send API requests
- Display responses

The frontend **must not**:

- Execute SQL
- Know database structure
- Call Gemini directly
- Implement business rules
- Make security decisions

Example:

User types:

> "Explain Machine Learning."

The frontend simply sends:

```http
POST /api/v1/chat/message
```

with the message.

The frontend does not decide:

- How prompts are built.
- Which AI provider to use.
- How conversations are stored.

Those decisions belong to the backend.

---

# Step 2 — API Route Layer

The Route Layer is the **entry point** of the backend.

Every request arrives here first.

Example:

```text
Frontend

↓

POST /chat/message

↓

Chat Route
```

The Route Layer has four responsibilities only.

## Responsibility 1

Receive the request.

Example:

```text
POST /chat/message
```

---

## Responsibility 2

Validate incoming data.

Validation happens using Schemas.

Example:

```text
Message cannot be empty.

Conversation ID is required.

User must be authenticated.
```

---

## Responsibility 3

Call the appropriate Service.

Example:

```text
Chat Route

↓

Chat Service
```

The route should never contain business logic.

---

## Responsibility 4

Return the response.

Example:

```json
{
  "success": true,
  "data": {
    "response": "..."
  }
}
```

Nothing more.

---

# What Routes Must Never Do

Routes must never:

- Query PostgreSQL
- Call Gemini
- Hash passwords
- Create JWTs
- Save files
- Process prompts
- Perform calculations
- Implement business rules

If a route starts becoming large, logic belongs somewhere else.

Routes should remain thin.

---

# Step 3 — Service Layer

The Service Layer is the **brain** of our application.

Almost every important decision happens here.

Think of Services as managers.

They coordinate work but don't directly store data or communicate with external systems.

Example:

```text
Chat Service
```

Responsibilities:

- Validate business rules.
- Decide workflow.
- Call repositories.
- Call AI services.
- Combine data.
- Return final result.

---

# Example Workflow

User sends:

```
Explain Transformers.
```

Chat Service decides:

```text
1. Verify conversation exists.

↓

2. Save user message.

↓

3. Send prompt to AI Service.

↓

4. Receive AI response.

↓

5. Save AI response.

↓

6. Return response.
```

Notice:

The Service Layer coordinates everything.

---

# Why Services Exist

Without services:

```text
Route

↓

Database

↓

Gemini

↓

Database

↓

JWT

↓

Files

↓

Response
```

Every route becomes huge.

Duplicated code appears.

Testing becomes difficult.

Maintenance becomes painful.

Instead:

```text
Route

↓

Service

↓

Everything else
```

Simple.

Clean.

Reusable.

---

# Step 4 — Repository Layer

Repositories communicate with PostgreSQL.

Nothing else.

Responsibilities:

- Create records
- Read records
- Update records
- Delete records
- Execute queries

Repositories should never:

- Generate JWT
- Call Gemini
- Build prompts
- Send emails
- Decide business rules

Example:

```
UserRepository
```

Functions might include:

```
create_user()

get_user_by_email()

update_user()

delete_user()
```

Notice how every function is database-related.

---

# Why Repository Pattern

Imagine we need user information.

Without Repository:

```text
Chat Service

↓

SQL Query
```

Now SQL exists inside Services.

Another Service also writes SQL.

Soon SQL appears everywhere.

Maintenance becomes difficult.

Instead:

```text
Chat Service

↓

User Repository

↓

Database
```

SQL stays in one place.

Services remain clean.

---

# Step 5 — Database

The database stores permanent information.

Examples:

- Users
- Chats
- Messages
- Sessions
- Settings
- Usage
- Tokens

The database never:

- Talks to Gemini.
- Knows HTTP.
- Knows Routes.

It only stores data.

---

# Complete Database Flow

```text
Frontend

↓

Route

↓

Service

↓

Repository

↓

PostgreSQL
```

Response returns through the exact same path.

---

# AI Request Lifecycle

Not every request needs the database.

Some require AI.

Those requests follow another branch.

```text
Frontend

↓

API Route

↓

Service

↓

AI Service

↓

Provider

↓

Gemini

↓

AI Response

↓

Service

↓

Route

↓

Frontend
```

---

# Why AI Service Exists

Suppose every Route called Gemini directly.

Later we switch to OpenAI.

Every route changes.

Suppose later we support Groq.

More routes change.

Soon the project becomes impossible to maintain.

Instead:

```text
Route

↓

Chat Service

↓

AI Service

↓

Provider

↓

Gemini
```

Routes never know which provider is being used.

---

# Why Provider Exists

Providers isolate vendor-specific code.

Example:

```
GeminiProvider

OpenAIProvider

GroqProvider

OpenRouterProvider

OllamaProvider
```

Every provider exposes the same interface.

Example:

```
generate_response()

generate_embedding()

count_tokens()
```

Internally they behave differently.

Externally they behave identically.

This is called **Provider Abstraction**.

---

# Complete AI Flow

```text
User

↓

Frontend

↓

Chat Route

↓

Chat Service

↓

AI Service

↓

Gemini Provider

↓

Gemini API

↓

Gemini Provider

↓

AI Service

↓

Chat Service

↓

Chat Route

↓

Frontend
```

Notice something important.

The Chat Route never knows Gemini exists.

---

# Why Schemas Exist

Schemas define the language spoken between:

Frontend

↓

Backend

They ensure:

- Input validation
- Response consistency
- Automatic documentation

Example:

Frontend sends:

```json
{
    "message": "Hello"
}
```

Schema verifies:

- Field exists.
- Type is correct.
- Length is acceptable.
- Required values are present.

If validation fails:

The request stops immediately.

It never reaches the Service Layer.

This protects the application from invalid data.

---

# Why Dependencies Exist

Dependencies provide reusable functionality across multiple routes.

Examples in our project:

```
Current User

Database Session

Admin Access

Premium User Check

Rate Limiter (Future)
```

Instead of repeating code:

```
Verify JWT

Verify JWT

Verify JWT

Verify JWT
```

We write it once.

Every protected route reuses it.

Benefits:

- Less duplication.
- Easier maintenance.
- Consistent security.
- Cleaner routes.

---

# Complete Responsibility Matrix

| Layer | Responsible For | Never Responsible For |
|---------|----------------|-----------------------|
| Frontend | UI & API requests | Business logic, database, AI |
| API Route | Receive request, validate, call Service, return response | Business logic, SQL, AI |
| Service | Business rules and workflow | HTTP handling, SQL implementation |
| Repository | Database operations | Business rules, AI |
| Database | Data storage | Business logic |
| AI Service | AI orchestration | HTTP handling |
| Provider | Provider-specific implementation | Business rules |
| Schema | Validation & serialization | Database operations |
| Dependency | Shared reusable functionality | Business workflows |

---

# Architectural Communication Rules

Only these communication paths are allowed:

```
Frontend

↓

Route

↓

Service

↓

Repository
```

and

```
Service

↓

AI Service

↓

Provider
```

Anything else is considered an architecture violation.

---

# Architecture Violations

The following are **strictly prohibited**:

❌ Frontend → Database

❌ Frontend → Gemini

❌ Route → Database

❌ Route → Gemini

❌ Repository → Gemini

❌ Provider → Database

❌ Repository → Repository

❌ Route → Repository (bypassing Service)

❌ Service → SQL directly

Every layer communicates only with the layer immediately below it, unless explicitly designed otherwise.

---

# Development Checklist

Whenever you implement a new feature, verify:

- Does the request enter through a Route?
- Does the Route call a Service?
- Does the Service coordinate the workflow?
- Are database operations delegated to a Repository?
- Are AI requests delegated to the AI Service?
- Does the AI Service communicate through a Provider?
- Are Schemas validating input and output?
- Are shared concerns implemented as Dependencies?

If the answer to all is **Yes**, the implementation follows the project architecture.

---

# Checkpoint

By the end of Part 2, you should clearly understand:

- How every request flows through the backend.
- Why each architectural layer exists.
- What responsibilities belong to each layer.
- Which communication paths are allowed.
- Which architectural shortcuts are forbidden.

This request lifecycle is the foundation that every future module in the project will follow.

---

## End of Chapter 2 — Part 2
