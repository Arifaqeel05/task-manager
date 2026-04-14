from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="A task manager built to learn FastAPI",
    version="0.1.0",
)

@app.get("/")
def Home():
    return {"message": "Welcome to the Task Manager API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

