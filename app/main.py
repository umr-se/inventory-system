from unittest.mock import Base
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn
from . import init_db
from .db import SessionLocal
from .sync import sync_sheet_to_db
from .report import generate_report
from app.db import engine

init_db()
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root():
    return{"welcome!!"}

@app.get("/sync")
def sync_sheet(db: Session = Depends(get_db)):
    sync_sheet_to_db(db)
    return {"message": "Sheet synced successfully."}

@app.get("/generate-report")
def report(db: Session = Depends(get_db)):
    link = generate_report(db)
    return {"report": link}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)