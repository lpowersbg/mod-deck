import telnetlib
import requests

def api_con(host):
    try:
        respwat = requests.get('http://' + host + ':8000/session_status')
        jsonwat = respwat.json()
        status = jsonwat["session_status"]
    except:
        print ("Host " + host + " failed API.")
        status = 0

    return status

def tel_con(host, nogo):
    try:
        tel2 = telnetlib.Telnet(bytes(host, encoding='utf-8'), 5000, 1)
        tel2.write(bytes(nogo, encoding='utf-8'))
        tel2.write(b"exit\n")
    except:
        print ("Host " + host + " failed telnet.")


    