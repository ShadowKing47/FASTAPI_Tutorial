# Demonstrates a POST endpoint that creates a resource and returns HTTP 201.
from fastapi import FastAPI, status
from pydantic import BaseModel
import datetime

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "title": "First Post",
        "content": "Hello",
        "author": "Alice",
        "date_created": datetime.datetime.now(),
    }
]


class PostCreate(BaseModel):
    title: str
    content: str
    author: str


class Post(PostCreate):
    id: int
    date_created: datetime.datetime


@app.post("/api/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id = posts[-1]["id"] + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "date_created": datetime.datetime.now(),
    }
    posts.append(new_post)
    return new_post
