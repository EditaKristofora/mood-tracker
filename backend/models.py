from pydantic import BaseModel
from datetime import datetime

class MoodEntry(BaseModel):
    user_id: str
    mood: str
    timestamp: datetime
    note: str | None = None
