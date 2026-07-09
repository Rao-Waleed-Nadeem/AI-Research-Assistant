# TODO — AI Knowledge Assistant Project

This document converts the project spec in `Readme.md` into an execution plan with small, testable milestones. The goal is a **bug-free, intended production-ready project** via strict layering, validation, tests, and incremental integration.

> Assumptions:
>
> - Current repo already has a Next.js `frontend/`.
> - A backend is intended (per `Readme.md`) using **FastAPI + SQLAlchemy + PostgreSQL + JWT**.
> - Future phases (Embeddings, RAG, Agents, Docker, AWS) are planned after the core system works end-to-end.

---

## Information gathered from `Readme.md`

1. **Architecture (layered)**
   - Routes (FastAPI) → JWT Authentication → Pydantic Validation → Service Layer → Repository Layer → SQLAlchemy → PostgreSQL (Docker) → AI Provider → Response
   - Frontend calls the backend (no direct DB/AI calls from frontend).

2. **Key components expected**
   - SQLAlchemy models: `User`, `Chat`, `Message`.
   - Pydantic schemas for request/response DTOs.
   - JWT authentication flow (password hashing, token issuance, dependency injection for current user).
   - AI integration encapsulated behind an `AIService` provider abstraction (Gemini primary, OpenRouter/Groq/Ollama optional, OpenAI optional).
   - Repository layer encapsulates CRUD + session/transactions.

3. **Development discipline**
   - Never place DB logic in routes.
   - Never call OpenAI directly from routes.
   - Always use repositories + services.
   - Always validate inputs with Pydantic.

4. **Phases / progress referenced in README**
   - Completed: Phase 0 → Phase 3
   - Phase 4+ roadmap: AI Integration (Gemini first) → Embeddings → RAG → Agents → Docker Compose → AWS Deployment.

---

## Edit plan (Milestone-based, sequential, testable)

### Milestone 0 — Project readiness & baseline

**Goal:** Ensure the repository can run locally with a stable baseline and consistent dev workflow.

1. Confirm runtime prerequisites
   - Node.js version (for Next.js)
   - Python version (for FastAPI)
   - PostgreSQL availability (we will use docker)
   - Environment variables strategy

2. Create/confirm backend folder structure (if not present)
   - `backend/app/api/routes`
   - `backend/app/core`
   - `backend/app/models`
   - `backend/app/schemas`
   - `backend/app/repositories`
   - `backend/app/services`
   - `backend/app/auth`
   - `backend/app/utils`

3. Add `.env.example` files for backend and frontend
   - Backend: `OPENAI_API_KEY`, `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`
   - Frontend: any public API base URLs (e.g., `NEXT_PUBLIC_API_URL`)

4. Ensure tooling is ready
   - Python: formatter + linter config
   - Frontend: existing ESLint config validated

**Exit criteria (testable):**

- `frontend` starts successfully.
- Backend can start (or at minimum, imports successfully) with stubbed routes if backend code is missing.

---

### Milestone 1 — Backend: database + models (User/Chat/Message)

**Goal:** Implement stable DB schema foundation.

1. Define SQLAlchemy models
   - `User` (id, email/username, password_hash, created_at, etc.)
   - `Chat` (id, user_id, title, created_at, updated_at)
   - `Message` (id, chat_id, sender_role/system/user/assistant, content, created_at)

2. Define relationships
   - `User → Chats`
   - `Chat → Messages`

3. Add migration strategy
   - Use Alembic
   - Generate initial migration for tables

4. Add basic repository scaffolding
   - Create DB session dependency
   - Provide repositories with clean CRUD method signatures

**Exit criteria (testable):**

- Migrations apply cleanly on a fresh database.
- SQLAlchemy models create expected tables with correct foreign keys.

---

### Milestone 2 — Backend: schemas + validation

**Goal:** Lock down request/response contracts.

1. Create Pydantic schemas (DTOs)
   - Auth schemas: register/login/token responses
   - User schema: `UserOut`, `MeOut`
   - Chat schemas: `ChatCreate`, `ChatOut`
   - Message schemas: `MessageCreate`, `MessageOut`
   - Chat list/stream schemas if applicable

2. Ensure consistent naming and serialization
   - Use `from_attributes` / `orm_mode` as appropriate
   - Ensure timestamps are consistently serialized

3. Add validation rules
   - Email format
   - Password constraints
   - Maximum lengths for chat titles and message content

**Exit criteria (testable):**

- Backend endpoints reject invalid payloads with clear 422 errors.

---

### Milestone 3 — Backend: authentication (JWT) end-to-end

**Goal:** Provide secure auth usable by frontend.

1. Implement password hashing/verification
   - Use a strong hash algorithm (e.g., bcrypt/argon2 depending on chosen stack)

2. Implement JWT token issuance
   - `POST /register`
   - `POST /login`
   - Return access token with expiry

3. Implement “current user” dependency
   - Read `Authorization: Bearer <token>`
   - Validate signature/expiry
   - Resolve user from DB

4. Protect routes
   - `GET /me`
   - `POST /chat` should require auth

5. Add error mapping
   - 401 for missing/invalid token
   - 409 for duplicate register if specified

**Exit criteria (testable):**

- Register → login → token → authenticated `/me` works.
- Wrong password/token returns correct HTTP status.

---

### Milestone 4 — Backend: repository layer + transactions

**Goal:** Ensure correctness under failures and consistent DB access patterns.

1. Implement repository methods
   - Users: create, get_by_email, get_by_id
   - Chats: create, get_by_id (scoped to user), list for user
   - Messages: create for chat, list for chat

2. Session/transaction handling
   - Repositories do not manage HTTP concerns
   - Ensure rollback on errors
   - Ensure consistent commit boundaries

3. Add guardrails
   - Enforce chat ownership (user can only access their chats)

**Exit criteria (testable):**

- Ownership checks prevent cross-user chat/message reads.
- DB integrity errors are handled predictably.

---

### Milestone 5 — Backend: OpenAI integration via AI service

**Goal:** Encapsulate AI provider logic.

1. Implement AI service responsibilities (per README)
   - Conversation builder
     - Load relevant chat history from repository
     - Convert messages into OpenAI format (roles + content)
   - Prompt builder / system prompt handling
   - OpenAI client wrapper
   - Response parser

2. Add structured error handling
   - Retry strategy (for transient provider errors)
   - Timeouts
   - Log-safe errors (no secrets)

3. Ensure OpenAI is called only from AI service
   - Routes must not instantiate OpenAI clients directly

4. Add config via environment variables
   - Model name, temperature, max tokens

**Exit criteria (testable):**

- `POST /chat` produces an assistant response and persists messages.
- Provider failures return a controlled 5xx (not a stack trace).

---

### Milestone 6 — Backend: API endpoints + dependency injection

**Goal:** Connect layers into stable HTTP endpoints.

1. Implement endpoints (per README)
   - `POST /register`
   - `POST /login`
   - `GET /me`
   - `POST /chat`
   - (If needed) `GET /chats`, `GET /chats/{id}/messages`

2. Use dependency injection
   - DB session dependency
   - Current user dependency
   - AI service dependency
   - Repositories as dependencies or injected into services

3. Response consistency
   - Always return typed Pydantic response schemas

**Exit criteria (testable):**

- Full API path works: request → validation → auth → service → repositories → OpenAI → persistence → response.

---

### Milestone 7 — Frontend: end-to-end integration & UX correctness

**Goal:** Ensure frontend consumes backend correctly and securely.

1. Configure frontend API base URL
   - `NEXT_PUBLIC_API_URL`

2. Implement auth flow UI (if not present)
   - Register form
   - Login form
   - Store token securely (recommended: httpOnly cookie via backend; if not available, then secure storage strategy)

3. Implement chat UI
   - Display message history
   - Submit new message
   - Show loading/error states

4. Token handling and protected calls
   - Send `Authorization` header

**Exit criteria (testable):**

- User can authenticate and create a chat with assistant responses.
- Errors show correct messages and do not break the UI.

---

### Milestone 8 — Testing & bug prevention (core)

**Goal:** Make the project stable and prevent regressions.

1. Backend unit tests
   - Schemas validation tests
   - Repository tests (with test DB)
   - Service tests (mock OpenAI client)

2. Backend integration tests
   - Register/login/token flow
   - Auth-protected endpoint behavior
   - Chat endpoint persists messages

3. Frontend tests (if test framework exists)
   - Basic component rendering tests
   - API mocking for chat submission

4. Add CI-like local checks
   - Run linters
   - Run formatting checks

**Exit criteria (testable):**

- Test suite passes.
- Lint/static analysis shows no critical issues.

---

### Milestone 9 — Phase 4 hardening (production readiness)

**Goal:** Eliminate common classes of production bugs.

1. Security review
   - JWT expiry enforced
   - Password hashing correctness
   - Ownership checks
   - Input length limits

2. Observability
   - Structured logs around failures
   - Correlation ids if feasible

3. Performance hygiene
   - Ensure chat history truncation strategy
   - Prevent N+1 patterns in repositories

4. Rate limiting / abuse resistance (optional per scope)

**Exit criteria (testable):**

- Manual smoke test passes: register/login/chat.
- Failure modes (invalid token, invalid payload, OpenAI failure) behave as documented.

---

## Remaining Milestones (from README roadmap)

### Milestone 10 — Embeddings (Phase 5 start)

**Goal:** Add groundwork for semantic search.

1. Add embedding provider integration to AI service
2. Create database support if required (tables for vectors or text chunks)
3. Add endpoint or background job strategy (depending on architecture)
4. Validate cost/latency constraints

**Exit criteria:** Embeddings can be generated and stored/retrieved reliably.

---

### Milestone 11 — RAG

**Goal:** Use embeddings to retrieve relevant context for chat.

1. Implement chunking strategy
2. Implement retrieval (top-k) and reranking (optional)
3. Build augmented prompt with retrieved context
4. Add tests for retrieval correctness

**Exit criteria:** Chat responses cite or incorporate retrieved context consistently.

---

### Milestone 12 — Agents

**Goal:** Add tool-using or multi-step reasoning flows.

1. Define agent interfaces
2. Implement tool registry
3. Ensure execution safety (time limits, tool validation)
4. Persist agent steps if required

**Exit criteria:** Agents run deterministically enough for stable UX.

---

### Milestone 13 — Dockerization

**Goal:** Reproducible deployments.

1. Add Dockerfile(s) for backend and (optionally) frontend
2. Add docker-compose for dev
3. Verify environment variable wiring

**Exit criteria:** `docker compose up` runs full stack locally.

---

### Milestone 14 — AWS deployment

**Goal:** Deploy the stack.

1. Decide deployment targets (EC2/ECS/Lambda + RDS)
2. Provision secrets management
3. Set up CI/CD pipeline
4. Validate scaling and logging

**Exit criteria:** Production environment runs and logs correctly.

---

## Commands checklist (tracked)

> Update this section as commands are verified in your environment.

### Backend

- Create venv / activate
- Install deps
- Run server
- Run alembic migrations
- Run tests

### Frontend

- `npm install`
- `npm run dev`
- Lint/tests

---

## Progress tracker (update as milestones complete)

- ✅ Milestone 0 — Project readiness & baseline
- ✅ Milestone 1 — Database + models
- ✅ Milestone 2 — Schemas + validation
- ✅ Milestone 3 — JWT authentication
- ⬜ Milestone 4 — Repository layer + transactions
- ⬜ Milestone 5 — AI integration via AIService (Gemini first)
- ⬜ Milestone 6 — API endpoints + DI
- ⬜ Milestone 7 — Frontend integration
- ⬜ Milestone 8 — Testing & bug prevention
- ⬜ Milestone 9 — Production hardening
- ⬜ Milestone 10 — Embeddings
- ⬜ Milestone 11 — RAG
- ⬜ Milestone 12 — Agents
- ⬜ Milestone 13 — Docker Compose
- ⬜ Milestone 14 — AWS deployment
