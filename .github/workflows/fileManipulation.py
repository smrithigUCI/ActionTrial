from google.oauth2 import service_account
from googleapiclient.discovery import build
import io

credentials = service_account.Credentials.from_service_account_file('.github/workflows/advantechuci-1fdd9c7f63c3.json')
drive_service = build('drive', 'v3', credentials=credentials)

# Find the file by its name or other identifier
file_content = 'Hello, World!'
file_name = 'example.txt'
metadata = {
    'name': file_name,
    'mimeType': 'text/plain'
}

file_metadata = {
    'name': 'example.txt',  # Name of the file
    'mimeType': 'text/plain'  # MIME type of the file
}

file_content = 'This is the content of the text file.'

file = drive_service.files().create(
    body=file_metadata,
    media_body=io.BytesIO(file_content.encode('utf-8'))
).execute()

print('File created:', file.get('id'))


