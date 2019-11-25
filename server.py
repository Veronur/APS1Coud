import flask
import sys
import requests

app = flask.Flask(__name__)
ip=sys.argv[1]

@app.route('/Tarefa/', methods=["GET", "POST"])
def Tarefas():
    r=requests.get('http://{}:5000/Tarefa/'.format(ip))
    if flask.request.method == 'POST':
        nome = flask.request.form['data']
        requests.post('http://{}:5000/Tarefa/'.format(ip), data={'data':nome})        
    return {'Nomes': r.text}          
    

@app.route('/Tarefa/<idT>', methods=["DELETE"])
def Delete(idT):
        requests.delete('http://{0}:5000/Tarefa/{1}'.format(ip,idT))
        return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

