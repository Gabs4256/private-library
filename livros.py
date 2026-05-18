from dados import livros, fila_leitura, pilha_concluidos, status

## Função para cadastrar um novo livro
def cadastrar_livro():
    nome_livro = input("Digite o nome do livro: ")
    autor_livro = input("Digite o nome do autor: ")
    quantidade_paginas = int(input("Digite a quantidade de páginas: "))

    livro = {
        "id": len(livros) + 1,
        "nome": nome_livro,
        "autor": autor_livro,
        "paginas": quantidade_paginas,
        "status": status[0]
    }

    livros.append(livro)
    fila_leitura.append(livro)
    print("Livro cadastrado, boa leitura :D!")

## Função para listar os livros cadastrados
def listar_livros():
    for livro in livros:
        print(f"""
              ID: {livro['id']}
              nome: {livro['nome']}
              autor: {livro['autor']}
              paginas: {livro['paginas']}
              status: {livro['status']}""")

## Função para atualizar o status do livro
def atualizar_status(opcao): 
    id_livro = int(input("Digite o ID do livro que deseja atualizar o status: "))
    encontrado = False
    
    for livro in livros:
        if livro["id"] == id_livro:
            encontrado = True
            match opcao:
                case 1:
                    livro["status"] = status[1]  # "Lendo"
                    if livro in fila_leitura:
                        fila_leitura.remove(livro)
                    print(f"Status do livro '{livro['nome']}' atualizado para 'Lendo'!")
                case 2:
                    livro["status"] = status[2]  # "Lido"
                    if livro not in pilha_concluidos:
                        pilha_concluidos.append(livro)
                    print(f"Status do livro '{livro['nome']}' atualizado para 'Lido'!")
            break
    
    if not encontrado:
        print("Livro não encontrado, tente novamente.")

## Mostrar fila de leitura
def mostrar_fila():
    print("\n=== FILA DE LEITURA ===")

    if len(fila_leitura) == 0:
        print("Nenhum livro na fila.")
    else:
        for livro in fila_leitura:
            print(f"{livro['nome']} - {livro['status']}")

## Mostrar pilha de livros concluídos
def mostrar_pilha():
    print("\n=== PILHA DE LIVROS CONCLUÍDOS ===")

    if len(pilha_concluidos) == 0:
        print("Nenhum livro concluído.")
    else:
        for livro in reversed(pilha_concluidos):
            print(f"{livro['nome']} - {livro['status']}")