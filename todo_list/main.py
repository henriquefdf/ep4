class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{self.title} - {status} - {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return task
        raise ValueError("Task not found")

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return task
        raise ValueError("Task not found")

