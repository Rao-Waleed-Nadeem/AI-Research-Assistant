# Phase 1 — Backend Foundations

# Chapter 4 — Authentication Foundation

## Part 2 — Authentication Implementation

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 1 — Backend Foundations  
> **Chapter:** 4 — Authentication Foundation  
> **Part:** 2

---

# Objective

In Part 1, we designed the authentication architecture.

In this chapter, we implement the authentication workflow used throughout our project.

By the end of this chapter, our backend will support:

- User Registration
- User Login
- JWT Generation
- Current User Dependency
- Protected Routes
- Authentication Request Flow
- Standard Authentication Responses

This authentication module will be reused by every secured feature in the project.

---

# Authentication Workflow

The complete authentication process in our project is:

```text
                Register

                    │

                    ▼

           Validate Request

                    │

                    ▼

            Check Existing User

                    │

                    ▼

            Hash Password

                    │

                    ▼

              Save User

                    │

                    ▼

          Registration Success
```

Login follows another flow.

```text
                Login

                    │

                    ▼

             Find User

                    │

                    ▼

          Verify Password

                    │

                    ▼

             Generate JWT

                    │

                    ▼

             Return Token

                    │

                    ▼

      Frontend Stores Token
```

---

# Register API

Purpose:

Create a new user account.

Example Endpoint

```text
POST

/api/v1/auth/register
```

---

# Registration Flow

```text
Frontend

↓

Register Route

↓

Validate Input

↓

Auth Service

↓

Check Email Exists

↓

Hash Password

↓

User Repository

↓

Database

↓

Success Response
```

---

# Registration Request

The frontend provides:

```text
Full Name

Email

Password
```

Only the required information should be accepted.

Future profile fields can be added later.

---

# Registration Validation

Before creating a user, the backend verifies:

- Required fields exist
- Email format is valid
- Password meets minimum requirements
- Email is not already registered

Only after successful validation should the user be created.

---

# Email Already Exists

Flow:

```text
Register

↓

Email Exists?

↓

Yes

↓

Return Error
```

No duplicate accounts should be created.

---

# Password Processing

Never save the password directly.

Correct flow:

```text
Password

↓

Hash Password

↓

Store Hash

↓

Database
```

The original password is discarded immediately after hashing.

---

# User Creation

Once validation succeeds:

```text
Create User

↓

Generate ID

↓

Store Name

↓

Store Email

↓

Store Password Hash

↓

Save
```

Only hashed credentials are stored.

---

# Registration Response

Successful registration returns:

```json
{
    "success": true,
    "message": "User registered successfully.",
    "data": {
        "id": "...",
        "email": "..."
    },
    "errors": null
}
```

Notice:

We never return:

- Password
- Password Hash
- Internal IDs not required by the frontend

---

# Login API

Purpose:

Authenticate an existing user.

Endpoint

```text
POST

/api/v1/auth/login
```

---

# Login Flow

```text
Frontend

↓

Login Route

↓

Auth Service

↓

Find User

↓

Verify Password

↓

Generate JWT

↓

Return Token
```

---

# Login Request

Frontend sends:

```text
Email

Password
```

Nothing more.

---

# User Lookup

Authentication starts by locating the user.

```text
Email

↓

Repository

↓

Database

↓

User
```

If no user exists:

Authentication stops immediately.

---

# Password Verification

The entered password is compared against the stored password hash.

```text
Entered Password

↓

Hash Verification

↓

Stored Hash

↓

Valid?

↓

Yes / No
```

Never compare plaintext passwords.

---

# Invalid Credentials

If:

- Email doesn't exist
- Password is incorrect

Return the same generic error.

Example:

```text
Invalid email or password.
```

Avoid revealing which field was incorrect.

This prevents user enumeration attacks.

---

# JWT Generation

After successful authentication:

```text
Verified User

↓

Security Module

↓

Generate JWT

↓

Return Token
```

The Security module is the only component responsible for creating tokens.

---

# JWT Response

Example:

```json
{
    "success": true,
    "message": "Login successful.",
    "data": {
        "access_token": "...",
        "token_type": "Bearer"
    },
    "errors": null
}
```

Only the access token should be returned.

---

# Frontend Token Storage

After login:

```text
Frontend

↓

Receive JWT

↓

Store Token

↓

Attach To Every Request
```

The frontend becomes responsible for sending the token with future requests.

---

# Authenticated Request

Every protected request follows:

```text
Client

↓

Authorization Header

↓

Backend

↓

Verify JWT

↓

Load User

↓

Continue Request
```

---

# Authorization Header

Protected requests include:

```text
Authorization

Bearer <JWT>
```

The backend extracts the token automatically.

---

# Current User Dependency

Purpose:

Retrieve the authenticated user before executing protected endpoints.

Flow:

```text
Protected Route

↓

Current User Dependency

↓

Extract JWT

↓

Verify JWT

↓

Find User

↓

Return User

↓

Route
```

Routes receive the authenticated user without implementing authentication themselves.

---

# Why Use Current User Dependency?

Without it:

Every protected route would contain:

```text
Extract JWT

↓

Verify JWT

↓

Load User
```

Repeated hundreds of times.

Instead:

```text
Dependency

↓

Every Protected Route
```

Authentication logic exists only once.

---

# Protected Routes

Any endpoint requiring authentication uses the Current User dependency.

Examples:

```text
GET

/api/v1/users/me
```

```text
POST

/api/v1/chat
```

```text
POST

/api/v1/documents
```

```text
GET

/api/v1/history
```

Public endpoints do not use this dependency.

---

# Protected Request Flow

```text
Frontend

↓

JWT

↓

Route

↓

Current User Dependency

↓

Verify JWT

↓

Load User

↓

Business Logic

↓

Response
```

Every secured endpoint follows this exact flow.

---

# Authentication Request Lifecycle

Complete login lifecycle:

```text
Login

↓

Validate Request

↓

Find User

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

Verify JWT

↓

Current User

↓

Protected Resource
```

This lifecycle remains consistent across the application.

---

# Authentication Error Handling

Common authentication errors include:

---

## Invalid Email

```text
User Not Found

↓

Authentication Failed
```

---

## Invalid Password

```text
Password Incorrect

↓

Authentication Failed
```

---

## Invalid Token

```text
JWT Invalid

↓

401 Unauthorized
```

---

## Expired Token

```text
JWT Expired

↓

Login Required
```

---

## Missing Token

```text
Protected Route

↓

No Authorization Header

↓

401 Unauthorized
```

---

# Authentication Response Standards

Successful authentication:

```json
{
    "success": true,
    "message": "...",
    "data": {},
    "errors": null
}
```

Failed authentication:

```json
{
    "success": false,
    "message": "Authentication failed.",
    "data": null,
    "errors": [
        "Invalid credentials."
    ]
}
```

Every authentication endpoint follows the global response format established in Chapter 3.

---

# Authentication Rules

### Rule 1

Routes never verify passwords.

---

### Rule 2

Routes never generate JWTs.

---

### Rule 3

Authentication logic belongs only inside the Authentication Service.

---

### Rule 4

Password hashing belongs only inside the Security module.

---

### Rule 5

JWT generation belongs only inside the Security module.

---

### Rule 6

Repositories never verify passwords.

---

### Rule 7

Protected routes always use the Current User dependency.

---

### Rule 8

Authentication failures never expose sensitive information.

---

# Authentication Responsibility Matrix

| Component | Responsibility |
|------------|----------------|
| Auth Route | Receive authentication requests |
| Auth Service | Execute authentication workflow |
| User Repository | Retrieve and create users |
| Security Module | Hash passwords, verify passwords, generate JWT |
| Current User Dependency | Authenticate protected requests |
| Frontend | Store JWT and attach it to authenticated requests |

---

# Implementation Verification Checklist

Before moving forward, verify:

- ✅ User registration works.
- ✅ Duplicate email registration is blocked.
- ✅ Passwords are hashed before storage.
- ✅ Login verifies hashed passwords.
- ✅ JWT is generated successfully.
- ✅ Frontend receives the token.
- ✅ Protected routes require authentication.
- ✅ Current User dependency loads authenticated users.
- ✅ Authentication errors return standardized responses.

---

# Deliverable

At the end of Part 2, the project has a fully functional authentication workflow.

Implemented features:

```text
Authentication Module

├── Register User
├── Login User
├── Password Hashing
├── JWT Generation
├── JWT Verification
├── Current User Dependency
├── Protected Routes
└── Standard Authentication Responses
```

This authentication system is now ready to secure every feature developed in the remaining phases of the project.

---

## End of Chapter 4 — Part 2
