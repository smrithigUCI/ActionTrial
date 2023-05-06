from googleapiclient.discovery import build
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('.github/workflows/advantechuci-1fdd9c7f63c3.json')
service = build('drive', 'v3', credentials=credentials)
# Find the file by its name or other identifier
response = service.files().list().execute()
files = response.get('files', [])
print(files)
for file in files:
    print(f"File Name: {file['name']}, File ID: {file['id']}")
