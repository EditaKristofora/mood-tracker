from fastapi import Header, HTTPException, Depends
from app.supabase_client import supabase
from gotrue.errors import AuthApiError

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.replace("Bearer ", "")
    try:
        user_response = supabase.auth.get_user(token)
        user = user_response.user  # ✅ Extract actual user
        return user
    except AuthApiError as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
