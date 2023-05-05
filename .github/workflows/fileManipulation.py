import json
import requests
def UploadToDrive(filepath,filename):

    headers = {"Authorization":"Bearer ya29.a0Ael9sCO2lIUKj9IjCAF9pn1Jh4ibbE9raibgODyeQ6qdMIpc_TCm5tzR2a8g5mg_qqf3y_EcKJMBI2RLGaXAiFGp8gWHYVDsiYY--kPtAuZzc0EwYpoRwGrWxXs33lGUZySYXQnkepoK2OSynPRwVN3GP3AqaCgYKAcESARMSFQF4udJhyn8VBTqoAMQRkXCI9HzufQ0163"}

    para = {
        "name":filename,
        "parents":["1DBr5USVxg6LJw_HDiBK743vjIFo4gIRK"]
    }
    files = {
        'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'),
        'file':open(filepath,'rb')
    }

    r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",headers=headers,files=files)
    print(f"Uploaded {filename} to Drive")
UploadToDrive(".github/workflows/outputFile1.txt","outputFile1.txt")
