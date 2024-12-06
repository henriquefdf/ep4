import pytest
from todo_list.main import ToDoList, Task


@pytest.fixture
def todo_list():
    return ToDoList()


def test_add_task(todo_list):
    task = todo_list.add_task("Test Task", "Test Description")
    assert len(todo_list.tasks) == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"


def test_remove_task(todo_list):
    todo_list.add_task("Task 1")
    removed_task = todo_list.remove_task("Task 1")
    assert removed_task.title == "Task 1"
    assert len(todo_list.tasks) == 0


def test_remove_nonexistent_task(todo_list):
    with pytest.raises(ValueError, match="Task not found"):
        todo_list.remove_task("Nonexistent Task")


def test_mark_task_completed(todo_list):
    todo_list.add_task("Task 1")
    task = todo_list.mark_task_completed("Task 1")
    assert task.completed is True


def test_list_tasks(todo_list):
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    tasks = todo_list.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


# Novos testes

def test_mark_nonexistent_task_completed(todo_list):
    with pytest.raises(ValueError, match="Task not found"):
        todo_list.mark_task_completed("Nonexistent Task")


def test_add_duplicate_tasks(todo_list):
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 1")  # Permitir tarefas com títulos iguais
    assert len(todo_list.tasks) == 2
    assert todo_list.tasks[0].title == "Task 1"
    assert todo_list.tasks[1].title == "Task 1"


def test_list_empty_todo_list(todo_list):
    tasks = todo_list.list_tasks()
    assert len(tasks) == 0


def test_remove_task_with_special_characters(todo_list):
    todo_list.add_task("Task@123", "Special characters in title")
    removed_task = todo_list.remove_task("Task@123")
    assert removed_task.title == "Task@123"
    assert len(todo_list.tasks) == 0


def test_task_str_representation(todo_list):
    task = todo_list.add_task("Task 1", "Task description")
    assert str(task) == "Task 1 - ✘ - Task description"
    task.mark_completed()
    assert str(task) == "Task 1 - ✔ - Task description"
