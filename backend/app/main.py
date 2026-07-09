from fastapi import FastAPI

app = FastAPI(title="AI Knowledge Assistant API", version="0.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}

