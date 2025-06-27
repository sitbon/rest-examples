from fastapi import FastAPI
from app.routers import users
from app.settings import get_settings

settings = get_settings()

app = FastAPI(
    title="Foo Demo",
    description="A FastAPI + SQLAlchemy demo project for interview.",
    version="0.1.0",
)

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to Foo Demo!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
