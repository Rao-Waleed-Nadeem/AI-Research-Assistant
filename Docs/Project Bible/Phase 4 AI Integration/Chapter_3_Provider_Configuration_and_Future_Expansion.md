# Phase 4 — AI Integration

# Chapter 3 — Provider Configuration & Future Expansion

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 4 — AI Integration  
> **Chapter:** 3 — Provider Configuration & Future Expansion

---

# Objective

This chapter completes the AI layer by configuring all supported providers, defining environment variables, establishing provider selection, and documenting how future AI modules (Embeddings, RAG, AI Agents, etc.) will integrate into the existing architecture.

The objective is **not to implement new architecture** but to configure and extend the architecture built in Chapters 1 and 2.

---

# Chapter Deliverable

After completing this chapter:

- ✅ AI providers are fully configured.
- ✅ Provider switching is supported.
- ✅ Environment variables are finalized.
- ✅ AI configuration is centralized.
- ✅ AI module is production-ready.
- ✅ Architecture is prepared for future AI features.

---

# Final AI Directory

```text
backend/

app/

├── api/
│   └── chat.py
│
├── services/
│   ├── ai_service.py
│   └── chat_service.py
│
├── providers/
│   ├── base_provider.py
│   ├── gemini_provider.py
│   ├── openai_provider.py
│   ├── groq_provider.py
│   ├── openrouter_provider.py
│   ├── ollama_provider.py
│   └── provider_factory.py
│
├── schemas/
│   ├── ai.py
│   └── chat.py
│
└── core/
    └── config.py
```

This structure should remain unchanged throughout the project.

Future AI modules will reuse these components.

---

# AI Configuration Architecture

```text
Application Startup

↓

Load .env

↓

Load Settings

↓

Initialize Provider Factory

↓

Register Providers

↓

Application Ready
```

All configuration happens once during application startup.

No provider should be configured manually inside Services.

---

# Environment Variables

All AI configuration should come from `.env`.

Example

```env
# Default Provider

DEFAULT_PROVIDER=gemini

# Default Model

DEFAULT_MODEL=gemini-2.5-flash

# Gemini

GEMINI_API_KEY=

# OpenAI

OPENAI_API_KEY=

# Groq

GROQ_API_KEY=

# OpenRouter

OPENROUTER_API_KEY=

# Ollama

OLLAMA_BASE_URL=http://localhost:11434
```

Never hardcode these values.

---

# Configuration Responsibilities

## DEFAULT_PROVIDER

Purpose

Defines which provider Provider Factory should return.

Example

```env
DEFAULT_PROVIDER=gemini
```

Possible values

- gemini
- openai
- groq
- openrouter
- ollama

Changing this value changes the application's AI provider without modifying any code.

---

## DEFAULT_MODEL

Purpose

Defines the default model used by the selected provider.

Example

```env
DEFAULT_MODEL=gemini-2.5-flash
```

If required, Services may override this model for specific requests.

---

## Provider API Keys

Each provider has its own API key.

Example

```env
GEMINI_API_KEY=...

OPENAI_API_KEY=...

GROQ_API_KEY=...
```

Only the corresponding Provider implementation should access its API key.

No other module should read provider credentials.

---

## OLLAMA_BASE_URL

Purpose

Defines the local Ollama server endpoint.

Example

```env
OLLAMA_BASE_URL=http://localhost:11434
```

Only the Ollama Provider uses this value.

---

# Provider Registration

Every provider must be registered inside Provider Factory.

Example workflow

```text
Application

↓

Provider Factory

↓

Register Gemini

↓

Register OpenAI

↓

Register Groq

↓

Register OpenRouter

↓

Register Ollama

↓

Ready
```

Unregistered providers cannot be selected.

---

# Provider Selection Flow

```text
Chat Service

↓

AI Service

↓

Provider Factory

↓

DEFAULT_PROVIDER

↓

Return Provider

↓

Generate Response
```

Provider selection happens automatically.

Business logic never selects providers directly.

---

# Switching Providers

Changing providers should require **zero code changes**.

Current

```env
DEFAULT_PROVIDER=gemini
```

Switch to OpenAI

```env
DEFAULT_PROVIDER=openai
```

Restart backend.

Done.

The following remain unchanged

- Routes
- Chat Service
- AI Service
- Frontend
- Database

Only the Provider implementation changes.

---

# Adding a New Provider

Future providers should follow the same workflow.

```text
Create Provider

↓

Inherit Base Provider

↓

Implement Interface

↓

Read Configuration

↓

Register Factory

↓

Testing

↓

Done
```

Example

```text
Claude Provider

↓

claude_provider.py

↓

Register Factory

↓

DEFAULT_PROVIDER=claude

↓

Ready
```

No changes are required anywhere else.

---

# Provider Requirements

Every provider must implement

- Authentication
- Generate Response
- Health Check
- List Models
- Error Handling

Optional

- Streaming
- Image Generation
- Function Calling

The interface should remain consistent.

---

# AI Module Startup

Complete startup sequence

```text
Backend Starts

↓

Load Environment Variables

↓

Load Configuration

↓

Initialize Database

↓

Initialize Provider Factory

↓

Register Providers

↓

Create AI Service

↓

Application Ready
```

The AI layer is initialized once during application startup.

---

# AI Module Communication

Complete communication architecture

```text
Frontend

↓

Chat Route

↓

Chat Service

↓

AI Service

↓

Provider Factory

↓

Selected Provider

↓

External LLM

↓

AI Response

↓

Chat Service

↓

Database

↓

Frontend
```

This communication flow should never change.

---

# Security Standards

Always

- Store API keys in `.env`
- Load configuration from Settings
- Validate provider configuration during startup
- Hide sensitive errors from users

Never

- Commit `.env`
- Hardcode API keys
- Return provider secrets in responses
- Log API keys

---

# Future AI Modules

The architecture is intentionally designed so that future modules reuse the existing AI infrastructure.

---

## Embeddings

Future flow

```text
Document

↓

Embedding Service

↓

AI Service

↓

Embedding Provider

↓

Vector

↓

Vector Database
```

No architectural changes required.

---

## Document Processing

```text
Upload File

↓

Document Service

↓

Extract Text

↓

AI Service

↓

LLM

↓

Summary

↓

Database
```

The Document Service simply consumes AI Service.

---

## Retrieval-Augmented Generation (RAG)

```text
Question

↓

RAG Service

↓

Vector Search

↓

Relevant Context

↓

AI Service

↓

Provider

↓

Answer
```

RAG becomes another consumer of AI Service.

---

## AI Agents

```text
User Goal

↓

Agent Service

↓

Planner

↓

AI Service

↓

Provider

↓

Execute Task

↓

Return Result
```

Agent Service orchestrates workflows but never bypasses AI Service.

---

## Multi-Agent System

```text
Coordinator

├── Research Agent

├── Coding Agent

├── Analysis Agent

└── Writing Agent

↓

AI Service

↓

Provider
```

All agents share the same AI infrastructure.

---

# AI Integration Rules

## Never

- Call providers from Routes.
- Call providers from Controllers.
- Hardcode provider names.
- Hardcode model names.
- Read `.env` inside Services.
- Duplicate provider logic.
- Skip Provider Factory.
- Store API keys in source code.

---

## Always

- Access AI through AI Service.
- Access providers through Provider Factory.
- Read configuration from Settings.
- Return standardized responses.
- Handle provider-specific errors inside Providers.
- Keep providers independent.
- Reuse AI Service for every AI-powered feature.

---

# Final AI Architecture

```text
Frontend

↓

FastAPI Route

↓

Authentication

↓

Schema Validation

↓

Chat Service

↓

AI Service

↓

Provider Factory

↓

Selected Provider

↓

Gemini
OpenAI
Groq
OpenRouter
Ollama

↓

AI Response

↓

Chat Service

↓

Repository

↓

Database

↓

Standard Response

↓

Frontend
```

This architecture will remain valid for the lifetime of the project.

---

# AI Implementation Checklist

Before moving to Phase 5, verify:

### Infrastructure

- ✅ AI folder structure created.
- ✅ Provider interface implemented.
- ✅ Provider Factory implemented.
- ✅ AI Service implemented.
- ✅ Chat Service implemented.

### Providers

- ✅ Gemini integrated.
- ✅ OpenAI integrated.
- ✅ Groq integrated.
- ✅ OpenRouter integrated.
- ✅ Ollama integrated.

### Configuration

- ✅ Environment variables configured.
- ✅ Default provider configured.
- ✅ Default model configured.
- ✅ Provider switching verified.

### Communication

- ✅ Chat flow completed.
- ✅ AI request lifecycle completed.
- ✅ AI response lifecycle completed.
- ✅ Conversation management completed.

### Future Ready

- ✅ Embeddings supported.
- ✅ RAG supported.
- ✅ AI Agents supported.
- ✅ Multi-provider architecture completed.

---

# Phase 4 Summary

Phase 4 establishes a complete, production-ready AI layer that is independent of any specific LLM provider.

The implementation is centered around three core components:

- **AI Infrastructure** — Provider abstraction, folder structure, and communication architecture.
- **AI Business Layer** — Chat Service, AI Service, conversation management, and standardized request/response handling.
- **Provider Configuration** — Environment-based configuration, provider registration, provider switching, and future extensibility.

With this phase complete, the backend is ready to support both current chat functionality and future AI capabilities—such as Embeddings, RAG, Document Intelligence, and AI Agents—without requiring architectural changes.

---

# Deliverable

At the completion of Phase 4:

- ✅ Multi-provider AI architecture is fully implemented.
- ✅ AI communication is centralized and standardized.
- ✅ Configuration is environment-driven.
- ✅ Provider switching requires no code changes.
- ✅ The project is prepared for advanced AI features in subsequent phases.

---

## End of Phase 4 — AI Integration

**Next Phase:** **Phase 5 — Embeddings & Vector Database**, where we will implement semantic search, vector generation, document indexing, retrieval pipelines, and lay the foundation for Retrieval-Augmented Generation (RAG).