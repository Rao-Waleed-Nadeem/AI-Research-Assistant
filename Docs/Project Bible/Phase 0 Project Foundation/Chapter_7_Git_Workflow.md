# Phase 0 — Project Foundation

# Chapter 7 — Git Workflow

> Version: 1.0
>
> Status: Completed
>
> Phase: 0 — Project Foundation
>
> Chapter: 7 — Git Workflow

---

# Table of Contents

1. Introduction
2. What is Git?
3. What is GitHub?
4. Why Version Control Matters
5. Git Workflow Philosophy
6. Branching Strategy
7. Branch Responsibilities
8. Commit Message Convention
9. Pull Request Workflow
10. Merge Strategy
11. Repository Structure
12. .gitignore Strategy
13. Versioning Strategy
14. Release Workflow
15. Daily Development Workflow
16. Best Practices
17. Common Mistakes
18. Chapter Summary

---

# 1. Introduction

Every professional software project requires a version control system.

Version control is much more than saving code—it enables developers to:

- Track every change
- Collaborate safely
- Restore previous versions
- Review code before merging
- Experiment without breaking production
- Maintain project history

For this project, we use **Git** as the version control system and **GitHub** as the remote repository platform.

---

# 2. What is Git?

Git is a distributed version control system that records every change made to a project.

Instead of creating multiple folders like:

```text
Project Final
Project Final 2
Project Latest
Project Final Final
```

Git maintains a complete history of changes in a structured manner.

Git allows us to:

- Save changes (Commit)
- Create isolated development branches
- Merge completed work
- Restore previous versions
- Compare changes
- Collaborate with multiple developers

Think of Git as the complete history of your project.

---

# 3. What is GitHub?

GitHub is a cloud platform that hosts Git repositories.

GitHub provides:

- Remote backups
- Collaboration
- Pull Requests
- Issue Tracking
- CI/CD Integration
- Code Reviews
- Project Boards
- Release Management

Git manages version history.

GitHub manages collaboration.

---

# 4. Why Version Control Matters

Without version control:

- Bugs are difficult to trace.
- Previous code is lost.
- Team collaboration becomes chaotic.
- Deployment becomes risky.
- Mistakes are irreversible.

With Git:

- Every change has a history.
- Every feature is isolated.
- Every bug can be traced.
- Every release can be restored.

Version control is mandatory in professional software engineering.

---

# 5. Git Workflow Philosophy

Our workflow follows several core principles.

## Never Develop Directly on Main

The `main` branch should always contain stable, production-ready code.

New work should always be developed in separate branches.

---

## Small Commits

Each commit should represent one logical change.

Good:

- Add JWT authentication
- Fix login validation
- Implement chat history

Bad:

- Update everything

---

## Clear Commit History

The commit history should tell the story of the project.

Anyone reading the history should understand:

- What changed
- Why it changed
- When it changed

---

## Frequent Commits

Commit regularly.

Do not wait until the end of the day.

Frequent commits make debugging easier.

---

# 6. Branching Strategy

Our project follows a simplified Git Flow strategy.

```text
main
│
├── develop
│
├── feature/authentication
├── feature/chat
├── feature/ai-service
├── feature/database
├── feature/rag
│
├── bugfix/login-error
├── bugfix/chat-history
│
├── hotfix/security-patch
│
└── release/v1.0.0
```

This structure keeps development organized and scalable.

---

# 7. Branch Responsibilities

## main

Purpose:

- Production-ready code
- Stable releases
- Tagged versions

Rules:

- Never commit directly.
- Merge only reviewed code.
- Always deployable.

---

## develop

Purpose:

- Integration branch
- Combines completed features
- Used for testing before release

Rules:

- Receives feature branches.
- Merges into main only after verification.

For small personal projects, `develop` can be omitted, but understanding it prepares you for industry workflows.

---

## feature/

Examples:

```text
feature/authentication

feature/chat

feature/ai-provider

feature/rag
```

Each branch focuses on a single feature.

---

## bugfix/

Examples:

```text
bugfix/login

bugfix/database-timeout

bugfix/token-expiry
```

Used to fix issues discovered during development.

---

## hotfix/

Examples:

```text
hotfix/security

hotfix/payment-error
```

Used for urgent fixes in production.

Hotfixes are merged directly into `main` and then back into `develop`.

---

## release/

Examples:

```text
release/v1.0.0

release/v2.0.0
```

Used for preparing a production release.

Only testing, documentation, and minor fixes occur here.

---

# 8. Commit Message Convention

Every commit should follow a consistent format.

Format:

```text
type: short description
```

---

## Common Types

| Type | Purpose |
|-------|----------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation |
| style | Formatting only |
| refactor | Code restructuring |
| test | Tests |
| chore | Maintenance |
| perf | Performance improvements |
| build | Build configuration |
| ci | CI/CD changes |

---

## Examples

```text
feat: add JWT authentication

feat: implement Gemini provider

fix: resolve login validation bug

docs: update project bible

refactor: simplify AI service

test: add authentication tests

chore: update dependencies
```

Avoid messages like:

```text
update

changes

fixed

final

done

test
```

They provide no useful information.

---

# 9. Pull Request Workflow

A Pull Request (PR) is a request to merge one branch into another.

Workflow:

```text
Create Feature Branch

↓

Develop Feature

↓

Commit Changes

↓

Push Branch

↓

Open Pull Request

↓

Code Review

↓

Address Feedback

↓

Merge

↓

Delete Feature Branch
```

Benefits:

- Peer review
- Automated testing
- Documentation
- Discussion
- Quality assurance

Even in solo projects, using Pull Requests builds good habits.

---

# 10. Merge Strategy

We prefer **Squash and Merge** for feature branches.

Benefits:

- Cleaner history
- One commit per feature
- Easier rollback
- Simpler release notes

Example:

Instead of:

```text
20 small commits
```

Main receives:

```text
feat: implement authentication system
```

This keeps the history concise and meaningful.

---

# 11. Repository Structure

Our GitHub repository should remain clean and organized.

Example:

```text
AI-Research-Knowledge-Assistant/

frontend/

backend/

docs/

docker/

scripts/

README.md

LICENSE

.gitignore

docker-compose.yml
```

Recommended repository additions:

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- CHANGELOG.md
- SECURITY.md

These files improve collaboration and professionalism.

---

# 12. .gitignore Strategy

Some files should never be committed.

Examples:

```text
.env

venv/

node_modules/

__pycache__/

.pytest_cache/

.next/

dist/

build/

coverage/

*.log

.DS_Store

.vscode/settings.json
```

Reasons:

- Security
- Reduced repository size
- Avoid generated files
- Prevent machine-specific configuration

Always commit:

```text
.env.example
```

Never commit:

```text
.env
```

---

# 13. Versioning Strategy

We follow **Semantic Versioning (SemVer)**.

Format:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.0.0
```

---

## MAJOR

Breaking changes.

Example:

```text
1.0.0

↓

2.0.0
```

---

## MINOR

New features without breaking compatibility.

Example:

```text
1.1.0
```

---

## PATCH

Bug fixes.

Example:

```text
1.1.2
```

---

## Example Timeline

```text
0.1.0

↓

0.2.0

↓

0.5.0

↓

1.0.0

↓

1.1.0

↓

1.1.1

↓

2.0.0
```

During development, versions below `1.0.0` indicate that the project is still evolving.

---

# 14. Release Workflow

A production release follows these steps:

```text
Feature Complete

↓

Merge into Develop

↓

Testing

↓

Create Release Branch

↓

Final Bug Fixes

↓

Merge into Main

↓

Create Git Tag

↓

Deploy

↓

Monitor
```

Each release should include:

- Updated documentation
- Passing tests
- Release notes
- Version tag

---

# 15. Daily Development Workflow

A typical development day:

```text
Pull Latest Code

↓

Create Feature Branch

↓

Implement Feature

↓

Run Tests

↓

Format Code

↓

Commit Changes

↓

Push Branch

↓

Open Pull Request

↓

Review

↓

Merge
```

Following this workflow consistently reduces integration problems.

---

# 16. Best Practices

- Commit frequently.
- Write meaningful commit messages.
- Keep commits focused.
- Pull changes before starting work.
- Rebase or merge regularly to stay updated.
- Delete merged feature branches.
- Protect the `main` branch.
- Review code before merging.
- Tag production releases.
- Keep documentation synchronized with code changes.

---

# 17. Common Mistakes

Avoid:

- Committing directly to `main`.
- Large "everything" commits.
- Vague commit messages.
- Committing secrets or API keys.
- Ignoring merge conflicts.
- Leaving stale branches in the repository.
- Using Git as a backup instead of version control.
- Skipping code reviews.
- Forgetting to update documentation after significant changes.

These practices can lead to confusion, security issues, and maintenance challenges.

---

# 18. Chapter Summary

This chapter established the Git workflow for the AI Research & Knowledge Assistant.

We defined how code moves from development to production through branches, commits, pull requests, and releases. By following a consistent workflow, we maintain a clean project history, improve collaboration, and reduce the risk of introducing bugs into the main codebase.

Version control is not just a tool—it is an essential engineering practice that supports traceability, accountability, and long-term maintainability. The workflow defined here will be followed throughout every phase of this project.

---

## End of Chapter 7
