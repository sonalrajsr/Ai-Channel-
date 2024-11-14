import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

def load_csv_data(file):
    return pd.read_csv(file)

def fetch_google_sheet_data(sheet_id, range_name):
    credentials = service_account.Credentials.from_service_account_file(
        'credentials/google_sheets_credentials.json',
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get('values', [])
    return pd.DataFrame(values[1:], columns=values[0])
