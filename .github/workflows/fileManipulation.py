from googleapiclient.discovery import build
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('.github/workflows/advantechuci-1fdd9c7f63c3.json')
service = build('drive', 'v3', credentials=credentials)
# Find the file by its name or other identifier
file_content = 'Hello, World!'
file_name = 'example.txt'
metadata = {
    'name': file_name,
    'mimeType': 'text/plain'
}

media = service.files().create(
    body=metadata
    #media_body=io.BytesIO(file_content.encode())
).execute()


