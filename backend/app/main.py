from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routes import auth, mood  # ✅ Corrected import

app = FastAPI()

# Include routes
app.include_router(auth.router)
app.include_router(mood.router)

# Add security schema to show Authorize button
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Mood Tracker API",
        version="1.0.0",
        description="Track and view your moods",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi





