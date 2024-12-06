# To-Do List Manager

Um programa simples de lista de tarefas escrito em Python. Este programa permite gerenciar tarefas com funcionalidades como adicionar, listar, remover e marcar tarefas como concluídas.

## Funcionalidades

- **Adicionar tarefa**: Adicione uma tarefa com título e descrição.
- **Remover tarefa**: Remova uma tarefa pelo título.
- **Listar tarefas**: Exiba todas as tarefas pendentes ou concluídas.
- **Marcar tarefa como concluída**: Atualize o status de uma tarefa.

## Estrutura do Projeto

```
.
├── todo_list/
│   ├── __init__.py
│   └── main.py          # Código principal do programa
├── tests/
│   ├── __init__.py
│   └── test_main.py      # Testes usando pytest
└── .github/
    └── workflows/
        └── ci.yml       # Configuração de CI/CD para GitHub Actions
```

## Requisitos

- Python 3.8 ou superior
- `pytest` para rodar os testes

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Adicionar tarefa
```python
from todo_list.main import ToDoList

todo = ToDoList()
todo.add_task("Comprar leite", "Ir ao supermercado comprar leite")
todo.add_task("Estudar Python", "Revisar listas e dicionários")
```

### Listar tarefas
```python
for task in todo.list_tasks():
    print(task)
```

### Marcar uma tarefa como concluída
```python
todo.mark_task_completed("Comprar leite")
```

### Remover tarefa
```python
todo.remove_task("Estudar Python")
```

## Testes

Os testes são escritos usando o `pytest`. Para executá-los:

1. Certifique-se de que o `pytest` está instalado:
   ```bash
   pip install pytest
   ```

2. Rode os testes:
   ```bash
   pytest
   ```

Se todos os testes passarem, você verá uma saída semelhante a:
```
============================= test session starts ==============================
collected 5 items

tests/test_main.py .....                                               [100%]

============================== 5 passed in 0.02s ==============================
```

## CI/CD com GitHub Actions

Este projeto usa GitHub Actions para garantir integração contínua. O workflow está configurado para:

- Executar os testes automaticamente em **Ubuntu**, **MacOS** e **Windows** a cada `push` ou `pull request` para o branch `main`.

### Configuração do workflow

Veja o arquivo de workflow em `.github/workflows/ci.yml`.
