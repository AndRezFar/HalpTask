nova_tarefa = {
        "titulo": "Teste 1",
        "prioridade": "Alta",
        "prazo": "2025-12-25"
    }

def test_criar_tarefa(client):
    resposta = client.post("/tarefas", json = nova_tarefa)
    dados = resposta.get_json()

    assert "menssagem" in dados
    assert dados["menssagem"] in ["Tarefa criada com sucesso!"]

def test_listar_tarefas(client):

    client.post("/tarefas", json = nova_tarefa)

    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
    dados = resposta.get_json()

    assert isinstance(dados, list)
    assert len(dados) == 1
    
    assert dados[0]["titulo"] == "Teste 1"
    assert dados[0]["prioridade"] == "Alta"

def test_concluir_tarefas(client):
    client.post("/tarefas", json = nova_tarefa)
    
    lista = client.get("/tarefas").get_json()
    tarefa_id = lista[0]["_id"]
 
    resposta_put = client.put(f"/tarefas/{tarefa_id}")
    msg = resposta_put.get_json()

    assert resposta_put.status_code == 200
    assert msg["menssagem"] == "Tarefa concluída!"

    lista_atualizada = client.get("/tarefas").get_json()
  
    assert all(t["_id"] != tarefa_id for t in lista_atualizada)


def test_excluir_tarefa(client):
    client.post("/tarefas", json = nova_tarefa)
    
    lista = client.get("/tarefas").get_json()
    tarefa_id = lista[0]["_id"]
 
    resposta_delete = client.delete(f"/tarefas/{tarefa_id}")
    msg = resposta_delete.get_json()

    assert resposta_delete.status_code == 200
    assert msg["menssagem"] == "Tarefa excluida!"

    lista_atualizada = client.get("/tarefas").get_json()
  
    assert all(t["_id"] != tarefa_id for t in lista_atualizada)
