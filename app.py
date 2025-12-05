from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers.tarefaController import (criar_tarefa, listar_tarefas, concluir_tarefa, excluir_tarefa)

app = Flask(__name__)
CORS(app)

@app.route("/tarefas", methods=["POST"])
def criar():
    data = request.json
    return jsonify(criar_tarefa(data))

@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(listar_tarefas())

@app.route("/tarefas/<id>", methods=["PUT"])
def concluir(id):
    return jsonify(concluir_tarefa(id))

@app.route("/tarefas/<id>", methods=["DELETE"])
def excluir(id):
    return jsonify(excluir_tarefa(id))

if __name__ == "__main__":
    app.run(debug=True)