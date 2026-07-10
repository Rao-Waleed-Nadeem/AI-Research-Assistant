# Phase 2 — Database Layer

# Chapter 3 — Repository Layer & Database Operations

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 2 — Database Layer  
> **Chapter:** 3 — Repository Layer & Database Operations

---

# Objective

The Repository Layer is the only component responsible for communicating with PostgreSQL.

Instead of allowing Services or API Routes to execute database queries directly, all database operations pass through repositories.

This provides:

- Clean architecture
- Reusable database operations
- Easier maintenance
- Consistent query patterns
- Better testing
- Separation of concerns

By the end of this chapter, the complete database communication workflow for our project is established.

---

# Chapter Deliverable

After completing this chapter:

- ✅ Repository architecture is finalized.
- ✅ CRUD workflow is standardized.
- ✅ Database request flow is documented.
- ✅ Session lifecycle is implemented.
- ✅ Transaction management is defined.
- ✅ Error handling strategy is established.
- ✅ Repository development standards are documented.

---

# Repository Architecture

Our backend follows the same layered architecture everywhere.

```text
Frontend

↓

API Route

↓

Service

↓

Repository

↓

SQLAlchemy

↓

PostgreSQL
```

Each layer has one responsibility.

---

# Why Repository Layer Exists

Repositories isolate database operations from business logic.

Without Repository:

```text
Service

↓

SQL Query

↓

Database
```

Problems:

- Business logic mixed with queries
- Duplicate SQL
- Difficult testing
- Hard maintenance

With Repository:

```text
Service

↓

Repository

↓

Database
```

Benefits:

- Reusable queries
- Cleaner services
- Centralized database access
- Easier debugging
- Easier future changes

---

# Repository Responsibilities

Repositories are responsible only for data access.

They should:

- Create records
- Read records
- Update records
- Delete records
- Search records
- Filter records

Repositories should **never**:

- Validate business rules
- Generate JWT
- Call AI providers
- Handle HTTP requests
- Format API responses

---

# Repository Folder Structure

```text
app/

repositories/

├── user_repository.py
├── conversation_repository.py
├── message_repository.py
└── base_repository.py (optional)
```

Each repository manages one model.

---

# Repository Ownership

| Repository | Responsible For |
|------------|-----------------|
| UserRepository | Users |
| ConversationRepository | Conversations |
| MessageRepository | Messages |

Future repositories:

- DocumentRepository
- EmbeddingRepository
- AgentRepository
- UsageRepository

---

# Complete Database Request Flow

Every database operation follows the same workflow.

```text
Client

↓

API Request

↓

Route

↓

Service

↓

Repository

↓

Database

↓

Repository

↓

Service

↓

Route

↓

Response
```

No shortcuts.

Every feature follows this flow.

---

# CRUD Workflow

Every repository supports four fundamental operations.

```text
Create

Read

Update

Delete
```

Additional operations like search and filtering are built on top of these.

---

# Create Operation

Purpose:

Insert new records.

Example:

```text
Register User

↓

User Repository

↓

Insert User

↓

Commit
```

Only repositories create records.

---

# Read Operation

Purpose:

Retrieve information.

Examples:

```text
Find User

↓

Load Conversation

↓

Get Messages
```

Reading data should never modify the database.

---

# Update Operation

Purpose:

Modify existing records.

Example:

```text
Update Conversation Title

↓

Repository

↓

Commit Changes
```

Only the required fields should be updated.

---

# Delete Operation

Purpose:

Remove data.

Examples:

```text
Delete Conversation

↓

Delete Messages

↓

Commit
```

Deletion strategy should remain consistent across the project.

---

# Common Repository Operations

Besides CRUD, repositories commonly perform:

```text
Find By ID

↓

Find By Email

↓

List User Conversations

↓

Load Conversation Messages

↓

Search

↓

Pagination
```

Every frequently used query belongs inside the repository.

---

# Service and Repository Relationship

Services decide **what** should happen.

Repositories decide **how** data is stored or retrieved.

Example:

```text
Chat Service

↓

Create Conversation

↓

Conversation Repository

↓

Database
```

The Service never writes SQLAlchemy queries.

---

# Session Lifecycle

Every request receives its own database session.

```text
Request Starts

↓

Create Session

↓

Repository Uses Session

↓

Commit or Rollback

↓

Close Session
```

Sessions must never be shared between requests.

---

# Transaction Workflow

Successful transaction:

```text
Start Session

↓

Execute Query

↓

Commit

↓

Close Session
```

Failed transaction:

```text
Start Session

↓

Execute Query

↓

Exception

↓

Rollback

↓

Close Session
```

This ensures database consistency.

---

# Query Guidelines

Repositories should write queries that are:

- Simple
- Readable
- Reusable
- Efficient

Avoid unnecessary complexity.

If a query becomes too large, split it into reusable helper methods.

---

# Pagination Strategy

Some tables will continue growing.

Examples:

- Messages
- Conversations
- Usage Logs

Never return unlimited records.

Instead:

```text
Client

↓

Page Number

↓

Repository

↓

Limited Records

↓

Response
```

Pagination improves performance and reduces response size.

---

# Database Error Handling

Database errors should be handled inside the Service layer after being raised by repositories.

Example flow:

```text
Repository

↓

Database Exception

↓

Service

↓

Rollback

↓

Global Exception Handler

↓

API Response
```

Repositories should not generate HTTP responses.

---

# Common Database Errors

Examples include:

- Record not found
- Duplicate email
- Foreign key violation
- Constraint violation
- Connection failure

Services determine how these errors affect business logic.

---

# Repository Development Workflow

Whenever a new feature requires database access:

```text
Create Model

↓

Create Repository

↓

Implement CRUD

↓

Create Service

↓

Expose Route

↓

Test Feature
```

Every module follows the same workflow.

---

# Adding a New Repository

When introducing a new entity:

Example:

```text
Document
```

Development order:

```text
Model

↓

Migration

↓

Repository

↓

Service

↓

API

↓

Frontend
```

Never skip the Repository layer.

---

# Repository Best Practices

### Keep One Repository Per Model

Correct:

```text
User Repository

Conversation Repository

Message Repository
```

Avoid mixing unrelated entities.

---

### Keep Methods Small

Each method should perform one task.

Good examples:

```text
get_user_by_email()

create_user()

get_conversation()

delete_message()
```

Avoid methods that perform multiple unrelated operations.

---

### Reuse Existing Methods

If a query already exists, reuse it.

Avoid duplicate implementations.

---

### Keep Business Logic Out

Incorrect:

```text
Repository

↓

Validate Password

↓

Generate JWT
```

Correct:

```text
Repository

↓

Database Only
```

---

# Repository Rules

### Rule 1

Only repositories communicate with SQLAlchemy.

---

### Rule 2

Services never execute SQL queries.

---

### Rule 3

Routes never communicate with repositories directly.

---

### Rule 4

One repository manages one model.

---

### Rule 5

Repositories never contain business logic.

---

### Rule 6

Repositories never call AI providers.

---

### Rule 7

Repositories never generate API responses.

---

### Rule 8

Keep methods reusable.

---

### Rule 9

Always use dependency-injected database sessions.

---

### Rule 10

Close every database session after request completion.

---

# Repository Checklist

Whenever creating a new repository, verify:

- Model already exists.
- Migration has been applied.
- CRUD methods implemented.
- Queries are reusable.
- Business logic is absent.
- Session is dependency-injected.
- Transactions handled correctly.
- Exceptions propagate correctly.

---

# Complete Database Communication Architecture

```text
Frontend

↓

FastAPI Route

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy Session

↓

PostgreSQL

↓

Repository

↓

Service

↓

API Route

↓

Frontend
```

This architecture will remain unchanged throughout the project.

Future modules—including AI Chat, Document Management, Embeddings, RAG, AI Agents, and Billing—will all follow this exact communication pattern.

---

# Phase 2 Summary

After completing Phase 2, the project has a complete database layer.

```text
Database Layer

├── PostgreSQL Integration
├── SQLAlchemy Configuration
├── Alembic Migration Workflow
├── Database Session Management
├── Database Models
├── Relationships
├── Constraints
├── Indexes
├── Repository Layer
├── CRUD Operations
├── Transaction Management
├── Error Handling
└── Development Standards
```

The database architecture is now stable, scalable, and ready to support all future application features.

---

# Deliverable

At the end of Phase 2:

- ✅ Database foundation is complete.
- ✅ Core schema is implemented.
- ✅ Repository pattern is established.
- ✅ Database communication follows Clean Architecture.
- ✅ CRUD standards are defined.
- ✅ Transaction and session management are standardized.
- ✅ The project is ready to build business features on top of a production-ready database layer.

---

## End of Phase 2 — Database Layer

**Next Phase:** **Phase 3 — Project Architecture**, where we will document how all backend components work together, including layered architecture, dependency injection, configuration management, request/response lifecycle, feature development workflow, and project-wide engineering standards.