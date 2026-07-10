# Phase 4 — AI Integration

# Chapter 2 — AI Service Layer & Chat Implementation

> **Version:** 1.0  
> **Status:** Completed  
> **Phase:** 4 — AI Integration  
> **Chapter:** 2 — AI Service Layer & Chat Implementation

---

# Objective

Chapter 1 established the AI infrastructure and provider architecture.

This chapter focuses on implementing the business layer responsible for AI communication.

The AI Service Layer acts as the central controller between the application's business logic and external AI providers. It ensures that AI communication is standardized, secure, reusable, and independent of any specific provider.

At the end of this chapter, our backend will have a complete AI workflow capable of handling user conversations, managing history, interacting with AI providers, and returning standardized responses.

---

# Chapter Deliverable

After completing this chapter:

- ✅ AI Service architecture is complete.
- ✅ Chat Service workflow is finalized.
- ✅ Conversation management is designed.
- ✅ AI communication flow is standardized.
- ✅ Error handling strategy is defined.
- ✅ Logging strategy is established.
- ✅ Standard AI response format is finalized.
- ✅ AI layer is ready for future RAG and AI Agents.

---

# AI Business Layer

The AI business layer consists of two services.

```text
services/

├── ai_service.py
└── chat_service.py
```

Each service has a separate responsibility.

---

# AI Business Architecture

```text
Frontend

↓

Chat Route

↓

Chat Service

↓

AI Service

↓

Provider

↓

LLM
```

This architecture ensures that business logic never communicates directly with AI providers.

---

# AI Service

Location

```text
app/services/ai_service.py
```

---

## Purpose

AI Service is responsible for all communication with AI providers.

It acts as the central gateway between the application and external LLMs.

No other component should directly communicate with Gemini, OpenAI, Groq, OpenRouter, or Ollama.

---

## Responsibilities

AI Service is responsible for:

- Receiving prompts
- Selecting the correct provider
- Sending requests
- Receiving AI responses
- Handling provider failures
- Standardizing responses
- Logging AI operations
- Returning data to Chat Service

---

## AI Service Does NOT

- Validate HTTP requests
- Store conversations
- Access database directly
- Manage authentication
- Contain route logic

Those responsibilities belong to other layers.

---

# AI Service Workflow

```text
Chat Service

↓

Prepare Prompt

↓

AI Service

↓

Provider Factory

↓

Selected Provider

↓

LLM

↓

AI Response

↓

Standard Response

↓

Chat Service
```

---

# Chat Service

Location

```text
app/services/chat_service.py
```

---

## Purpose

Chat Service manages the complete conversation lifecycle.

Unlike AI Service, Chat Service understands the business rules of our application.

---

## Responsibilities

Chat Service is responsible for:

- Managing conversations
- Creating new chats
- Loading previous messages
- Saving user messages
- Calling AI Service
- Saving AI responses
- Returning formatted chat data

---

## Chat Service Does NOT

- Call Gemini directly
- Handle provider authentication
- Parse provider responses
- Manage API keys

Those tasks belong to AI Service.

---

# Chat Service Workflow

```text
Receive User Message

↓

Load Conversation

↓

Save User Message

↓

Call AI Service

↓

Receive AI Response

↓

Save AI Response

↓

Return Conversation
```

---

# Complete Chat Request Flow

```text
Frontend

↓

POST /chat

↓

Authentication

↓

Validate Request

↓

Chat Route

↓

Chat Service

↓

Conversation Repository

↓

Store User Message

↓

AI Service

↓

Provider Factory

↓

Gemini

↓

Provider

↓

AI Service

↓

Chat Service

↓

Conversation Repository

↓

Store AI Response

↓

Return Response

↓

Frontend
```

This is the standard workflow for every chat request.

---

# Conversation Management

Every conversation consists of multiple messages exchanged between the user and the AI.

Typical structure:

```text
Conversation

├── User Message
├── AI Response
├── User Message
├── AI Response
└── ...
```

Each message is stored individually, allowing the application to reconstruct the conversation history when needed.

---

# Conversation Lifecycle

```text
User Starts Chat

↓

Create Conversation

↓

Store User Message

↓

Generate AI Response

↓

Store AI Response

↓

Return Updated Conversation
```

If the conversation already exists, the existing history is loaded before generating a response.

---

# Conversation History

Conversation history provides context for the AI model.

Workflow:

```text
Load Conversation

↓

Retrieve Previous Messages

↓

Build Chat Context

↓

Send Context to AI

↓

Receive Response
```

This ensures that the AI responds based on the ongoing conversation rather than treating each request independently.

---

# AI Request Preparation

Before sending a request to the provider, Chat Service prepares the complete input.

This includes:

- User prompt
- Previous conversation (if applicable)
- System instructions (future)
- Model configuration

The prepared request is then passed to AI Service.

---

# AI Provider Communication

AI Service delegates the request to the selected provider.

```text
AI Service

↓

Provider Factory

↓

Selected Provider

↓

Generate Response

↓

Return Result
```

AI Service does not know the internal implementation of the provider—it only relies on the common provider interface.

---

# AI Response Processing

After receiving a response:

1. Validate the response.
2. Convert it to the project's standard format.
3. Return it to Chat Service.

Chat Service then:

1. Saves the response.
2. Updates the conversation.
3. Returns the final API response.

---

# Standard AI Response

Every provider must return the same internal structure.

Example:

```json
{
    "success": true,
    "message": "Response generated successfully.",
    "data": {
        "conversation_id": "...",
        "response": "...",
        "provider": "gemini",
        "model": "gemini-2.5-flash"
    }
}
```

This consistency allows the frontend to work with any provider without modification.

---

# Error Handling Strategy

AI communication can fail for many reasons.

Common scenarios:

- Invalid API key
- Network failure
- Rate limit exceeded
- Provider unavailable
- Timeout
- Invalid response

All such errors should be handled within AI Service or the Provider implementation.

Routes and Chat Service should never contain provider-specific error handling.

---

# Retry Strategy

For temporary failures, AI Service may retry the request.

Typical retry scenarios:

- Timeout
- Temporary network issue
- Transient provider error

Retries should:

- Be limited in number.
- Stop immediately for permanent failures (e.g., invalid API key).

---

# Fallback Provider (Future)

If enabled, AI Service can switch to another provider when the primary provider fails.

Example:

```text
Gemini Failed

↓

AI Service

↓

Fallback Provider

↓

Groq

↓

Return Response
```

This improves application availability without affecting business logic.

---

# Logging Strategy

AI-related operations should be logged for monitoring and debugging.

Log:

- Provider used
- Selected model
- Request timestamp
- Response time
- Success/Failure
- Error details (non-sensitive)

Never log:

- User passwords
- API keys
- JWT tokens
- Sensitive conversation content (unless explicitly required and protected)

---

# Database Integration

Chat Service communicates with repositories to manage conversation data.

```text
Chat Service

↓

Conversation Repository

↓

Conversation Table

↓

Message Table
```

AI Service never accesses the database directly.

---

# Separation of Responsibilities

| Component | Responsibility |
|------------|----------------|
| Route | Receive request |
| Chat Service | Manage conversation |
| AI Service | Manage AI communication |
| Provider | Communicate with LLM |
| Repository | Store and retrieve data |

Each component has a single responsibility.

---

# Future Integration

The AI Service is designed to support future modules without major changes.

Future features:

```text
Chat

↓

Document Analysis

↓

Embeddings

↓

Vector Search

↓

RAG

↓

AI Agents

↓

Multi-Agent Systems
```

These modules will reuse AI Service rather than creating new AI communication logic.

---

# Development Rules

## Never

- Call providers directly from Routes.
- Call providers directly from Chat Service.
- Store API keys in Services.
- Mix business logic with provider logic.
- Duplicate AI communication code.
- Skip conversation storage.

---

## Always

- Use AI Service for every AI request.
- Access providers through Provider Factory.
- Save user and AI messages.
- Return standardized responses.
- Handle provider-specific errors inside Providers.
- Log AI operations.
- Maintain separation of concerns.

---

# AI Service Checklist

Before considering the AI layer complete:

- ✅ AI Service implemented.
- ✅ Chat Service implemented.
- ✅ Provider communication centralized.
- ✅ Conversation management completed.
- ✅ Conversation history supported.
- ✅ Standard AI response implemented.
- ✅ Error handling completed.
- ✅ Retry mechanism implemented.
- ✅ Logging configured.
- ✅ Future modules can reuse AI Service.

---

# Chapter Summary

The AI business layer is now fully defined.

The application has a clear separation between conversation management and provider communication:

- **Chat Service** manages conversations and business rules.
- **AI Service** manages all interactions with AI providers.
- **Providers** handle provider-specific implementations.
- **Repositories** manage persistent storage.

This architecture keeps the system modular, testable, and ready for future AI capabilities.

---

# Deliverable

At the completion of Chapter 2:

- ✅ AI Service architecture is complete.
- ✅ Chat Service workflow is established.
- ✅ Conversation management is standardized.
- ✅ AI communication is centralized.
- ✅ Error handling and logging strategies are finalized.
- ✅ The AI business layer is production-ready and prepared for Embeddings, RAG, and AI Agents.

---

## End of Chapter 2 — AI Service Layer & Chat Implementation

**Next:** **Chapter 3 — Provider Configuration & Future Expansion**, where we will configure all supported AI providers, define environment variables, establish provider selection, and prepare the architecture for future AI features such as Embeddings, RAG, and AI Agents.