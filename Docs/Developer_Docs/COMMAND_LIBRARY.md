# COMMAND_LIBRARY.md

# AI Research Assistant

## AI Agent Command Library

> Version: 1.0
>
> This document contains the official commands for interacting with AI coding agents during the entire project lifecycle.
>
> Always use these commands instead of creating new prompts whenever possible.
>
> These commands assume the existence of:
>
> - AGENT_GUIDE.md
> - IMPLEMENTATION_ORDER.md
> - PROJECT_STATUS.md
> - SESSION_HANDOFF.md
>
> The AI agent should automatically read these documents whenever required.

---

# General Rules

The AI should always

- Read required project documents.
- Follow project architecture.
- Never skip implementation order.
- Never implement unrelated features.
- Update documentation after implementation.
- Stop after completing the requested task.

---

# 1. Analyze Project

## Purpose

Used when starting a new AI session.

## Command

```text
Analyze the project.

Read:

- AGENT_GUIDE.md
- IMPLEMENTATION_ORDER.md
- PROJECT_STATUS.md
- SESSION_HANDOFF.md

Explain your understanding of:

- Current architecture
- Current implementation status
- Next feature
- Current blockers

Do not write any code.
```

---

# 2. Continue Development

## Purpose

Continue exactly where the previous session ended.

## Command

```text
Continue development.

Read:

- AGENT_GUIDE.md
- IMPLEMENTATION_ORDER.md
- PROJECT_STATUS.md
- SESSION_HANDOFF.md

Determine the next task.

If the required feature specification does not exist:

Generate it.

Then wait for my approval.

Do not write production code yet.
```

---

# 3. Generate Feature Specification

## Purpose

Generate implementation documentation before coding.

## Command

```text
Generate the Feature Specification for the next pending feature.

Use:

- Project Bible
- AGENT_GUIDE.md
- Existing Architecture

Include:

- Objective
- Folder Structure
- Models
- Schemas
- Repositories
- Services
- Routes
- APIs
- Validation
- Dependencies
- Testing Checklist

Save as:

FEATURE_<FEATURE>.md

Do not implement any code.
```

---

# 4. Implement Feature

## Purpose

Implement one complete feature.

## Command

```text
Implement the approved feature.

Read:

- AGENT_GUIDE.md
- PROJECT_STATUS.md
- SESSION_HANDOFF.md
- FEATURE_<FEATURE>.md

Requirements

- Follow project architecture.
- Follow coding standards.
- Do not modify unrelated modules.
- Use Repository Pattern.
- Use Service Layer.
- Use Dependency Injection.
- Use Providers where required.

After completion

- Update PROJECT_STATUS.md
- Update SESSION_HANDOFF.md

Stop.
```

---

# 5. Continue Current Feature

## Purpose

Resume unfinished work.

## Command

```text
Continue implementing the current feature.

Read:

PROJECT_STATUS.md

SESSION_HANDOFF.md

Continue from the exact stopping point.

Do not restart the implementation.
```

---

# 6. Review Implementation

## Purpose

Review completed work.

## Command

```text
Review the implementation.

Check

- Architecture
- Folder Structure
- SOLID
- DRY
- Error Handling
- Validation
- Security
- Scalability
- Performance
- Naming
- Documentation

Do not modify code.

Provide recommendations only.
```

---

# 7. Refactor Module

## Purpose

Improve existing code.

## Command

```text
Refactor only the requested module.

Goals

- Improve readability
- Reduce duplication
- Increase maintainability

Do not change behavior.

Do not modify unrelated files.
```

---

# 8. Fix Bug

## Purpose

Resolve issues safely.

## Command

```text
Analyze the reported bug.

Find

- Root cause
- Impact
- Best solution

Explain your findings.

Wait for approval before modifying code.
```

---

# 9. Generate Tests

## Purpose

Generate testing files.

## Command

```text
Generate tests for the selected feature.

Include

- Unit Tests
- Integration Tests
- API Tests

Do not modify production code.
```

---

# 10. Improve Performance

## Purpose

Optimize implementation.

## Command

```text
Analyze performance.

Suggest improvements for

- Database
- API
- AI
- Memory
- Response Time

Do not implement changes until approved.
```

---

# 11. Improve Security

## Purpose

Security review.

## Command

```text
Perform a security review.

Check

- Authentication
- Authorization
- Input Validation
- SQL Injection
- Secrets
- Environment Variables
- API Security

Provide recommendations only.
```

---

# 12. Update Documentation

## Purpose

Synchronize documentation.

## Command

```text
Update

- PROJECT_STATUS.md
- SESSION_HANDOFF.md

If architecture changed

Update the relevant Project Bible chapter.

Do not modify code.
```

---

# 13. Generate Git Commit

## Purpose

Create meaningful commits.

## Command

```text
Generate a professional Git commit message.

Follow Conventional Commits.

Include

- Type
- Scope
- Summary
```

---

# 14. Prepare Pull Request

## Purpose

Generate PR description.

## Command

```text
Generate a Pull Request.

Include

- Summary
- Changes
- Testing
- Notes
- Known Issues
```

---

# 15. End Session

## Purpose

Properly close a development session.

## Command

```text
Before ending

Verify

- Feature completed
- Tests completed
- Documentation updated
- PROJECT_STATUS.md updated
- SESSION_HANDOFF.md updated

Then prepare the project for the next session.
```

---

# 16. Emergency Recovery

## Purpose

Recover from interrupted sessions.

## Command

```text
Recover the project.

Read

- AGENT_GUIDE.md
- IMPLEMENTATION_ORDER.md
- PROJECT_STATUS.md
- SESSION_HANDOFF.md

Analyze

- Current project state
- Last completed task
- Incomplete work
- Next recommended step

Do not write code.
```

---

# 17. Project Audit

## Purpose

Review the entire project.

## Command

```text
Audit the entire project.

Review

- Architecture
- Folder Structure
- APIs
- Database
- AI
- Security
- Documentation
- Testing

Provide a detailed report.

Do not modify code.
```

---

# Quick Commands

These commands are intended for daily development.

| Command              | Action                                            |
| -------------------- | ------------------------------------------------- |
| **Analyze**          | Analyze current project state                     |
| **Continue**         | Continue previous session                         |
| **Next Feature**     | Determine next feature and generate specification |
| **Implement**        | Implement approved feature                        |
| **Continue Feature** | Resume current feature                            |
| **Review**           | Review implementation                             |
| **Refactor**         | Refactor selected module                          |
| **Fix Bug**          | Analyze and fix bug                               |
| **Generate Tests**   | Create test files                                 |
| **Performance**      | Analyze performance                               |
| **Security**         | Perform security review                           |
| **Update Docs**      | Update documentation                              |
| **Commit**           | Generate Git commit                               |
| **Pull Request**     | Generate PR description                           |
| **End Session**      | Close development session                         |
| **Recover**          | Recover interrupted work                          |
| **Audit**            | Audit the entire project                          |

---

# Recommended Development Workflow

```text
Start Session

↓

Analyze

↓

Next Feature

↓

Generate Feature Specification

↓

Review Specification

↓

Implement Feature

↓

Test

↓

Review

↓

Update Documentation

↓

Commit

↓

End Session
```

---

# Final Rule

The AI agent should always prioritize:

1. Correctness
2. Maintainability
3. Scalability
4. Clean Architecture
5. Consistency

Never sacrifice architecture for speed.

---

## End of COMMAND_LIBRARY.md
