from azure.storage.blob import BlobServiceClient , generate_blob_sas,BlobSasPermissions
import pandas as pd
from datetime import datetime,timedelta
print('Hi')
account_name='sunflowerweedimage'
account_key='+55v1G3ZgPTBu2p9iu6YXfi3SrS+jXkPX9eR4pydpO6q5OCKyScdpLMzMLe9YiGwHbXa1viUUBflu+ASt+RoWKg=='
container_name='sunfloweweedimagecontainer'

connection_string='DefaultEndpointsProtocol=https;AccountName='+account_name+';AccountKey='+account_key+';EndpointSuffix=core.windows.net';
blob_service_client =BlobServiceClient.from_connection_string(connection_string)
print('Hi')
container_client = blob_service_client.get_container_client(container_name)
blob_list =[]
print('Hi')
sas_i=generate_blob_sas(account_name=account_name,container_name=container_name,blob_name='myDate2.txt',account_key=account_key,permissions=BlobSasPermissions(read=True),expiry=datetime.utcnow()+timedelta(hours=1))
print(sas_i)
df=pd.read_csv("https://sunflowerweedimage.blob.core.windows.net/sunfloweweedimagecontainer/myDate2.txt?sp=racw&st=2023-05-10T09:46:35Z&se=2023-05-23T17:46:35Z&spr=https&sv=2022-11-02&sr=b&sig=YQ4cTyFbPZKjQDdEIuHl2EzY6W0C3iWfXXmpA%2FzBH%2Bc%3D")
try:
    df[date.today()];
    print('all good')
except:
    print('not the date')
