from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# Define SCOPES
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/spreadsheets'
]

SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', 'service_account.json')

# Authenticate once and share the clients
def get_google_clients():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    drive_service = build('drive', 'v3', credentials=credentials)
    docs_service = build('docs', 'v1', credentials=credentials)
    sheets_service = build('sheets', 'v4', credentials=credentials)

    return drive_service, docs_service, sheets_service
