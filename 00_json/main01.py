import requests
import json

requestsGET = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

requestsPOST = requests.post(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

try:
    requestsJSON = requestsGET.json()
    print('Price the Dollar to Real is: R$' + requestsJSON['USDBRL']['bid'])
except:
    print("No Capture Request.")
finally:
    print("End Try/Except.")
