# 📚 Biblioteca — Documentação do Projeto

## Visão Geral

**Biblioteca** é um sistema de gerenciamento de livros em linha de comando (CLI) desenvolvido em Python. Ele permite cadastrar livros, acompanhar o status de leitura, organizar uma fila de leitura e empilhar os livros já concluídos.

---

## Estrutura do Projeto

```
biblioteca/
│
├── main.py          # Ponto de entrada da aplicação (menu principal)
├── livros.py        # Módulo com as funções de gerenciamento de livros
└── utils.py         # Módulo utilitário (ex: função de título)
```

---

## Módulos

### `main.py`

Arquivo principal da aplicação. Responsável por exibir o menu interativo e acionar as funções de acordo com a escolha do usuário.

**Fluxo de execução:**

1. Limpa o terminal com `os.system("cls")`
2. Exibe o menu principal em loop contínuo (`while True`)
3. Lê a opção digitada pelo usuário
4. Chama a função correspondente
5. Repete até que o usuário escolha **Sair**

**Opções do menu:**

| Opção | Descrição |
|-------|-----------|
| `1`   | Cadastrar um novo livro |
| `2`   | Listar todos os livros cadastrados |
| `3`   | Atualizar o status de um livro (`Lendo` ou `Lido`) |
| `4`   | Mostrar a fila de leitura |
| `5`   | Mostrar a pilha de livros concluídos |
| `6`   | Encerrar o programa |

---

### `livros.py`

Módulo responsável pela lógica de negócio do sistema. Contém as seguintes funções importadas em `main.py`:

#### `cadastrar_livro()`
Solicita os dados de um novo livro ao usuário e o adiciona ao sistema.

#### `listar_livros()`
Exibe todos os livros cadastrados com seus respectivos status de leitura.

#### `atualizar_status(opcao: int)`
Atualiza o status de leitura de um livro.

| Parâmetro | Tipo  | Descrição |
|-----------|-------|-----------|
| `opcao`   | `int` | `1` para *Lendo*, `2` para *Lido* |

#### `mostrar_fila()`
Exibe a **fila de leitura** (estrutura FIFO — First In, First Out), ou seja, os livros na ordem em que foram adicionados para leitura.

#### `mostrar_pilha()`
Exibe a **pilha de livros concluídos** (estrutura LIFO — Last In, First Out), ou seja, o último livro lido aparece primeiro.

---

### `utils.py`

Módulo com funções utilitárias de suporte à interface.

#### `titulo(texto: str)`
Exibe um cabeçalho formatado no terminal com o texto fornecido.

**Exemplo de uso:**
```python
titulo("Biblioteca")
# Saída esperada:
# ================
#    Biblioteca
# ================
```

---

## Estruturas de Dados Utilizadas

| Estrutura | Uso no Projeto |
|-----------|---------------|
| **Fila (Queue / FIFO)** | Organiza os livros aguardando leitura na ordem de cadastro |
| **Pilha (Stack / LIFO)** | Armazena os livros concluídos, exibindo o mais recente primeiro |

---

## Como Executar

### Pré-requisitos

- Python 3.x instalado
- Sistema operacional Windows (o `cls` em `main.py` é específico para Windows; em Linux/macOS, substituir por `clear`)

### Execução

```bash
python main.py
```

---

## Exemplo de Uso

```
================
   Biblioteca
================
1 - Cadastrar livro
2 - Listar livros
3 - Atualizar status do livro
4 - Mostrar fila de leitura
5 - Mostrar pilha de livros concluídos
6 - Sair

Digite a opção desejada: 1
```

---

## Conceitos e Recursos Python Utilizados

### 🔧 Funções
Toda a lógica do sistema é organizada em funções reutilizáveis definidas nos módulos `livros.py` e `utils.py`, como `cadastrar_livro()`, `listar_livros()`, `atualizar_status()`, `mostrar_fila()`, `mostrar_pilha()` e `titulo()`. Isso mantém o código modular e fácil de manter.

### 📋 Listas
Listas Python são utilizadas para armazenar a coleção de livros cadastrados, servindo como base para a fila de leitura e a pilha de livros concluídos. Operações como `.append()`, `.pop()` e iteração são aplicadas sobre essas listas.

### 📦 Dicionários
Cada livro é representado como um dicionário Python, permitindo armazenar múltiplos atributos de forma organizada. Exemplo de estrutura:

```python
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "status": "Lendo"
}
```

### 🔀 Estruturas de Controle
Blocos `if`, `elif` e `else` são usados no menu principal para direcionar o fluxo da aplicação conforme a opção escolhida pelo usuário, e também dentro das funções para validar entradas e tratar casos específicos.

### 🔁 Laços de Repetição
O menu principal roda dentro de um laço `while True`, mantendo o programa em execução contínua até que o usuário escolha a opção **Sair**. Laços `for` são utilizados nas funções de listagem para percorrer os livros cadastrados.

### 🔃 Match-Case (Estrutura de Decisão)
A estrutura `match-case` (disponível a partir do Python 3.10) é empregada como alternativa moderna ao encadeamento de `if/elif`, tornando a leitura do fluxo de decisão mais clara e expressiva em determinadas partes do projeto.

```python
match opcao:
    case "1":
        cadastrar_livro()
    case "2":
        listar_livros()
    ...
```

### ⌨️ Entrada e Saída
- **Entrada:** função `input()` para capturar as escolhas e dados digitados pelo usuário no terminal.
- **Saída:** função `print()` para exibir menus, mensagens, listagens e resultados das operações.

### 🧩 Modulação
O projeto é dividido em módulos com responsabilidades bem definidas, seguindo o princípio da separação de responsabilidades:

| Módulo      | Responsabilidade                              |
|-------------|-----------------------------------------------|
| `main.py`   | Interface com o usuário e fluxo principal     |
| `livros.py` | Lógica de negócio e manipulação de dados      |
| `utils.py`  | Funções auxiliares e utilitários de interface |

### 📥 Importação de Módulos
Módulos próprios e da biblioteca padrão do Python são importados com `import` e `from ... import`:

```python
from livros import cadastrar_livro, listar_livros, atualizar_status, mostrar_fila, mostrar_pilha
from utils import titulo
import os
```

### 🛠️ Manipulação de Listas
As listas são manipuladas diretamente para simular as estruturas de fila e pilha:

| Operação      | Método       | Uso no Projeto                          |
|---------------|--------------|-----------------------------------------|
| Adicionar item | `.append()`  | Cadastrar novo livro na lista           |
| Remover primeiro | `.pop(0)` | Retirar o próximo da fila (FIFO)        |
| Remover último | `.pop()`    | Retirar o topo da pilha (LIFO)          |
| Percorrer      | `for item in lista` | Listar todos os livros         |

---

## Possíveis Melhorias Futuras

- [ ] Persistência de dados com arquivo `.json` ou banco de dados SQLite
- [ ] Compatibilidade com Linux/macOS (substituir `cls` por `clear` automaticamente)
- [ ] Busca de livros por título ou autor
- [ ] Interface gráfica (GUI)  Interface Gráfica do Usuário ou versão web
- [ ] Exportação da lista de livros para `.csv`

---

## Autor

> Documentação gerada para o projeto **Biblioteca** — sistema CLI de gerenciamento de leitura em Python.
