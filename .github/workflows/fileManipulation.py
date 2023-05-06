from googleapiclient.discovery import build
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('.github/workflows/advantechuci-1fdd9c7f63c3.json')
service = build('drive', 'v3', credentials=credentials)
# Find the file by its name or other identifier
response = service.files().list().execute()
files = response.get('files', [])
for file in files:
    print(f"File Name: {file['name']}, File ID: {file['id']}")
"""file_name = 'outputFile1'
response = service.files().list(q=f"name='{file_name}'").execute()
print('response->',response)
file_id = response['files'][0]
print('file_id->',file_id)
content = 'Hello, World!'"""
"""media_body = service.files().get_media(file_id).execute()
print('media_body->',media_body)
media_body += content.encode()
updated_file = service.files().update(
    fileId=file_id,
    media_body=media_body
).execute()"""

