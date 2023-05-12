from azure.storage.blob import BlobServiceClient , generate_blob_sas,BlobSasPermissions
import pandas as pd
from datetime import datetime,timedelta,date
def pushBullet(title, body):
    TOKEN = 'o.WDQEkWs8Rs5S6WEJq1MhXU69k4rZMuEr'
    # Making a dictionary for type, title and body parameters
    msg = {"type": "note", "title": title, "body": body}
        # Sent a posts request
    response1 = requests.post('https://api.pushbullet.com/v2/pushes',data=json.dumps(msg),headers={'Authorization': 'Bearer ' + TOKEN,'Content-Type': 'application/json'})
    if response1.status_code != 200: # Response code 200 signifies perfect access to app 
        raise Exception('Error', resp.status_code)
def startPump():
    payload = { "Ch": 0,"Md": 0,"Val": 1,"Stat": 1,"PsCtn": 1,"PsStop": 0,"PsIV": 0}
    headers = {"Content-Type": "application/json","Authorization": "Basic cm9vdDowMDAwMDAwMA==","Cookie": "Cookie=adamsessionid=12965427BA2"}
    Flag = True;
    while(Flag):
        response = requests.request("POST", self.url, json=payload, headers=headers)
        time.sleep(58)
        print(response)
        Flag = False;
                
            #switching the relay 0 OFF
    payload1 = {"Ch": 0,"Md": 0,"Val": 1,"Stat":0 ,"PsCtn": 1,"PsStop": 0,"PsIV": 0}
    response = requests.request("POST", "https://169.234.25.18/do_value/slot_0/ch_0", json=payload1, headers=headers)
            
    if response1.status_code == 200:
        msg = "The first preventive herbicide spray is done kindly place the robot on the field to monitor the further emergence of weed"
        pushbullet_notification("First preventive herbicide spray done",msg)
    else:
        msg = f"The preventive spray is predicted for {contents}"
        pushbullet_notification("Today is not the predicted date for the preventive herbicide spray",msg)

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
df=pd.read_csv("https://sunflowerweedimage.blob.core.windows.net/sunfloweweedimagecontainer/myDate2.txt?sp=r&st=2023-05-12T00:59:32Z&se=2023-06-25T08:59:32Z&spr=https&sv=2022-11-02&sr=b&sig=hqMIVFoprRLYKlG95tZw0VbHI37pZN%2BG67m%2B4FWHTrA%3D")
print(df.columns)
for i in df.columns:
    print(i)
    print('date->',date.today())
    if i=='2023-05-11':
        print('starting pump')
        startPump();
