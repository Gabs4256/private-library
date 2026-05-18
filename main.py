from livros import (
    cadastrar_livro,
    listar_livros,
    atualizar_status,
    mostrar_fila,
    mostrar_pilha
)
from utils import titulo

import os
os.system("cls")

while True:
    titulo("Biblioteca")

    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Atualizar status do livro")
    print("4 - Mostrar fila de leitura ")
    print("5 - Mostrar pilha de livros concluídos")
    print("6 - Sair")

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
         mostrar_fila()

    elif opcao == "5":
        mostrar_pilha()
        
    elif opcao == "6":
        print("Saindo...")
        break
        

    else:
        print("Opção inválida, tente novamente.")