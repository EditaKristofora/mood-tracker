import sys
import os
sys.path.append(os.path.dirname(__file__))  # ✅ Add backend/ to Python path
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware  # 👈 ADD THIS
from app.routes import auth, mood

app = FastAPI()

# 👇 ADD THIS CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://editakristofora.github.io"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(mood.router)

# Add custom security scheme for Swagger Authorize button
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
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))  # 👈 Render uses $PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port)
