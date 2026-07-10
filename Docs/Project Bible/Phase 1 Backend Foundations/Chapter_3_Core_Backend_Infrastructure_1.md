# Phase 1 — Backend Foundations

# Chapter 3 — Core Backend Infrastructure

## Part 1 — Configuration Foundation

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 1 — Backend Foundations  
> **Chapter:** 3 — Core Backend Infrastructure  
> **Part:** 1

---

# Objective

In the previous chapter, we designed the backend architecture.

Now we begin implementing the reusable infrastructure that every module will depend on.

Nothing in this chapter belongs to a specific feature such as Authentication, Chat, AI, or RAG.

Instead, we build the project's shared foundation.

By the end of this part, our application will have:

- Centralized configuration
- Environment management
- Configuration loading flow
- Environment separation
- Project-wide configuration standards

Every future module will use this infrastructure.

---

# Expected Outcome

After completing this part:

- Every configurable value comes from one place.
- No secrets exist inside source code.
- Development and Production configurations are separated.
- Every module accesses configuration consistently.

This eliminates duplicated configuration and makes the application easier to maintain.

---

# Why Configuration Matters

Our application contains many values that will change depending on the environment.

Examples:

- Database URL
- JWT Secret
- Gemini API Key
- OpenRouter API Key
- Debug Mode
- Server Host
- Server Port

These values should never be hardcoded.

Instead, they are loaded during application startup.

---

# Configuration Architecture

Our project follows this configuration flow.

```text
Developer

↓

.env

↓

Settings

↓

Configuration

↓

Entire Backend
```

Everything starts from the environment file.

No module should bypass this flow.

---

# Configuration Directory

Configuration belongs inside:

```text
backend/

app/

core/

├── settings.py

├── config.py

├── security.py

└── logging.py
```

Each file has a dedicated responsibility.

---

# Responsibility of Each Configuration File

## settings.py

Purpose:

Load environment variables.

Responsibilities:

- Read `.env`
- Validate required values
- Store application settings
- Provide configuration object

This is the only file that should directly access environment variables.

---

## config.py

Purpose:

Prepare application configuration.

Responsibilities:

- API metadata
- Application constants
- Shared configuration
- Global application settings

Other modules should import configuration from here rather than creating their own values.

---

## security.py

Purpose:

Centralize security configuration.

Examples:

- JWT Algorithm
- Password hashing settings
- Token expiration
- Authentication configuration

Authentication modules should never define security values themselves.

---

## logging.py

Purpose:

Centralize logging configuration.

Responsibilities:

- Log level
- Log format
- Logger initialization
- File logging (future)
- Console logging

Every module uses the same logger configuration.

---

# Environment Files

Our backend uses environment files to store configurable values.

Project structure:

```text
backend/

.env

.env.example

app/

requirements.txt
```

---

# .env

Purpose:

Stores the actual configuration used by the current environment.

Typical values include:

```text
APP_NAME

APP_VERSION

ENVIRONMENT

DEBUG

DATABASE_URL

JWT_SECRET_KEY

JWT_ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES

GEMINI_API_KEY

OPENROUTER_API_KEY

OPENAI_API_KEY

GROQ_API_KEY
```

This file contains sensitive information.

It must never be committed to Git.

---

# .env.example

Purpose:

Acts as a template.

It contains every required variable without exposing secrets.

Example structure:

```text
APP_NAME=

APP_VERSION=

DATABASE_URL=

JWT_SECRET_KEY=

GEMINI_API_KEY=
```

When another developer clones the project:

1.

Copy

```text
.env.example
```

↓

2.

Rename

```text
.env
```

↓

3.

Fill in actual values.

This makes project setup much easier.

---

# Environment Separation

Our project supports multiple environments.

```text
Development

↓

Testing

↓

Production
```

Each environment can use different values while keeping the code identical.

Example:

Development:

```text
DEBUG=True
```

Production:

```text
DEBUG=False
```

The application behavior changes automatically without modifying source code.

---

# Configuration Loading Flow

When the backend starts:

```text
Application Starts

↓

Read .env

↓

Load Settings

↓

Validate Configuration

↓

Create Configuration Object

↓

Application Ready
```

If required configuration is missing:

Application startup should fail immediately.

It is better to stop the application than run with incomplete configuration.

---

# Configuration Categories

Instead of placing everything together, configuration should be grouped logically.

---

## Application

Contains application information.

Examples:

```text
Application Name

Version

Description

Environment

Debug Mode
```

---

## Database

Contains database connection settings.

Examples:

```text
Database URL

Pool Size

Connection Timeout

Echo Mode
```

Future database settings should also be added here.

---

## Authentication

Contains JWT configuration.

Examples:

```text
Secret Key

Algorithm

Token Expiration
```

Keeping authentication settings together simplifies maintenance.

---

## AI Providers

Contains provider credentials.

Examples:

```text
Gemini API Key

OpenRouter API Key

OpenAI API Key

Groq API Key
```

Adding another provider later only requires extending this section.

---

## Server

Contains application server settings.

Examples:

```text
Host

Port

Reload Mode
```

---

# Configuration Access Rule

Every module follows this rule:

```text
Need Configuration?

↓

Settings

↓

Configuration

↓

Use Value
```

Never:

```text
Service

↓

Read .env

❌
```

Never:

```text
Repository

↓

Read Environment Variable

❌
```

Configuration should always be centralized.

---

# Why Centralized Configuration?

Without centralization:

```text
Authentication

↓

JWT Secret
```

AI Service

↓

API Key

Database

↓

Database URL

Every module stores its own configuration.

Soon:

- Duplicate values
- Different naming
- Hardcoded secrets
- Difficult maintenance

Instead:

```text
Settings

↓

Entire Application
```

One source.

One configuration.

One maintenance point.

---

# Configuration Naming Standards

Use descriptive names.

Good:

```text
DATABASE_URL

JWT_SECRET_KEY

ACCESS_TOKEN_EXPIRE_MINUTES

GEMINI_API_KEY
```

Avoid:

```text
DB

SECRET

KEY

TOKEN
```

Names should clearly describe their purpose.

---

# Configuration Rules

Every configuration value should satisfy these rules.

### Rule 1

Configuration should never be hardcoded.

---

### Rule 2

Configuration should be environment-specific.

---

### Rule 3

Secrets belong only inside `.env`.

---

### Rule 4

Only the Settings module reads environment variables.

---

### Rule 5

Application modules access configuration through the centralized configuration object.

---

### Rule 6

Configuration names should remain consistent throughout the project.

---

# Files That Use Configuration

As the project grows, nearly every module will depend on configuration.

Examples:

```text
main.py

↓

Settings
```

```text
Database

↓

Database URL
```

```text
Authentication

↓

JWT Secret
```

```text
AI Service

↓

Gemini API Key
```

```text
Logging

↓

Log Level
```

Every module receives configuration from the same source.

---

# Future Configuration Expansion

Later phases will extend this system.

Future additions include:

```text
Docker Configuration

AWS Configuration

Redis

Celery

Email Service

Payment Gateway

RAG Settings

Embedding Models

Agent Configuration

Monitoring

Caching
```

No architectural changes will be required.

Only new configuration entries will be added.

---

# Configuration Verification Checklist

Before continuing, verify:

- ✅ `.env` exists.
- ✅ `.env.example` exists.
- ✅ Configuration is centralized.
- ✅ Secrets are not hardcoded.
- ✅ Environment variables load successfully.
- ✅ Every module uses the shared configuration.
- ✅ Development and Production values can differ.
- ✅ Configuration follows naming standards.

---

# Best Practices

- Keep all configurable values outside the source code.
- Never commit `.env` to Git.
- Keep `.env.example` updated whenever a new variable is introduced.
- Group related configuration together (Application, Database, AI, Authentication, etc.).
- Remove unused configuration variables to keep the project clean.
- Document every new environment variable so other developers know its purpose.

---

# Deliverable

At the end of Part 1, the backend has a centralized configuration system.

Current infrastructure:

```text
backend/

├── .env
├── .env.example
│
├── app/
│   │
│   ├── core/
│   │   ├── settings.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   │
│   └── main.py
│
└── requirements.txt
```

Every future feature—Authentication, Database, AI Providers, RAG, Agents, Docker, and Deployment—will use this configuration foundation.

---

## End of Chapter 3 — Part 1
