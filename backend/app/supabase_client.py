import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()  # 👈 Make sure this line is present and at the top

SUPABASE_URL = os.getenv("SUPABASE_URL")  # 👈 variable name as string, NOT the actual URL
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Missing SUPABASE_URL or SUPABASE_KEY in environment variables")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)



