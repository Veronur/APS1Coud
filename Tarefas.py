import json



class Tarefas:
    def __init__(self,nome):
        with open("tarefas.json", 'r') as f:
            dictTarefas = json.load(f)
        self.idTarefa=len(dictTarefas['tarefas'])
        self.nome=nome

    