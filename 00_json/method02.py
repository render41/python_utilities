import requests
import json
# Requisição do tipo GET da API.
r = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

print(r)
