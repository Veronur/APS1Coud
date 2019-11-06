import requests
idT= input("id da tarefa\n")

res = requests.delete('http://127.0.0.1:5000/Tarefa/{}'.format(idT))