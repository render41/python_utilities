import requests
import json

filelink = open('test.json')

datarequest = json.load(filelink)

requestsGET = requests.get(datarequest['link'])

requestsPOST = requests.post(datarequest['link'])

try:
    requestsJSON = requestsGET.json()
    print('Price the Dollar to Real is: R$' + requestsJSON['USDBRL']['bid'])
except:
    print("No Capture Request.")
finally:
    print("End Try/Except.")

filelink.close()
