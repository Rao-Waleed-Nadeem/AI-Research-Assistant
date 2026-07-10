# Phase 2 — Database Layer

# Chapter 2 — Database Design & Models

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 2 — Database Layer  
> **Chapter:** 2 — Database Design & Models

---

# Objective

This chapter designs the complete database schema for our AI SaaS application.

Instead of creating tables randomly as features are developed, we first establish a well-planned schema that supports both the current implementation and future expansion.

Our Version 1 implements only the required tables, while keeping the architecture ready for future modules such as Documents, Embeddings, RAG, AI Agents, Usage Analytics, and Billing.

---

# Chapter Deliverable

After completing this chapter:

- ✅ Complete database schema is finalized.
- ✅ Relationships are clearly defined.
- ✅ Naming conventions are standardized.
- ✅ Database constraints are established.
- ✅ Indexing strategy is documented.
- ✅ Future scalability is planned.

---

# Database Design Philosophy

Our database follows these principles:

- One table = One responsibility
- Avoid duplicate data
- Store only necessary information
- Keep relationships simple
- Design for scalability
- Never store computed business logic
- Keep AI providers independent from database structure

Every table should represent a real business entity.

---

# Current Database Architecture

Version 1 contains three core tables.

```text
Users

↓

Conversations

↓

Messages
```

Relationship:

```text
User

1

↓

Many

Conversation

1

↓

Many

Message
```

This architecture is sufficient for:

- Authentication
- AI Chat
- Conversation History
- Chat Management

Everything else will extend this structure.

---

# Complete Database Schema

```text
Users
│
├── Conversations
│       │
│       └── Messages
│
├── Documents (Future)
│
├── Embeddings (Future)
│
├── AI Agents (Future)
│
├── Usage Logs (Future)
│
└── Billing (Future)
```

The database is intentionally designed so future modules integrate naturally.

---

# Table 1 — Users

Purpose:

Stores registered users.

Every feature in the application begins with a user.

---

## Responsibilities

The Users table stores:

- Account information
- Authentication data
- Account status
- Creation timestamps

It does **not** store:

- Chat history
- AI responses
- Documents
- Tokens
- Business logic

---

## Core Fields

```text
id

full_name

email

password_hash

is_active

created_at

updated_at
```

---

## Relationships

```text
User

↓

Many Conversations
```

Future:

```text
User

↓

Many Documents

↓

Many Agents

↓

Many Usage Logs
```

---

## Constraints

- Primary Key
- Email must be unique
- Email cannot be null
- Password hash cannot be null

---

## Indexes

Create indexes on:

```text
email
```

Reason:

Login searches users by email.

Without an index:

```text
Slow Search
```

With an index:

```text
Fast Lookup
```

---

# Table 2 — Conversations

Purpose:

Represents one chat session between the user and the AI.

Instead of storing every message directly under a user, messages are grouped into conversations.

Example:

```text
User

↓

Conversation

↓

Many Messages
```

This structure supports unlimited chat sessions.

---

## Responsibilities

Conversation stores:

- Conversation ownership
- Conversation title
- Creation date
- Update date

It does **not** store:

- AI messages
- User messages
- Embeddings

---

## Core Fields

```text
id

user_id

title

created_at

updated_at
```

---

## Relationships

```text
Conversation

↓

Belongs To

↓

User
```

```text
Conversation

↓

Contains

↓

Many Messages
```

---

## Constraints

- Primary Key
- Foreign Key → User
- Required User ID

---

## Indexes

Indexes:

```text
user_id
```

Reason:

Most conversation queries filter by user.

Example:

```
Show all conversations for User X.
```

---

# Table 3 — Messages

Purpose:

Stores every message exchanged during a conversation.

Both user prompts and AI responses are stored here.

---

## Responsibilities

Stores:

- Message content
- Sender
- Conversation
- Timestamp

Does not store:

- User account information
- Conversation metadata

---

## Core Fields

```text
id

conversation_id

role

content

created_at
```

---

## Message Role

Role identifies who created the message.

Possible values:

```text
user

assistant

system
```

Future AI features can use system messages for prompt engineering.

---

## Relationships

```text
Message

↓

Belongs To

↓

Conversation
```

---

## Constraints

- Primary Key
- Foreign Key → Conversation
- Content required
- Role required

---

## Indexes

Indexes:

```text
conversation_id
```

Reason:

Every chat loads messages by conversation.

---

# Relationship Diagram

```text
User

1

↓

Many

Conversation

1

↓

Many

Message
```

This relationship remains unchanged even when future features are added.

---

# Future Tables

These tables are **not implemented now**, but the architecture is prepared for them.

---

## Documents

Purpose:

Store uploaded files.

Relationship:

```text
User

↓

Many Documents
```

---

## Embeddings

Purpose:

Store vector embeddings generated from documents.

Relationship:

```text
Document

↓

Many Embeddings
```

---

## Knowledge Base

Purpose:

Connect uploaded documents with AI retrieval.

Relationship:

```text
User

↓

Knowledge Base

↓

Documents

↓

Embeddings
```

---

## AI Agents

Purpose:

Store user-created AI assistants.

Relationship:

```text
User

↓

Many Agents
```

---

## Usage Logs

Purpose:

Track:

- AI requests
- Token usage
- Cost
- Model usage

Useful for analytics and billing.

---

## Billing

Purpose:

Store:

- Subscription
- Payment history
- Credits

Future premium features will depend on this table.

---

# Foreign Key Strategy

Every child table references its parent.

Example:

```text
Conversation

↓

user_id

↓

Users.id
```

```text
Message

↓

conversation_id

↓

Conversations.id
```

This guarantees data integrity.

---

# Cascade Strategy

When a user is deleted:

```text
User

↓

Delete Conversations

↓

Delete Messages
```

This prevents orphaned records.

Future child tables should follow the same cascade strategy where appropriate.

---

# Timestamp Strategy

Every primary entity should contain:

```text
created_at

updated_at
```

Benefits:

- Sorting
- Auditing
- History
- Analytics

Messages only require:

```text
created_at
```

because message content is immutable in our application.

---

# Naming Conventions

Tables:

Plural.

Examples:

```text
users

conversations

messages
```

Columns:

Snake case.

Examples:

```text
user_id

created_at

password_hash
```

Foreign Keys:

Always end with:

```text
_id
```

Examples:

```text
user_id

conversation_id
```

Consistency improves readability and reduces confusion.

---

# Data Ownership

Every record should have a clear owner.

Example:

```text
User

↓

Conversation

↓

Message
```

Future:

```text
User

↓

Document

↓

Embedding
```

No table should contain ambiguous ownership.

---

# Adding a New Model

Whenever a new feature requires storage, follow this workflow.

```text
Identify Entity

↓

Design Model

↓

Define Relationships

↓

Add Constraints

↓

Add Indexes

↓

Create Migration

↓

Implement Repository

↓

Implement Service

↓

Expose API
```

Never create tables without following this process.

---

# Model Design Rules

### Rule 1

One model represents one entity.

---

### Rule 2

Never duplicate data.

---

### Rule 3

Use foreign keys instead of repeated values.

---

### Rule 4

Store timestamps.

---

### Rule 5

Index frequently searched fields.

---

### Rule 6

Keep relationships simple.

---

### Rule 7

Business logic belongs in Services, not Models.

---

### Rule 8

Models should only describe database structure.

---

# Database Growth Strategy

Current Version:

```text
Users

↓

Conversations

↓

Messages
```

Future:

```text
Users

├── Conversations
│      └── Messages
│
├── Documents
│      └── Embeddings
│
├── Agents
│
├── Usage Logs
│
└── Billing
```

Notice that every new module connects naturally to the existing schema without redesigning the database.

---

# Chapter Checklist

Before moving to the next chapter, verify:

- ✅ User model finalized.
- ✅ Conversation model finalized.
- ✅ Message model finalized.
- ✅ Relationships defined.
- ✅ Foreign keys documented.
- ✅ Constraints established.
- ✅ Indexes identified.
- ✅ Naming conventions standardized.
- ✅ Future tables planned.
- ✅ Database remains scalable.

---

# Database Schema Summary

```text
Users

├── id
├── full_name
├── email
├── password_hash
├── is_active
├── created_at
└── updated_at

        │

        ▼

Conversations

├── id
├── user_id
├── title
├── created_at
└── updated_at

        │

        ▼

Messages

├── id
├── conversation_id
├── role
├── content
└── created_at
```

This schema forms the foundation for every feature developed in the remaining phases of the project.

---

# Deliverable

At the completion of Chapter 2:

- ✅ Database schema is finalized.
- ✅ Core entities are designed.
- ✅ Relationships are established.
- ✅ Constraints and indexes are defined.
- ✅ Future AI modules are accommodated without structural changes.

The project now has a clean, scalable, and extensible database design ready for implementation.

---

## End of Chapter 2 — Database Design & Models

**Next:** **Chapter 3 — Repository Layer & Database Operations**, where we will implement the Repository pattern, CRUD standards, session lifecycle, transaction handling, query guidelines, database error handling, and development workflow used by every feature in the project.