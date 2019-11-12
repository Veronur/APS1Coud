import flask
from Tarefas import Tarefas
import json


app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/Tarefa/', methods=["GET", "POST"])
def listaTarefas():
    #Checa se houve um POST e se sim o trata
    if flask.request.method == 'POST':
        with open('tarefas.json', 'r') as fr:
            fr = json.load(fr)
            
        nome = flask.request.form['data']
        
        tarefa= Tarefas(nome)
        dicti={
            "id" : tarefa.idTarefa,
            "nome": tarefa.nome
        }
        fr['tarefas'].append(dicti)
        
        with open('tarefas.json', 'w') as fw:
            json.dump(fr, fw)
    #Executa o Get
    with open("tarefas.json", 'r') as f:
        t = json.load(f)
    return t            
    

@app.route('/Tarefa/<idT>', methods=["GET", "DELETE", "PUT"])
def tarefaId(idT):
    if flask.request.method == 'GET':
        with open("tarefas.json", 'r') as f:
            t = json.load(f)
        for i in t['tarefas']:
            if i["id"]==int(idT):
                return i
        return "Not found..."

    elif flask.request.method == 'PUT':
        with open("tarefas.json", 'r') as f:
            t = json.load(f)
        k=0
        for i in t['tarefas']:
            if i["id"]==int(idT):
                t['tarefas'][k]['nome']=flask.request.form['data']
                with open('tarefas.json', 'w') as fw:
                    
                    json.dump(t, fw)
                return "Editado com sucesso"
            k+=1
        return "Falha na edicao"



    elif flask.request.method == 'DELETE':
        with open("tarefas.json", 'r') as f:
            t = json.load(f)
        
        for i in t['tarefas']:
            if i["id"]==int(idT):
                t['tarefas'].remove(i)
                with open('tarefas.json', 'w') as fw:
                    
                    json.dump(t, fw)                    
                    return "Deletado"
        return "Falha na Delecao"

@app.route('/healthcheck/')
def healthcheck():
    return 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

