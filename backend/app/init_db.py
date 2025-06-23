from .database import Base, engine
from . import models

print("📦 Creating tables in the database...")
Base.metadata.create_all(bind=engine)
print("✅ Done.")
