import sqlite3
import json

def exportar_json(arquivo = "data/tasks.json"):
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT tarefas.id, tarefas.titulo, tarefas.descricao, tarefas.status, usuarios.nome, usuarios,email
    FROM tarefas
    JOIN usuarios ON tarefas.usuario_id = usuarios_id
    """)

    tarefas = [
        {"id":t[0], "titulo":t[1], "descricao":t[2], "status":t[3], "usuario":{"nome":t[4],
        "email":t[5]}}
        for t in cursor.fetchall()
    ]

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

    conn.close()
    print(f"Arquivo {arquivo} salvo com êxito!")
