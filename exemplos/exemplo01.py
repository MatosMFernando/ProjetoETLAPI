import requests

url = "https://api.coinbase.com/v2/prices/spot"
headers = {
    "Accept": "application.json",
    
}

resposta = requests.get(url)

print(resposta)

