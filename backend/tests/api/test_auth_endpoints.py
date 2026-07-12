from __future__ import annotations

from datetime import datetime, timedelta, timezone

from fastapi.testclient import TestClient
from jose import jwt

from app.core.security import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


def test_register_login_me_flow(client: TestClient):
    # Register
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "alice@example.com",
            "password": "password9",
            "full_name": "Alice",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "alice@example.com"
    assert data["full_name"] == "Alice"
    assert "password_hash" not in data

    # Login (OAuth2PasswordRequestForm)
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "alice@example.com", "password": "password9"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"

    token = token_data["access_token"]

    # /me with token
    me_response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    me = me_response.json()
    assert me["email"] == "alice@example.com"


def test_register_duplicate_email_fails(client: TestClient):
    payload = {"email": "bob@example.com", "password": "password123", "full_name": "Bob"}

    first = client.post("/api/v1/auth/register", json=payload)
    assert first.status_code == 200

    second = client.post("/api/v1/auth/register", json={**payload, "full_name": "Bobby"})
    assert second.status_code == 400
    assert second.json()["detail"] == "Email already registered"


def test_login_incorrect_password_fails(client: TestClient):
    payload = {"email": "carol@example.com", "password": "password123", "full_name": "Carol"}
    created = client.post("/api/v1/auth/register", json=payload)
    assert created.status_code == 200

    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "carol@example.com", "password": "wrongpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_response.status_code == 401
    assert login_response.json()["detail"] == "Incorrect email or password"


def test_me_with_invalid_token_fails(client: TestClient):
    me_response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer invalid.jwt.token"},
    )
    assert me_response.status_code == 401


def test_me_with_expired_token_fails(client: TestClient):
    # Create a token with an expired exp.
    now = datetime.now(timezone.utc)
    expired = now - timedelta(minutes=1)

    token = jwt.encode({"sub": "1", "exp": expired}, SECRET_KEY, algorithm=ALGORITHM)

    me_response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 401

