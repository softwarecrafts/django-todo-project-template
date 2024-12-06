from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Uses Factories to setup objects in the database so the platform
    can work correctly.

    This will be used to reset staging or future sandbox environments
    """

    def handle(self, **options):
        if settings.ENVIRONMENT == "production":
            return
        self.main()

    def main(self):
        self.setup_users()
        self.setup_projects()
        self.setup_tasks()

    def setup_users(self):
        pass
        # self.admin = UserFactory(is_superuser=True, is_staff=True, ...)

    def setup_projects(self):
        pass
        # self.project_1 = ProjectFactory(name='Christmas setup')

    def setup_tasks(self):
        pass
        # t1 = TaskFactory(name='Wrap presents', project=self.project_1)
        # TaskFactory(name='Buy presents', project=self.project_1, parent_task=t1)
