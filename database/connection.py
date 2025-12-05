import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_db():
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise Exception("ERRO: Variável MONGO_URI não encontrada no ambiente!")

    client = MongoClient(mongo_uri, server_api=ServerApi('1'))

    return client["HelpTask"]

db = get_db()
colecao = db["tarefas"]