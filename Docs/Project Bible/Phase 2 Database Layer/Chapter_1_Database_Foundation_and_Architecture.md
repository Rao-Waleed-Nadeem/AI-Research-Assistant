# Phase 2 — Database Layer

# Chapter 1 — Database Foundation & Architecture

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 2 — Database Layer  
> **Chapter:** 1 — Database Foundation & Architecture

---

# Objective

The database is the permanent storage layer of our application.

Every major feature in this project depends on it:

- Authentication
- AI Chat
- Conversation History
- User Management
- Documents (Future)
- Embeddings (Future)
- RAG (Future)
- AI Agents (Future)
- Usage Analytics (Future)

Instead of allowing every module to communicate directly with PostgreSQL, we build a structured database layer following our backend architecture.

By the end of this chapter, we will have a scalable, maintainable, and production-ready database foundation that every future module will use.

---

# Chapter Deliverable

After completing this chapter:

- ✅ Database architecture is finalized.
- ✅ Database connection is centralized.
- ✅ SQLAlchemy integration is complete.
- ✅ Alembic migration workflow is established.
- ✅ Session management is standardized.
- ✅ Database folder structure is defined.
- ✅ Development workflow is documented.
- ✅ Database foundation is production-ready.

---

# Our Database Philosophy

Our database layer follows one simple principle:

> **The database stores application data. It never contains business logic.**

The database is responsible for:

- Persisting data
- Maintaining relationships
- Enforcing constraints
- Providing reliable storage

The database is **not** responsible for:

- Authentication logic
- AI communication
- Business rules
- API handling
- Response formatting

Those responsibilities belong to the Service Layer.

---

# Database Architecture

Our application follows this architecture.

```text
Frontend

↓

API Route

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy

↓

PostgreSQL
```

Every database operation follows this flow.

No layer is allowed to bypass another layer.

---

# Why This Architecture?

Instead of writing SQL inside API routes:

```text
Route

↓

SQL Query
```

We separate responsibilities.

```text
Route

↓

Service

↓

Repository

↓

Database
```

Benefits:

- Easier maintenance
- Cleaner code
- Better testing
- Reusable queries
- Consistent database access
- Better scalability

Every feature follows the same workflow.

---

# Database Technology Stack

Our database layer consists of three components.

```text
PostgreSQL

↓

SQLAlchemy

↓

Alembic
```

Each has a different responsibility.

---

## PostgreSQL

Purpose:

Permanent data storage.

Stores:

- Users
- Conversations
- Messages
- Future Documents
- Future Embeddings
- Future Agent Data
- Future Usage Statistics

Every important application record is stored here.

---

## SQLAlchemy

Purpose:

Acts as the communication layer between Python and PostgreSQL.

Instead of writing raw SQL throughout the project, SQLAlchemy manages:

- Models
- Queries
- Relationships
- Sessions
- Transactions

All repositories communicate with the database through SQLAlchemy.

---

## Alembic

Purpose:

Manage database schema changes.

Whenever we:

- Create a new table
- Modify a column
- Add an index
- Remove a constraint

Alembic tracks those changes through migrations.

Every developer stays synchronized with the same database structure.

---

# Complete Database Flow

Every database request follows this lifecycle.

```text
Frontend

↓

API Request

↓

API Route

↓

Service

↓

Repository

↓

SQLAlchemy Session

↓

PostgreSQL

↓

Repository

↓

Service

↓

Route

↓

Frontend
```

The Service never communicates directly with PostgreSQL.

The Route never communicates directly with SQLAlchemy.

The Repository is the only layer responsible for data access.

---

# Database Folder Structure

```text
backend/

app/

├── db/
│   ├── session.py
│   ├── base.py
│   ├── database.py
│   └── init_db.py
│
├── models/
│
├── repositories/
│
├── migrations/
│
└── alembic/
```

Each folder has one responsibility.

---

# Folder Responsibilities

---

## db/

Purpose:

Contains the entire database configuration.

Responsibilities:

- Database connection
- Session creation
- Base model
- Initialization
- Shared database utilities

This folder never contains business logic.

---

## models/

Purpose:

Defines database tables.

Every table in PostgreSQL has one corresponding model.

Examples:

```text
User

Conversation

Message

Document

Embedding

Agent
```

Models only describe database structure.

They do not contain business logic.

---

## repositories/

Purpose:

Communicate with PostgreSQL.

Repositories perform:

- Create
- Read
- Update
- Delete
- Search
- Filtering

No feature should query SQLAlchemy outside a repository.

---

## migrations/

Purpose:

Store migration history.

Every schema change generates one migration.

Example:

```text
Create Users Table

↓

Migration
```

Later:

```text
Add Conversation Table

↓

New Migration
```

Migration history allows every environment to stay synchronized.

---

## alembic/

Purpose:

Contains Alembic configuration files.

Responsibilities:

- Migration configuration
- Migration environment
- Migration execution

Developers rarely modify this folder directly.

---

# Database Connection Architecture

Database communication is centralized.

```text
Application

↓

Configuration

↓

Database Engine

↓

Session Factory

↓

Repositories

↓

PostgreSQL
```

Only one connection configuration exists.

Every repository uses the same session factory.

---

# Database Configuration

All database configuration comes from environment variables.

Examples:

```text
DATABASE_URL

DATABASE_HOST

DATABASE_PORT

DATABASE_NAME

DATABASE_USER

DATABASE_PASSWORD
```

Never hardcode connection information.

Configuration always comes from:

```text
.env

↓

Settings

↓

Database
```

---

# Database Initialization

Application startup follows this sequence.

```text
Application Starts

↓

Load Environment

↓

Load Settings

↓

Initialize Database Engine

↓

Create Session Factory

↓

Application Ready
```

Database initialization occurs only once during startup.

---

# SQLAlchemy Session Management

Every request receives its own database session.

Flow:

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

↓

Request Ends
```

Sessions should never remain open after the request finishes.

---

# Why One Session Per Request?

Benefits:

- Isolated transactions
- Better concurrency
- Cleaner resource management
- Automatic cleanup
- Fewer connection leaks

Every request is independent.

---

# Session Lifecycle

```text
Incoming Request

↓

Create Database Session

↓

Business Logic

↓

Repository Operations

↓

Commit Changes

↓

Close Session
```

If an exception occurs:

```text
Exception

↓

Rollback

↓

Close Session
```

This guarantees database consistency.

---

# Transaction Management

A transaction groups related database operations.

Example:

User Registration

```text
Create User

↓

Save User

↓

Commit
```

If something fails:

```text
Create User

↓

Error

↓

Rollback
```

No incomplete data remains in the database.

---

# Commit Strategy

Only commit after the complete operation succeeds.

Correct flow:

```text
Validate

↓

Process

↓

Save

↓

Commit
```

Never commit partial work.

---

# Rollback Strategy

Whenever an unexpected database error occurs:

```text
Database Error

↓

Rollback

↓

Return Error

↓

Close Session
```

Rollback restores the database to its previous consistent state.

---

# Database Migration Workflow

Whenever the database schema changes:

```text
Modify Model

↓

Generate Migration

↓

Review Migration

↓

Apply Migration

↓

Database Updated
```

Never modify the production database manually.

All schema changes should go through Alembic migrations.

---

# Development Workflow

Whenever a developer creates a new feature involving the database:

### Step 1

Create the model.

↓

### Step 2

Create the repository.

↓

### Step 3

Generate migration.

↓

### Step 4

Apply migration.

↓

### Step 5

Implement service logic.

↓

### Step 6

Expose API endpoint.

Following this order keeps the project organized and prevents inconsistencies.

---

# Database Communication Rules

Every module follows these rules.

---

## Rule 1

Routes never access the database directly.

---

## Rule 2

Services never execute SQL queries.

---

## Rule 3

Repositories are the only layer allowed to communicate with SQLAlchemy.

---

## Rule 4

Models only define database structure.

---

## Rule 5

Database configuration remains centralized.

---

## Rule 6

Every request uses a fresh database session.

---

## Rule 7

Always rollback on failure.

---

## Rule 8

Always close database sessions.

---

## Rule 9

Never hardcode database credentials.

---

## Rule 10

Every schema change must go through Alembic migrations.

---

# Future Database Growth

Although Version 1 starts with only a few tables, the architecture is designed for future expansion.

Future modules can add:

```text
Users

↓

Conversations

↓

Messages

↓

Documents

↓

Embeddings

↓

Knowledge Base

↓

AI Agents

↓

Usage Analytics

↓

Billing

↓

API Keys

↓

Audit Logs
```

No architectural changes will be required.

Only new models, repositories, and migrations will be added.

---

# Database Verification Checklist

Before moving to the next chapter, verify:

- ✅ PostgreSQL is configured.
- ✅ SQLAlchemy is connected.
- ✅ Alembic is configured.
- ✅ Database connection is centralized.
- ✅ Session management is implemented.
- ✅ Migration workflow is established.
- ✅ Folder responsibilities are clear.
- ✅ Repository is the only database access layer.
- ✅ Configuration comes from environment variables.
- ✅ Database follows project architecture.

---

# Database Foundation Summary

The database layer is now fully established.

```text
Database Foundation

├── PostgreSQL
├── SQLAlchemy
├── Alembic
├── Database Configuration
├── Database Connection
├── Session Management
├── Migration Workflow
├── Database Initialization
├── Repository Integration
└── Development Standards
```

This foundation will support every current and future feature of the project without requiring architectural changes.

---

# Deliverable

At the completion of Chapter 1:

- ✅ Database architecture is complete.
- ✅ Connection management is standardized.
- ✅ Session lifecycle is defined.
- ✅ Migration workflow is established.
- ✅ Development standards are documented.
- ✅ The backend has a scalable and production-ready database foundation ready for model design and implementation.

---

## End of Chapter 1 — Database Foundation & Architecture

**Next:** **Chapter 2 — Database Design & Models**, where we will design the complete schema for the application, including Users, Conversations, Messages, future AI-related tables, relationships, constraints, indexes, timestamps, and the workflow for adding new models while maintaining a clean and scalable database.