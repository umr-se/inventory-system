from google.oauth2 import service_account
from googleapiclient.discovery import build
from sqlalchemy.orm import Session
from .models import InventoryItem
import os

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = os.getenv("CREDENTIALS_GOOGLE")
SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

def get_sheet_data():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range="Sheet1!A2:C").execute()
    values = result.get("values", [])
    return values

def sync_sheet_to_db(db: Session):
    data = get_sheet_data()

    # 1. Clear existing data
    db.query(InventoryItem).delete()
    db.commit()

    # 2. Insert fresh data from the sheet
    for row in data:
        try:
            product_name, change_qty, threshold = row
            change_qty = int(change_qty)
            threshold = int(threshold)

            item = InventoryItem(
                product_name=product_name, quantity=change_qty, threshold=threshold
            )
            db.add(item)
        except Exception as e:
            print(f"Error processing row: {row} - {e}")
    db.commit()

