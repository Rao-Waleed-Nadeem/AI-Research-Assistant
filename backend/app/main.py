from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(title="AI Knowledge Assistant API", version="0.0.0")

app.include_router(auth_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}

