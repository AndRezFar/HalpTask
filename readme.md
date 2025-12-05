# ✅ HelpTask — Gerenciador de Tarefas Inteligente

O **HelpTask** é um sistema web desenvolvido para ajudar usuários a **organizar suas tarefas diárias**, oferecendo uma experiência simples, rápida e eficiente.  
Foi criado como parte de um projeto acadêmico, mas pensado para uso real, com funcionalidades completas de criação, listagem, filtragem e gestão de tarefas.

---

## 🎯 **Objetivo do Projeto**

O intuito do HelpTask é proporcionar uma ferramenta visual e intuitiva que auxilie usuários a:

- Criar tarefas facilmente  
- Acompanhar pendências  
- Organizar rotinas  
- Priorizar atividades  
- Manter histórico de concluídas e excluídas  

Tudo isso com uma interface simples e um back-end robusto, conectado ao banco de dados na nuvem.

---

# 🛠️ **Tecnologias Utilizadas**

### **Front-End**
- HTML5  
- CSS3  
- JavaScript (ES6+)  
- Layout responsivo

### **Back-End**
- Python  
- Flask  
- Gunicorn (produção)

### **Banco de Dados**
- MongoDB Atlas (nuvem)

### **Testes**
- Pytest  
- Mongomock (mock da base de dados)

---

# ⚙️ **Funcionalidades**

### ✔ Criar tarefas  
Inclui título, prioridade, prazo e data de criação automatizada.

### ✔ Listar tarefas  
Apenas tarefas pendentes aparecem na lista principal.

### ✔ Filtrar tarefas  
Por:
- Data de criação  
- Prazo  
- Prioridade  

### ✔ Marcar como concluída  
Move automaticamente para o histórico (status: "concluida").

### ✔ Excluir tarefa  
Move para histórico com status "excluida".

### ✔ Histórico de ações  
Cada tarefa guarda:
- dataCriacao  
- dataConclusao  
- dataExclusao  

### ✔ API REST própria  
Endpoints em Flask.

---

# 🔌 **API — Endpoints**

### ➕ Criar tarefa
