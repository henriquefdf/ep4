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
│   └── test_main.py      # Testes unitários
└── .github/
    └── workflows/
        └── ci.yml       # Configuração de CI/CD para GitHub Actions
```

## Requisitos

- Python 3.8 ou superior

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

Execute os testes unitários para verificar se o programa está funcionando corretamente:

```bash
python -m unittest discover tests
```

## CI/CD com GitHub Actions

Este projeto utiliza GitHub Actions para:

- Testar automaticamente o código em **Ubuntu**, **MacOS** e **Windows**.
- Garantir que todos os commits sejam testados.

### Configuração do workflow

Veja o arquivo de workflow em `.github/workflows/ci.yml`.


## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
