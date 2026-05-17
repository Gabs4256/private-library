from livros import cadastrar_livro, listar_livros, atualizar_status
from utils import titulo
import os
os.system("cls")

while True:
    titulo("Biblioteca")

    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Atualizar status do livro")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        print("\n1 - Atualizar para 'Lendo'")
        print("2 - Atualizar para 'Lido'")
        status_opcao = input("Escolha uma opção: ")
        
        if status_opcao in ["1", "2"]:
            atualizar_status(int(status_opcao))
        else:
            print("Opção inválida, tente novamente.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")