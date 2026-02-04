import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "clerk_jwks_url": os.getenv("CLERK_JWKS_URL", "NOT SET"),
        "openai_key_set": bool(os.getenv("OPENAI_API_KEY"))
    }
