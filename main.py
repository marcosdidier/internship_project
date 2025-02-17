from models.usuario import Usuario
from models.tarefa import Tarefa
from utils.exportador import exportar_json

def main():
    while True:
        print("\n📌 MENU DO SISTEMA 📌")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Criar Tarefa")
        print("4 - Listar Tarefas")
        print("5 - Atualizar Status de uma Tarefa")
        print("6 - Exportar Tarefas para JSON")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            Usuario.cadastrar(input("Nome: "), input("Email: "))

        elif opcao == "2":
            for usuario in Usuario.listar():
                print(usuario)

        elif opcao == "3":
            Tarefa.criar(input("Título: "), input("Descrição: "), int(input("ID do Usuário: ")))

        elif opcao == "4":
            for tarefa in Tarefa.listar():
                print(tarefa)

        elif opcao == "5":
            Tarefa.atualizar_status(int(input("ID da Tarefa: ")), input("Novo Status: "))

        elif opcao == "6":
            exportar_json()

        elif opcao == "0":
            break

if __name__ == "__main__":
    main()
