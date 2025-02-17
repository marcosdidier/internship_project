import sqlite3

class Usuario:
    @staticmethod
    def cadastrar(nome, email):
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        try: 
            cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
            print(f"O usuário {nome} foi cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            print("Usuário já cadastrado!")

        conn.close()

    @staticmethod
    def listar():
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        conn.close()
        return usuarios 
    
    @staticmethod
    def buscar_por_id(id_usuario):
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
        usuario = cursor.fetchone()

        if usuario is None:
            print("Usuário não encontrado!")
            return None

        conn.close()
        return usuario