from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, EmailStr
from app.supabase_client import supabase

router = APIRouter()  # ✅ This creates the route group

# --- Signup ---
class SignupRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/signup")
def signup(data: SignupRequest):
    response = supabase.auth.sign_up({
        "email": data.email,
        "password": data.password
    })

    if response.user is None:
        raise HTTPException(status_code=400, detail="Signup failed.")

    return {"message": "User created", "user_id": response.user.id}


# --- Login ---
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
def login(data: LoginRequest):
    response = supabase.auth.sign_in_with_password({
        "email": data.email,
        "password": data.password
    })

    if response.user is None or response.session is None:
        raise HTTPException(status_code=401, detail="Login failed. Check credentials or email confirmation settings.")

    return {
        "message": "Login successful",
        "access_token": response.session.access_token,
        "refresh_token": response.session.refresh_token,
        "user_id": response.user.id
    }

# --- Redirect Success Page ---
@router.get("/success", response_class=HTMLResponse)
def success_page():
    return "<h1>Password reset successful! You can close this window.</h1>"
