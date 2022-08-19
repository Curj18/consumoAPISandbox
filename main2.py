import json

import requests

import conf



sandbox = "https://10.10.20.14"

def obtener_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"
    body = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
            }
        }
    }
    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return token

#http://apic-ip-address/api/class/topSystem.json
def top_system():
    cabecera = {
        "Content-Type" : "application/json"
    }
    galleta = {
        "APIC-Cookie":  obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta= requests.get(sandbox+"/api/class/topSystem.json", headers= cabecera, cookies= galleta, verify=False)

    total_nodos =respuesta.json()["totalCount"]

    for i in range(0, int(respuesta.json()["totalCount"])):  # o poner 3 en ves d elo ultimo de totalcount
        ip_local = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["address"]
        print(ip_local)

top_system()

