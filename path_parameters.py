# Demonstrates path parameter extraction, query params, and 404 handling.
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

posts = [
    {"id": 1, "title": "First Post",  "content": "Hello"},
    {"id": 2, "title": "Second Post", "content": "World"},
]


@app.get("/app/post/{post_id}")
def get_post_simple(post_id: int):
    return {"post_id": post_id}


# Returns 200 even when the post is missing — illustrates the problem with silent failures
@app.get("/api/posts/no-error/{post_id}")
def get_post_no_error(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"Not Found": f"Post with id {post_id} not found"}


# Correct version: raises a proper 404 so the client knows the resource is missing
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found",
    )
