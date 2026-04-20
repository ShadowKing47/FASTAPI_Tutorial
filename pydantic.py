# Demonstrates Pydantic schema definitions, Field validation, and response_model usage.
from pydantic import BaseModel, EmailStr, Field
from typing import List
from fastapi import FastAPI

app = FastAPI()

# In-memory store (demo only — not thread-safe for production)
posts: list[dict] = [
    {"id": 1, "title": "First Post",  "content": "Hello", "author": "Alice"},
    {"id": 2, "title": "Second Post", "content": "World", "author": "Bob"},
]


class BaseUserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr


# Request body schema for creating or updating a post
class PostCreate(BaseModel):
    title: str   = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=1000)
    author: str  = Field(min_length=1, max_length=100)


# Response schema — extends PostCreate and adds the server-generated id
class PostResponse(PostCreate):
    id: int

    class Config:
        from_attributes = True  # allows building from ORM objects


# --- CRUD endpoints ---

@app.get("/api/posts", response_model=List[PostResponse])
def get_posts():
    return posts
