from datetime import timedelta
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user_in: UserCreate):
        if self.user_repo.get_by_email(user_in.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        if self.user_repo.get_by_username(user_in.username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
        
        password_hash = get_password_hash(user_in.password)
        return self.user_repo.create(user_in, password_hash)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repo.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user

    def create_token_for_user(self, user):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        return access_token
