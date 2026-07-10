# Phase 1 — Backend Foundations

# Chapter 4 — Authentication Foundation

## Part 1 — Authentication Architecture

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 1 — Backend Foundations  
> **Chapter:** 4 — Authentication Foundation  
> **Part:** 1

---

# Objective

Authentication is the first real business feature of our application.

Its purpose is to ensure that every request is associated with a verified user before that user can access protected resources such as chats, documents, AI requests, and future premium features.

By the end of this chapter we will have a complete authentication architecture that every secured module in the project will use.

---

# Expected Outcome

After completing this part:

- User model is designed.
- Authentication architecture is finalized.
- Password storage strategy is defined.
- JWT architecture is defined.
- Authentication request flow is established.
- Authentication folder structure is ready.

Implementation of APIs will be covered in the next part.

---

# Why Authentication Comes First

Almost every feature in our application depends on knowing **who the current user is**.

Examples:

```
Chat

↓

Which user's conversation?
```

```
Documents

↓

Who uploaded them?
```

```
History

↓

Which user's history?
```

```
Billing (Future)

↓

Which subscription?
```

```
RAG

↓

Which user's knowledge base?
```

Without authentication, the application cannot safely associate data with the correct user.

---

# Authentication Scope

Authentication is responsible only for identity verification.

It answers one question:

> **Who is making this request?**

It is **not** responsible for:

- Business logic
- AI communication
- Database queries (except user lookup)
- Authorization policies
- Subscription validation

Each responsibility belongs to a different layer.

---

# Authentication Architecture

Authentication follows the same architecture established in Chapter 2.

```text
Frontend

↓

Auth Route

↓

Auth Service

↓

User Repository

↓

PostgreSQL
```

When authentication succeeds:

```text
Auth Service

↓

JWT Service

↓

Generate Token

↓

Frontend
```

Every component has a single responsibility.

---

# Authentication Folder Structure

Authentication is distributed across the existing architecture.

```text
app/

├── api/
│     └── auth.py
│
├── services/
│     └── auth_service.py
│
├── repositories/
│     └── user_repository.py
│
├── models/
│     └── user.py
│
├── schemas/
│     └── auth_schema.py
│
├── dependencies/
│     └── current_user.py
│
└── core/
      └── security.py
```

Notice that we **do not** create an `authentication/` folder.

Authentication is implemented using the project's layered architecture.

---

# User Model

The User model represents every registered account.

Every authenticated feature ultimately depends on this model.

Initially, our application only needs the following information:

```text
User

├── id

├── full_name

├── email

├── password_hash

├── is_active

├── created_at

└── updated_at
```

Additional fields can be introduced later without changing the authentication architecture.

Examples:

- Profile picture
- Subscription
- Preferences
- Theme
- Timezone

---

# Why Store Email?

Email serves as the primary login identifier.

Requirements:

- Unique
- Required
- Indexed
- Case-insensitive during authentication

Every login request begins by locating the user using their email.

---

# Why Store Password Hash Instead of Password?

The application **never stores plaintext passwords**.

Instead:

```text
User Password

↓

Hash

↓

Database
```

If the database is compromised:

Attackers obtain only password hashes, not actual passwords.

This is a fundamental security requirement.

---

# Password Hashing

Password hashing converts a password into a secure one-way value.

Authentication flow:

```text
User Password

↓

Hash Password

↓

Store Hash
```

During login:

```text
Entered Password

↓

Hash Verification

↓

Stored Hash

↓

Match?

↓

Success / Failure
```

Notice:

The original password is never recovered.

It is only verified.

---

# Password Hashing Rules

Passwords must always be:

- Hashed before storage.
- Verified using the hashing library.
- Never decrypted.
- Never logged.
- Never returned in API responses.

Every password operation is handled inside the Authentication Service.

---

# Security Module

Password hashing belongs inside:

```text
app/

core/

security.py
```

Responsibilities:

- Hash passwords.
- Verify passwords.
- Generate JWT.
- Validate JWT.

Keeping security operations centralized avoids duplication.

---

# JWT Authentication

After successful login, the backend creates a JSON Web Token (JWT).

Instead of asking the user to log in before every request:

```
Login Once

↓

Receive JWT

↓

Reuse JWT
```

This enables stateless authentication.

---

# JWT Architecture

Authentication flow:

```text
User

↓

Login

↓

Verify Password

↓

Generate JWT

↓

Frontend

↓

Protected Request

↓

Verify JWT

↓

Access Granted
```

JWT becomes the proof that the user has already authenticated.

---

# JWT Contents

Our token contains only the information required to identify the user.

Typical contents include:

```text
User ID

Email

Expiration Time
```

Avoid storing:

- Password
- Personal information
- API Keys
- Permissions
- Subscription details

The token should remain lightweight.

---

# Token Lifetime

Every JWT has an expiration time.

```text
Login

↓

JWT Created

↓

Valid Period

↓

Expires

↓

Login Again
```

Expired tokens are rejected automatically.

The expiration duration is configurable through the centralized settings.

---

# Authentication Flow

Complete authentication process:

```text
User

↓

Enter Email

↓

Enter Password

↓

Frontend

↓

POST /api/v1/auth/login

↓

Auth Route

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

Return Token

↓

Frontend Stores Token

↓

Future Requests

↓

Authorization Header

↓

Authenticated
```

This flow will remain unchanged throughout the project.

---

# Authentication Request Types

Our authentication module exposes two categories of endpoints.

## Public Endpoints

Accessible without authentication.

Examples:

```text
Register

Login

Health
```

---

## Protected Endpoints

Require a valid JWT.

Examples:

```text
Current User

Chat

Documents

Conversation History

AI Requests

Future Premium Features
```

The authentication system decides which category each endpoint belongs to.

---

# Current User Dependency

Every protected request needs to know **who the current user is**.

Instead of manually verifying the JWT in every route:

```text
Chat Route

↓

Verify JWT

↓

Get User

↓

Continue
```

We use a shared dependency.

Flow:

```text
Request

↓

Current User Dependency

↓

Verify JWT

↓

Load User

↓

Route

↓

Service
```

This keeps authentication reusable and consistent across the application.

---

# Authentication Rules

The following rules apply throughout the project.

### Rule 1

Passwords are never stored in plaintext.

---

### Rule 2

Passwords are always hashed before storage.

---

### Rule 3

JWT generation is centralized.

---

### Rule 4

JWT verification is centralized.

---

### Rule 5

Routes never implement authentication logic directly.

---

### Rule 6

Authentication logic belongs only inside the Authentication Service and Security module.

---

### Rule 7

Every protected endpoint uses the Current User dependency.

---

### Rule 8

Never trust user-provided identity.

The backend always determines the authenticated user from the validated JWT.

---

# Authentication Responsibility Matrix

| Component | Responsibility |
|------------|----------------|
| **Auth Route** | Receive login/register requests |
| **Auth Service** | Authentication workflow |
| **User Repository** | User lookup and persistence |
| **User Model** | Database representation of users |
| **Auth Schemas** | Request and response validation |
| **Security Module** | Password hashing and JWT operations |
| **Current User Dependency** | Authenticate protected requests |

---

# Architecture Verification Checklist

Before continuing:

- ✅ User model is designed.
- ✅ Authentication architecture is defined.
- ✅ Password hashing strategy is established.
- ✅ JWT architecture is finalized.
- ✅ Authentication flow is documented.
- ✅ Authentication folder structure follows project architecture.
- ✅ Responsibilities of every component are clearly defined.

---

# Deliverable

At the end of Part 1:

- Authentication architecture is complete.
- User model is finalized.
- Password security strategy is defined.
- JWT strategy is established.
- Authentication request lifecycle is documented.

The project is now ready to implement the authentication APIs.

---

## End of Chapter 4 — Part 1
