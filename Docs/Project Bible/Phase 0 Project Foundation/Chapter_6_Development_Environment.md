# Phase 0 — Project Foundation

# Chapter 6 — Development Environment

> Version: 1.0
>
> Status: Completed
>
> Phase: 0 — Project Foundation
>
> Chapter: 6 — Development Environment

---

# Table of Contents

1. Introduction
2. Development Environment Philosophy
3. Required Software
4. Development Tools
5. IDE Selection
6. Python Environment
7. Node.js Environment
8. Git Setup
9. Docker Setup
10. Environment Variables
11. Project Initialization
12. Recommended VS Code Extensions
13. Recommended Antigravity IDE Extensions
14. Development Workflow
15. Best Practices
16. Common Mistakes
17. Chapter Summary

---

# 1. Introduction

Before writing the first line of code, every developer should have a consistent and reliable development environment.

A development environment includes all the software, tools, configurations, and dependencies required to build, run, test, and debug the application.

Having a standardized setup ensures:

- Every developer works in the same environment.
- Projects behave consistently across different machines.
- Dependency issues are minimized.
- Onboarding new developers becomes straightforward.
- Deployment environments closely match local development.

Throughout this project, we will use industry-standard tools that are widely adopted in professional software development.

---

# 2. Development Environment Philosophy

Our development environment is designed around five principles:

- **Consistency** – Every team member uses the same tools and configurations.
- **Productivity** – Tools should help us write code faster and with fewer errors.
- **Scalability** – The environment should support future project growth.
- **Automation** – Repetitive tasks should be automated wherever possible.
- **Portability** – The project should run consistently on Windows, Linux, and macOS.

---

# 3. Required Software

The following software is required to develop and run the project.

| Software | Purpose |
|----------|---------|
| Python | Backend development |
| Node.js | Frontend development |
| npm | Package management |
| Git | Version control |
| Docker Desktop | Containerization |
| PostgreSQL (optional locally) | Database |
| VS Code or Antigravity IDE | Code editor |
| Chrome/Edge | Testing |

---

# 4. Development Tools

## Python

Purpose:

- Backend language
- FastAPI framework
- AI integration
- Database communication

Recommended Version:

```text
Python 3.12+
```

Why?

- Stable
- Fast
- Excellent library support
- Compatible with FastAPI ecosystem

---

## Node.js

Purpose:

- Next.js runtime
- Package management
- Build system

Recommended Version

```text
Node.js LTS (Latest Stable)
```

Avoid experimental releases for production projects.

---

## npm

Purpose

- Install frontend dependencies
- Manage scripts
- Build project
- Run development server

Example:

```bash
npm install

npm run dev

npm run build
```

---

## Git

Purpose

- Version control
- Collaboration
- Branch management
- History tracking

Every code change should be committed through Git.

---

## Docker Desktop

Purpose

- Run containers
- Standardize environments
- Eliminate "works on my machine" problems

Docker becomes increasingly important as the project grows.

---

# 5. IDE Selection

A powerful IDE significantly improves developer productivity.

For this project, we officially support:

- Visual Studio Code
- Antigravity IDE

Both editors can successfully build and maintain the project.

---

# Visual Studio Code (VS Code)

## Overview

Visual Studio Code is Microsoft's lightweight, extensible code editor.

It is one of the most widely used IDEs for modern web, backend, and AI development.

---

## Why We Recommend VS Code

- Excellent FastAPI support
- Excellent Next.js support
- Strong TypeScript integration
- Rich extension ecosystem
- Built-in Git support
- Integrated terminal
- Docker integration
- Database extensions
- Debugging tools
- Cross-platform

---

## Best Use Cases

VS Code is ideal for developers who prefer:

- Traditional development
- Maximum customization
- Stable ecosystem
- Large extension marketplace

---

# Antigravity IDE

## Overview

Antigravity IDE is an AI-first integrated development environment designed to enhance software development through deep AI assistance.

Unlike traditional editors where AI is an extension, Antigravity places AI at the center of the development workflow.

---

## Why We Include It

Our project is heavily focused on AI engineering.

Antigravity can significantly improve productivity by assisting with:

- Code generation
- Refactoring
- Architecture understanding
- Documentation
- Error explanation
- Codebase navigation
- AI-assisted debugging

It complements the Project Bible by helping developers understand and implement the documented architecture.

---

## Advantages

- AI-native development experience
- Better context awareness
- Faster code generation
- Intelligent project understanding
- Built-in AI chat
- Helpful for large codebases

---

## Considerations

- Still evolving compared to VS Code
- Smaller extension ecosystem
- Some workflows may differ from traditional editors

---

## Best Use Cases

Antigravity is particularly useful for:

- Learning new technologies
- Large-scale refactoring
- AI-assisted development
- Understanding unfamiliar codebases
- Generating boilerplate code

---

## Which IDE Should You Choose?

| Scenario | Recommended IDE |
|-----------|-----------------|
| Traditional software development | VS Code |
| AI-assisted development | Antigravity IDE |
| Learning | Either |
| Team collaboration | VS Code |
| Maximum AI productivity | Antigravity IDE |

Regardless of the editor, the project's architecture, folder structure, and coding standards remain identical.

---

# 6. Python Environment

Every Python project should use an isolated virtual environment.

Why?

Without virtual environments:

- Package conflicts occur.
- Different projects require different versions.
- Global Python installation becomes cluttered.

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate (Windows)

```bash
venv\Scripts\activate
```

---

## Activate (Linux/macOS)

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Freeze Dependencies

```bash
pip freeze > requirements.txt
```

---

# 7. Node.js Environment

Install project dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Create production build:

```bash
npm run build
```

Always use the project's `package.json` as the single source of truth for frontend dependencies.

---

# 8. Git Setup

Verify installation:

```bash
git --version
```

Configure identity:

```bash
git config --global user.name "Your Name"

git config --global user.email "your@email.com"
```

Initialize repository (if needed):

```bash
git init
```

Check status:

```bash
git status
```

Commit changes:

```bash
git add .

git commit -m "feat: initial project setup"
```

Git workflows will be covered in the next chapter.

---

# 9. Docker Setup

Install:

- Docker Desktop

Verify installation:

```bash
docker --version

docker compose version
```

Start services:

```bash
docker compose up
```

Stop services:

```bash
docker compose down
```

Docker ensures that every developer runs the same application stack regardless of their operating system.

---

# 10. Environment Variables

Sensitive configuration should never be hardcoded.

Instead, store it in environment variables.

Example:

```env
DATABASE_URL=

JWT_SECRET=

JWT_ALGORITHM=

ACCESS_TOKEN_EXPIRE_MINUTES=

AI_PROVIDER=

GEMINI_API_KEY=

OPENAI_API_KEY=

GROQ_API_KEY=

OPENROUTER_API_KEY=
```

---

## Why Environment Variables?

They allow different configurations for:

- Development
- Testing
- Staging
- Production

without modifying source code.

---

## Security Rules

Never commit:

- .env

Always commit:

- .env.example

This protects secrets while documenting required configuration.

---

# 11. Project Initialization

Clone repository:

```bash
git clone <repository-url>
```

Move into project:

```bash
cd AI-Research-Knowledge-Assistant
```

Backend setup:

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Frontend setup:

```bash
cd frontend

npm install
```

Start backend:

```bash
uvicorn app.main:app --reload
```

Start frontend:

```bash
npm run dev
```

The application is now ready for development.

---

# 12. Recommended VS Code Extensions

| Extension | Purpose |
|-----------|---------|
| Python | Python support |
| Pylance | IntelliSense |
| Black Formatter | Python formatting |
| Ruff | Fast linting |
| ESLint | JavaScript/TypeScript linting |
| Prettier | Code formatting |
| Tailwind CSS IntelliSense | Tailwind autocomplete |
| Docker | Docker integration |
| GitLens | Git insights |
| Error Lens | Inline error highlighting |
| Thunder Client or REST Client | API testing |
| PostgreSQL | Database management |
| Material Icon Theme | Better file icons |
| Path Intellisense | Path autocomplete |

These extensions improve productivity and help maintain consistent code quality.

---

# 13. Recommended Antigravity IDE Features

While Antigravity shares compatibility with many VS Code extensions, its built-in AI capabilities are its primary strength.

Recommended usage:

- AI code generation
- AI code review
- Architecture explanation
- Documentation generation
- Bug investigation
- Refactoring assistance
- Intelligent navigation
- Project-wide code understanding

Use AI suggestions as a productivity aid, but always review generated code for correctness, security, and consistency with the project's architecture.

---

# 14. Development Workflow

Our daily development process follows these steps:

```text
Pull Latest Changes
        │
        ▼
Create Feature Branch
        │
        ▼
Implement Feature
        │
        ▼
Run Tests
        │
        ▼
Format & Lint Code
        │
        ▼
Commit Changes
        │
        ▼
Push Branch
        │
        ▼
Create Pull Request
        │
        ▼
Code Review
        │
        ▼
Merge into Main
```

This workflow encourages collaboration, traceability, and code quality.

---

# 15. Best Practices

- Use a virtual environment for every Python project.
- Keep dependencies up to date.
- Install packages only through the project's dependency files.
- Never hardcode secrets.
- Commit small, meaningful changes.
- Keep local and remote repositories synchronized.
- Format and lint code before committing.
- Review AI-generated code before accepting it.
- Regularly update your development tools.

---

# 16. Common Mistakes

Avoid the following:

- Installing Python packages globally.
- Committing `.env` files.
- Ignoring dependency version conflicts.
- Running outdated Node.js or Python versions.
- Mixing project dependencies across different environments.
- Skipping code formatting and linting.
- Relying blindly on AI-generated code.
- Developing directly on the `main` branch.

---

# 17. Chapter Summary

This chapter established the standard development environment for the AI Research & Knowledge Assistant.

We selected modern, production-ready tools for backend development, frontend development, version control, containerization, and code editing. By standardizing our environment, we ensure that every developer works with the same toolchain, reducing inconsistencies and simplifying collaboration.

Whether using Visual Studio Code or Antigravity IDE, the project's architecture and workflow remain unchanged. The development environment defined here provides a stable foundation for implementing every feature described in the Project Bible.

---

## End of Chapter 6
