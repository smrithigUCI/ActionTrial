from googleapiclient.discovery import build
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('.github/workflows/client_secret_217221968848-frebl3d7fmf13o36hq5fjv0ar5c88091.apps.googleusercontent.com.json')
service = build('drive', 'v3', credentials=credentials)
# Find the file by its name or other identifier
file_name = 'outputFile1.docx'
response = service.files().list(q=f"name='{file_name}'").execute()
print('response->',response)
file_id = response['files'][0]['id']
print('file_id->',file_id)
content = 'Hello, World!'
media_body = service.files().get_media(fileId=file_id).execute()
print('media_body->',media_body)
media_body += content.encode()
updated_file = service.files().update(
    fileId=file_id,
    media_body=media_body
).execute()

