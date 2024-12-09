from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Project

User = get_user_model()

class ProjectListViewTestCase(TestCase):

    def test_list(self):
        user = User.objects.create()
        Project.objects.create(name="Project 1", description="test description", created_by=user)
        Project.objects.create(name="Project 2", description="test description", created_by=user)
        Project.objects.create(name="Project 3", description="test description", created_by=user)
        response = self.client.get("/projects/")
        self.assertContains(
            response, '<dt><a href="/projects/1">Project 1</a></dt>', html=True
        )
        self.assertContains(
            response, '<dt><a href="/projects/2">Project 2</a></dt>', html=True
        )
        self.assertContains(
            response, '<dt><a href="/projects/3">Project 3</a></dt>', html=True
        )


class ProjectCreateViewTestCase(TestCase):

    def test_valid_form(self):
        user = User.objects.create()
        self.client.force_login(user)
        response = self.client.post(
            "/projects/create",
            {
                "name": "My New Project",
                "description": "This is a test project",
            },
        )
        self.assertRedirects(response, "/projects/")
        project = Project.objects.get(pk=1)
        self.assertEqual(project.name, "My New Project")
        self.assertEqual(project.description, "This is a test project")
