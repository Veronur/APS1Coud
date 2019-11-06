import requests
idT= input("id da tarefa\n")
nome= input("novo nome da tarefa\n")

res = requests.put('http://127.0.0.1:5000/Tarefa/{}'.format(idT), data={'data':nome})