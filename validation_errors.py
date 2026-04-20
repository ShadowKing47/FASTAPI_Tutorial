# Demonstrates a custom handler for Pydantic's RequestValidationError (HTTP 422).
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Flatten Pydantic's nested error list into a simpler field → message structure
    errors = [
        {
            "field":   ".".join(str(loc) for loc in err["loc"]),
            "message": err["msg"],
        }
        for err in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"errors": errors})
