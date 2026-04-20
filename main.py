# Entry point for the FastAPI learning project.
# Run with: uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from database import engine, Base

# Create all ORM tables on startup if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Learning Project", version="1.0.0")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return {
        "message": "FastAPI learning project",
        "docs": "/docs",
        "note": "See individual module files for focused examples",
    }
