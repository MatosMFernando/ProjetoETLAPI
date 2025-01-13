import requests

url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

resposta = requests.get(url)
data = resposta.json()

print(data)