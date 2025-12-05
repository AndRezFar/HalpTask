import pytest
import mongomock
import database.connection as conn
from app import app


@pytest.fixture
def client():
    mongo_mock = mongomock.MongoClient()
    db_mock = mongo_mock["helpTask_test"]
    colecao_mock = db_mock["tarefas"]
    
    conn.colecao = colecao_mock
    
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

    colecao_mock.delete_many({})