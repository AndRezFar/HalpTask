from models.tarefa import Tarefa
from datetime import datetime
from bson import ObjectId
import database.connection as conn

def criar_tarefa(data):
    tarefa = Tarefa(
        titulo = data["titulo"],
        descricao=data.get("descricao", ""),
        prioridade=data["prioridade"],
        prazo=data.get("prazo")
    )

    doc = {
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "prioridade": tarefa.prioridade,
        "prazo": tarefa.prazo,
        "status": tarefa.status,
        "dataCriacao": datetime.now(),
        "dataConclusao": None,
        "dataExclusao": None
    }

    conn.colecao.insert_one(doc)
    return {"menssagem": "Tarefa criada com sucesso!"}

def listar_tarefas():
    tarefas = list(conn.colecao.find({"status": "pendente"}))

    for t in tarefas:
        t["_id"] = str(t["_id"])
        t["dataCriacao"] = datetime.strftime(t["dataCriacao"], "%d/%m/%Y")
        if t.get("prazo"):
            t["prazo"] = datetime.strftime(t["prazo"], "%d/%m/%Y")

    return tarefas

def concluir_tarefa(id):
    conn.colecao.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "status": "concluida",
            "dataConclusao": datetime.now()
        }}
    )
    return {"menssagem": "Tarefa concluída!"}

def excluir_tarefa(id):

    conn.colecao.update_one(
        {"_id": ObjectId(id)},
        {"$set":{
            "status": "excluida",
            "dataExclusao": datetime.now()
        }}
    )
    return {"menssagem": "Tarefa excluida!"}