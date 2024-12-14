from datetime import datetime
from typing import List

class Task:
    def __init__(self, id: int, title: str, description: str, user: 'User', project: 'Project', due_date: datetime):
        """инициализация задачи"""
        self.id = id
        self.title = title
        self.description = description
        self.user = user
        self.project = project
        self.due_date = due_date
        self.status = "New"  

    def is_overdue(self) -> bool:
        """проверка, просрочена ли задача"""
        return self.due_date < datetime.now()

class Project:
    def __init__(self, id: int, name: str):
        """инициализация проекта"""
        self.id = id
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """добавление задачи в проект"""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """удаление задачи из проекта"""
        task.status = "Deleted"
        self.tasks.remove(task)

    def get_overdue_tasks(self) -> List[Task]:
        """получение просроченных задач"""
        return [task for task in self.tasks if task.is_overdue()]

class User:
    def __init__(self, id: int, username: str):
        """инициализация пользователя"""
        self.id = id
        self.username = username
        self.tasks: List[Task] = []

    def assign_task(self, task: Task):
        """назначение задачи пользователю"""
        self.tasks.append(task)
        task.user = self

    def remove_task(self, task: Task):
        """удаление задачи у пользователя"""
        self.tasks.remove(task)
        task.user = None

class TaskManager:
    def __init__(self):
        """инициализация менеджера задач"""
        self.tasks: List[Task] = []
        self.projects: List[Project] = []
        self.users: List[User] = []

    def create_task(self, title: str, description: str, user: User, project: Project, due_date: datetime) -> Task:
        """создание задачи"""
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description, user, project, due_date)
        self.tasks.append(task)
        project.add_task(task)
        user.assign_task(task)
        return task

    def remove_task(self, task: Task):
        """удаление задачи"""
        self.tasks.remove(task)
        task.status = "Deleted"
        task.project.remove_task(task)
        task.user.remove_task(task)

    def get_overdue_tasks(self) -> List[Task]:
        """получение всех просроченных задач"""
        return [task for task in self.tasks if task.is_overdue()]
