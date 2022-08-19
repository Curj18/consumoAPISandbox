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

    try:
        respuesta = requests.get(sandbox+"/api/class/topSystem.json", headers= cabecera, cookies= galleta, verify=False)
        print(respuesta.request.method)
        print(respuesta.request.path_url)
        print(respuesta.request.body)
        print(respuesta.request.headers["Cookie"])
        print(respuesta.headers)
    except Exception as err:
        print("Error al consumir su API por la conex")
        exit(1)

    total_nodos =respuesta.json()["totalCount"]

    for i in range(0, total_nodos):  # o poner 3 en ves d elo ultimo de totalcount
        ip_local = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["address"]
        mac_local = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
        state_local = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["state"]

        print(ip_local + "|" + mac_local + "|" + state_local)

top_system()

