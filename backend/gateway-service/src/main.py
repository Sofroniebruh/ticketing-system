import uvicorn
from fastapi import FastAPI
from src.router import router as gateway_router

app = FastAPI(title="Gateway Service")

app.include_router(gateway_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
