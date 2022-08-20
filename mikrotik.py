import requests
import urllib3
import json

urllib3.disable_warnings()

url= "https://192.168.0.23"
user = "admin"

clave = "admin"

r = requests.get(url+"/rest/ip/address/*3", auth= (user,clave), verify = False)


#print(json.dumps(r.json(), indent =2))

r2 = requests.get(url + "/rest/interface/ether1", auth= (user,clave), verify = False)

print(r2.json()["mac-address"])