from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService


def test_register_user_creates_user_and_hashes_password():
    engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        repo = UserRepository(db)
        service = AuthService(repo)

        # Use a password >= 8 chars (schema) and short enough for bcrypt
        user_in = UserCreate(email="alice@example.com", password="password9", full_name="Alice")
        user = service.register_user(user_in)


        assert user.id is not None
        assert user.email == user_in.email
        assert user.full_name == user_in.full_name
        assert user.password_hash != user_in.password
    finally:
        db.close()


def test_register_user_rejects_duplicate_email():
    engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        repo = UserRepository(db)
        service = AuthService(repo)

        user_in = UserCreate(email="alice@example.com", password="password12345", full_name="Alice")

        service.register_user(user_in)

        duplicate = UserCreate(email="alice@example.com", password="password456", full_name="Alice 2")
        try:
            service.register_user(duplicate)
            assert False, "Expected HTTPException"
        except Exception as exc:
            assert "Email already registered" in str(exc)
    finally:
        db.close()

