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
