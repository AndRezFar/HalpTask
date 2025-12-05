from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, prazo):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        if isinstance(prazo, str):
            try:
                self.prazo = datetime.strptime(prazo, "%Y-%m-%d")
            except:
                self.prazo = None
        else:
            self.prazo = prazo
        self.status = "pendente"