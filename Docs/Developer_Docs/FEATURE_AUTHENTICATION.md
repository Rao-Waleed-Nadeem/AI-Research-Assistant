# Feature Specification: Authentication (Phase 3)

## Objective
Implement a secure, stateless authentication system using JSON Web Tokens (JWT). This module handles user registration, secure login via password hashing, and provides a generic dependency to securely identify the current user across all protected application routes.

## Folder Structure
```text
app/
├── api/
│     └── auth.py
├── core/
│     └── security.py
├── dependencies/
│     └── auth.py
├── models/
│     └── user.py
├── repositories/
│     └── user_repository.py
├── schemas/
│     └── user.py
└── services/
      └── auth_service.py
```

## Models
- **User (`app/models/user.py`)**
  - `id`: Integer (Primary Key)
  - `full_name`: String
  - `email`: String (Unique, Indexed)
  - `password_hash`: String (Hashed via bcrypt)
  - `is_active`: Boolean (Default: True)
  - `created_at`: DateTime (Default: UTC now)
  - `updated_at`: DateTime (Default: UTC now on update)

## Schemas
- **UserCreate (`app/schemas/user.py`)**: `email` (EmailStr), `password` (str), `full_name` (str)
- **UserLogin (`app/schemas/user.py`)**: `email` (EmailStr), `password` (str)
- **UserResponse (`app/schemas/user.py`)**: `id`, `email`, `full_name`, `is_active`
- **Token (`app/schemas/user.py`)**: `access_token` (str), `token_type` (str)
- **TokenPayload (`app/schemas/user.py`)**: `sub` (str - User ID)

## Repositories
- **UserRepository (`app/repositories/user_repository.py`)**
  - `get_by_email(email: str) -> User | None`
  - `get_by_id(user_id: int) -> User | None`
  - `create(user: UserCreate) -> User`

## Services
- **AuthService (`app/services/auth_service.py`)**
  - `register_user(user_in: UserCreate) -> User`: Validates uniqueness, delegates hashing, and creates user.
  - `authenticate_user(email, password) -> User | None`: Retrieves user and verifies password hash.

## Routes
- **AuthRouter (`app/api/auth.py`)**

## APIs
- `POST /api/v1/auth/register`: Creates a new user account. Returns `UserResponse`.
- `POST /api/v1/auth/login`: Authenticates credentials. Returns `Token` (JWT).
- `GET /api/v1/auth/me`: Returns the current authenticated user's details (`UserResponse`).

## Validation
- Enforce valid email format via `pydantic.EmailStr`.
- Strong password validation (e.g., minimum length).
- Handled via Pydantic schemas before reaching the service layer.

## Dependencies
- **`app/dependencies/auth.py`**:
  - `get_current_user`: Requires `Depends(OAuth2PasswordBearer)`. Decodes the JWT, extracts the User ID (`sub`), and looks up the user using `UserRepository`. Raises 401 Unauthorized if token is invalid or user doesn't exist.
- **`app/core/security.py`**:
  - Contains `passlib` configuration for password hashing.
  - Contains `python-jose` logic for encoding and decoding JWTs.

## Testing Checklist
- [ ] Test successful user registration.
- [ ] Test registration fails if email already exists.
- [ ] Test successful login returns a JWT.
- [ ] Test login fails with invalid password or unregistered email.
- [ ] Test protected route (`/me`) succeeds with valid JWT.
- [ ] Test protected route (`/me`) fails with expired/invalid JWT.
