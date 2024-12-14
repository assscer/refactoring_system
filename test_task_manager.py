import unittest
from task_manager import Task, Project, User, TaskManager
from datetime import datetime


class TestTaskManager(unittest.TestCase):
    def test_task_creation(self):
        manager = TaskManager()
        user = User(1, "test_user")
        project = Project(1, "test_project")
        task = manager.create_task("Test Task", "Description", user, project, datetime(2024, 12, 20))

        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "New")
        self.assertEqual(len(manager.tasks), 1)

if __name__ == '__main__':
    unittest.main()
