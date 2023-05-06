from googleapiclient.discovery import build
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('.github/workflows/advantechuci-1fdd9c7f63c3.json')
service = build('drive', 'v3', credentials=credentials)
# Find the file by its name or other identifier
folder_id = '1oMYGCzitX98Oldeu5MDmhBerTko2WcKe'
response = service.files().list(q=f"name='{file_name}' and '{folder_id}' in parents").execute()
print(response)

