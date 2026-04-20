# FastAPI Learning Project

A collection of focused example files covering core FastAPI and SQLAlchemy concepts — each file is a standalone runnable demo.

## Project Structure

```
.
├── main.py                  # App entry point (run this with uvicorn)
├── database.py              # SQLAlchemy engine, session factory, and Base
├── models.py                # ORM model definitions (User)
├── pydantic.py              # Pydantic schemas, Field validation, response_model
├── path_parameters.py       # Path params, query params, HTTPException 404
├── post_endpoints.py        # POST endpoint returning HTTP 201
├── template_rendering.py    # Jinja2 HTML template rendering
├── custom_handlers.py       # Custom HTTP exception handler (JSON vs HTML)
├── validation_errors.py     # Custom RequestValidationError handler (HTTP 422)
├── relationship.py          # SQLAlchemy Core table join (ForeignKey)
├── SQL1.py                  # Raw SQL + SQLAlchemy Core CRUD operations
├── home.html                # Jinja2 snippet: url_for link example
├── templates/
│   ├── home.html            # Post listing page
│   ├── post.html            # Single post detail page
│   └── error.html           # Error page (used by custom_handlers.py)
├── requirements.txt
└── .env                     # DATABASE_URL (not committed)
```

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy and configure environment variables
cp .env .env.local              # edit DATABASE_URL if needed

# 4. Start the development server
uvicorn main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

## What Each File Teaches

| File | Concept |
|------|---------|
| `database.py` | Engine setup, `SessionLocal`, `DeclarativeBase`, `get_db` dependency |
| `models.py` | ORM table mapping with `Mapped` / `mapped_column`, `@property` |
| `pydantic.py` | `BaseModel`, `Field` constraints, `response_model`, `List[Schema]` |
| `path_parameters.py` | Path params, type coercion, silent vs proper 404 comparison |
| `post_endpoints.py` | POST body parsing, HTTP 201, in-memory list mutation |
| `template_rendering.py` | `Jinja2Templates`, `TemplateResponse`, `include_in_schema=False` |
| `custom_handlers.py` | `@app.exception_handler`, content-negotiation (JSON vs HTML) |
| `validation_errors.py` | `RequestValidationError`, custom 422 error shape |
| `relationship.py` | `ForeignKey`, Core `.join()`, `select_from` |
| `SQL1.py` | Raw `text()` SQL, `MetaData`, `Table`, Core INSERT / SELECT / UPDATE / DELETE |

## Dependencies

```
fastapi
uvicorn[standard]
sqlalchemy
pydantic[email]
jinja2
python-multipart
```

## Running Individual Examples

Each file (except `database.py` and `models.py`) contains its own `app = FastAPI()` instance and can be run independently:

```bash
uvicorn path_parameters:app --reload
uvicorn post_endpoints:app --reload
uvicorn template_rendering:app --reload
# etc.
```

## Notes

- The `.env` file holds `DATABASE_URL`. Default is `sqlite:///./test.db`.
- `SQL1.py` and `relationship.py` run as plain scripts (`python SQL1.py`) — they do not start a web server.
- Templates live in `templates/` and are loaded by both `template_rendering.py` and `custom_handlers.py`.
