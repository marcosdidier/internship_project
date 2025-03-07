import sqlite3
from models.usuario import Usuario

class Tarefa:
    OPCOES_STATUS = ["Pendente", "Em andamento", "Concluída"]

    @staticmethod
    def criar(titulo, descricao, usuario_id):
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        usuario = Usuario.buscar_por_id(usuario_id)

        if not usuario:
            print("Usuário não encontrado!")
            return
        
        cursor.execute("INSERT INTO tarefas (titulo, descricao, usuario_id) VALUES (?, ?, ?)", (titulo, descricao, usuario_id))
        conn.commit()
        conn.close()
        print("Tarefa cadastrada com sucesso!")

    @staticmethod
    def listar():
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT tarefas.id, tarefas.titulo, tarefas.status, usuarios.nome
        FROM tarefas
        JOIN usuarios ON tarefas.usuario_id = usuarios.id
        """)

        tarefas = cursor.fetchall()
        conn.close()
        return tarefas
    
    @staticmethod
    def atualizar_status(id_tarefa, novo_status):
        if novo_status not in Tarefa.OPCOES_STATUS:
            print("Status inválido!")
            return
        
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM tarefas WHERE id = ?", (id_tarefa,))
        if not cursor.fetchone():
            print("Tarefa não encontrada!")
            return
        

        cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?", (novo_status, id_tarefa))
        conn.commit()
        conn.close()
        print(f"Status da tarefa {id_tarefa} atualizado para {novo_status}")
