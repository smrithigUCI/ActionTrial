payload = { "Ch": 0,"Md": 0,"Val": 1,"Stat": 1,"PsCtn": 1,"PsStop": 0,"PsIV": 0}
headers = {"Content-Type": "application/json","Authorization": "Basic cm9vdDowMDAwMDAwMA==","Cookie": "Cookie=adamsessionid=12965427BA2"}
Flag = True;
while(Flag):
  response = requests.request("POST", "http://169.234.25.18/do_value/slot_0/ch_0", json=payload, headers=headers)
  time.sleep(58)
  print(response)
  Flag = False;
                
            #switching the relay 0 OFF
payload1 = {"Ch": 0,"Md": 0,"Val": 0,"Stat":0 ,"PsCtn": 1,"PsStop": 0,"PsIV": 0}
response1 = requests.request("POST", "http://169.234.25.18/do_value/slot_0/ch_0", json=payload1, headers=headers)
if response1.status_code == 200:
  print('success')
