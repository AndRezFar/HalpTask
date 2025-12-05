from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://HelpTask:qoqca8-fumcum-sEqpuj@helptask.azbxbso.mongodb.net/")
    db = client["HelpTask"]
    return db

db = get_db()
colecao = db["tarefas"]