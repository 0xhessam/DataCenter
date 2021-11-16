import json
import requests
import csv
url = "https://iaasnetbox.arvan.me/api/dcim/devices/?limit=1000"
res = requests.get(url,headers={'Content-Type': 'application/json',
'Authorization': 'Token --------------------------'})
#print(res.content)
json_data = json.loads(res.content)
#print(json_data)
res = json_data['results']
#print(str(res)+"++++++++")
file_name = "importvalues.csv"
reader = csv.DictReader(open(file_name))

for csv_f in reader:
 for device in res:
   
  #print(csv_f['name'])
 # print(device['name'])
  if csv_f['name'] == device['name']:
   url = "https://iaasnetbox.arvan.me/api/dcim/devices/"+str(device['id'])+"/"
   #print(url)
   #payload=json.dumps({"comments{"serial":csv_f['ilo_ip']}":csv_f['ilo_ip']})
   data ={}
   data['custom_fields'] = {}
   data['custom_fields']['ILO IP'] = csv_f['ilo_ip']
   data['custom_fields']['Supplier'] = "15"
   #print(data)
   res2 = requests.request("patch",url,headers={'Content-Type': 'application/json',
   'Authorization': 'Token 6932fc319f8711e4c55135c28894e22db84c28df'},json=data)
   print("iLo IP Successfuly Added !" + str(csv_f['name']+ "----------" + str(res2.status_code) +"--------"))
   #print(res.json())
 # else:
  # print("iLo IP Failed to Add !" + str(csv_f['name']))







   #       "custom_fields": { "ILO IP": "192.168.2.2}
