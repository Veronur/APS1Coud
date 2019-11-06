import requests
dictToSend = input("nome da nova tarefa\n")

res = requests.post('http://127.0.0.1:5000/Tarefa/', data={'data':dictToSend})
