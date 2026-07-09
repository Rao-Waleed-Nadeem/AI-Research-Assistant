# TODO — AI Knowledge Assistant (Frontend-first roadmap)

## Plan (sequential)

1. Analyze root `Readme.md` to extract the planned phases and missing work.
2. Inspect the existing frontend (read `frontend/README.md`, `frontend/AGENTS.md`, and key pages/components) to understand what is currently implemented.
3. Define a _frontend execution roadmap_ that maps the big future roadmap (Embeddings → RAG → Agents → Docker/AWS) into smaller frontend milestones.
4. Create a single consolidated list of tasks/milestones in `TODO.md` with clear, easy-to-follow instructions.
5. For each milestone: identify the exact files/components likely affected (only when necessary), then implement step-by-step.
6. Validate each milestone locally (lint/build/run) and ensure the frontend still connects to the backend endpoints.
7. After completing the roadmap milestones, re-check documentation consistency (update any README sections that no longer match reality).

## Milestones / Task Breakdown

### M0 — Inventory & alignment (frontend + backend integration)

- [ ] Confirm what frontend currently does (existing page(s) and API calls).
- [ ] Record which backend endpoints are called by the frontend and which ones are still missing in the UI.
- [ ] Identify the UX gap(s): what users can’t yet do in the UI compared to the intended chat workflow.

### M1 — Chat UI + API wiring (baseline experience)

- [ ] Implement/finish a dedicated chat page/component (messages list, composer, send button).
- [ ] Add minimal auth handling (detect missing JWT / show login prompt when unauthorized).
- [ ] Add loading + error states for the `/chat` request.
- [ ] Ensure message persistence works with the backend response shape.

### M2 — Embeddings UI + backend contract (Day 7)

- [ ] Add a UI flow to trigger/build embeddings for a corpus (or confirm existing backend endpoint).
- [ ] Display embedding status/progress/errors.
- [ ] Confirm response schema and handle failures gracefully.

### M3 — RAG UI + retrieval experience (Day 8–10)

- [ ] Add a chat mode toggle or “RAG enabled” flow.
- [ ] Show retrieved context (or a collapsed “sources/context” panel) when available.
- [ ] Ensure the backend RAG response is rendered correctly.

### M4 — Agent UI (Day 10)

- [ ] Add “agent mode” (e.g., reasoning/tooling on/off depending on backend capability).
- [ ] Render agent-specific outputs (steps, tool results, final answer) if backend provides structured fields.
- [ ] Ensure safety/limits: timeouts and max token handling UX.

### M5 — DevOps prep: Docker (Day ?)

- [ ] Add a frontend-friendly Docker setup plan (build artifacts, env vars, port mapping).
- [ ] Verify frontend build inside Docker (or document it if out of scope).

### M6 — Deploy readiness: AWS (Day ?)

- [ ] Document deployment steps for the full stack.
- [ ] Ensure required environment variables are enumerated and mapped.

## Notes / Assumptions

- The root `Readme.md` contains a detailed backend-layer roadmap, but it does not include frontend implementation details.
- This TODO focuses on turning the large roadmap into manageable milestones that can be executed safely.
