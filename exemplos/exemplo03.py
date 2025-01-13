import requests

url = "https://jsonplaceholder.typicode.com/comments"
parametros = {"postId": 1}
resposta = requests.get(url, params=parametros)

comentarios = resposta.json()
print(f"Foram encontrados {len(comentarios)} comentários.")
print(f"Erro: {resposta.status_code} - {resposta.text}")

