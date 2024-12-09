from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import Project, Task


class Command(BaseCommand):
    """
    Uses Factories to setup objects in the database so the platform
    can work correctly.

    This will be used to reset staging or future sandbox environments
    """

    def handle(self, **options):
        self.main()

    def main(self):
        self.setup_users()
        self.setup_projects()
        self.setup_tasks()

    def setup_users(self):
        self.admin, created = User.objects.get_or_create(
            username='admin',
            defaults = {
                # password: admin
                "password":'pbkdf2_sha256$870000$6myKOIw46oZOiabclMTZGk$LlvbNe7YuK8bBFNKdVlJrq6OKXUflHY12y0whcnnATI=',
                "is_superuser":True,
                "is_staff":True
            }
        )
        self.user, created = User.objects.get_or_create(
            username='user',
            defaults = {
                # password: qwerty
                "password":'pbkdf2_sha256$870000$5w8U7Va8hW9RdLGIOuBgjj$padDfTRMTHa18MjTJKCdk545K1d9UV1PRi/Jqo8BXJk=',
                "is_superuser":False,
                "is_staff":False
            }
        )
        self.user_2, created = User.objects.get_or_create(
            username='second',
            defaults = {
                # password: 123456
                "password":'pbkdf2_sha256$870000$zVA4SC46PSfMUHPRzq0CXz$98jxCl8U4ilqeXiijJMzTppK0zcJ6W2SN58Qm4CwexU=',
                "is_superuser":False,
                "is_staff":False
            }
        )

    def setup_projects(self):
        self.project_1, created = Project.objects.get_or_create(
            name='Project 1',
            defaults = {
                "description":'Test Project',
                "created_by":self.user
            }
        )
        self.project_2, created = Project.objects.get_or_create(
            name='Project 2',
            defaults = {
                "description":'Test Project',
                "created_by":self.user
            }
        )
        self.project_3, created = Project.objects.get_or_create(
            name='Project 3',
            defaults = {
                "description":'Test Project',
                "created_by":self.user_2
            }
        )

    def setup_tasks(self):
        TASK_DATA = [
            {
              "reported_by": self.user,
              "assigned_to": self.user_2,
              "project": self.project_1,
              "name": "Initial Project Setup",
              "description": "Set up initial project infrastructure and baseline configurations",
              "due_date": "2024-03-15 13:00:00+00:00"
            },
            {
              "reported_by": self.user_2,
              "assigned_to": self.user,
              "project": self.project_2,
              "name": "Requirements Gathering",
              "description": "Collect and document comprehensive project requirements",
              "due_date": "2024-03-20 13:00:00+00:00"
            },
            {
              "reported_by": self.user,
              "assigned_to": self.user,
              "project": self.project_3,
              "name": "Internal Review Process",
              "description": "Develop internal review and approval workflow",
              "due_date": "2024-03-25 13:00:00+00:00"
            },
            {
              "reported_by": self.user_2,
              "assigned_to": self.user_2,
              "project": self.project_1,
              "name": "System Architecture Design",
              "description": "Create detailed system architecture blueprint",
              "due_date": "2024-04-01 13:00:00+00:00"
            },
            {
              "reported_by": self.user,
              "assigned_to": self.user_2,
              "project": self.project_2,
              "name": "API Development",
              "description": "Develop core API endpoints for project integration",
              "due_date": "2024-04-10 13:00:00+00:00"
            },
            {
              "parent_task": "API Development",
              "reported_by": self.user_2,
              "assigned_to": self.user,
              "project": self.project_2,
              "name": "API Authentication",
              "description": "Implement secure authentication mechanisms for API",
              "due_date": "2024-04-15 13:00:00+00:00"
            },
            {
              "reported_by": self.user_2,
              "assigned_to": self.user,
              "project": self.project_3,
              "name": "Performance Testing",
              "description": "Conduct comprehensive performance testing",
              "due_date": "2024-04-20 13:00:00+00:00"
            }
          ]
        for task_data in TASK_DATA:
            if "parent_task" in task_data:
                task_data['parent_task'] = Task.objects.get(name=task_data['parent_task'])
            task = Task.objects.get_or_create(name=task_data['name'], defaults=task_data)
