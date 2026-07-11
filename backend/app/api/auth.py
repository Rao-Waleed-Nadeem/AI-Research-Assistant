from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserResponse, Token
from app.db.session import get_db
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))

@router.post("/register", response_model=UserResponse)
def register(user_in: UserCreate, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.register_user(user_in)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(get_auth_service)):
    # OAuth2 uses username field for the unique identifier (we use email)
    user = auth_service.authenticate_user(email=form_data.username, password=form_data.password) 
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
