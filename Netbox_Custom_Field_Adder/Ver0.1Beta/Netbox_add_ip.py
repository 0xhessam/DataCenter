import json
import requests
import csv
url = "https://iaasnetbox.arvan.me/api/dcim/devices/?limit=1000"
res = requests.get(url,headers={'Content-Type': 'application/json',
'Authorization': 'Token tokentextshouldbehere'})
json_data = json.loads(res.content)
res = json_data['results']
file_name = "importvalues.csv"
reader = csv.DictReader(open(file_name))

for csv_f in reader:
 for device in res:
   

  if csv_f['name'] == device['name']:
   url = "https://iaasnetbox.arvan.me/api/dcim/devices/"+str(device['id'])+"/"
  })
   data ={}
   data['custom_fields'] = {}
   data['custom_fields']['ILO IP'] = csv_f['ilo_ip']
   data['custom_fields']['Supplier'] = "15"
   res2 = requests.request("patch",url,headers={'Content-Type': 'application/json',
   'Authorization': 'Token tokentextshouldbehere'},json=data)
   print("iLo IP Successfuly Added !" + str(csv_f['name']+ "----------" + str(res2.status_code) +"--------"))
 








