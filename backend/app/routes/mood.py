from fastapi import Depends, HTTPException
from gotrue.types import User
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from app.dependencies.auth import get_current_user
from app.supabase_client import supabase

router = APIRouter()

class MoodEntry(BaseModel):
    mood: str
    timestamp: datetime
    note: str | None = None

@router.post("/log-mood")
def log_mood(entry: MoodEntry, user: User = Depends(get_current_user)):
    supabase.table("mood_entries").insert({
        "user_id": user.id,
        "mood": entry.mood,
        "note": entry.note,
        "timestamp": entry.timestamp.isoformat()
    }).execute()

    return {"message": "Mood entry logged"}



from fastapi import Query
from typing import Optional

@router.get("/get-moods")
def get_moods(limit: int = 20, user: User = Depends(get_current_user)):
    try:
        response = (
            supabase
            .table("mood_entries")
            .select("*")
            .eq("user_id", user.id)
            .order("timestamp", desc=True)
            .limit(limit)
            .execute()
        )

        return {"message": "Mood history retrieved", "data": response.data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




