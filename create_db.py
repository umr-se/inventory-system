# create_db.py
from app.db import Base, engine
from app.models import InventoryItem

Base.metadata.create_all(bind=engine)
