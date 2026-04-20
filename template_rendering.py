# Demonstrates Jinja2 template rendering for HTML responses in FastAPI.
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

posts = [
    {"id": 1, "title": "First Post",  "content": "Hello"},
    {"id": 2, "title": "Second Post", "content": "World"},
]


# include_in_schema=False hides this route from the auto-generated OpenAPI docs
@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return templates.TemplateResponse(
                "post.html", {"request": request, "post": post}
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found",
    )
