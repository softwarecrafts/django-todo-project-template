from django.test import TestCase

from .models import Project

class ProjectListViewTestCase(TestCase):

    def test_list(self):
        Project.objects.create(name='Project 1', description="test description")
        Project.objects.create(name='Project 2', description="test description")
        Project.objects.create(name='Project 3', description="test description")
        response = self.client.get('/projects/')
        self.assertContains(response, '<dt><a href="/projects/1">Project 1</a></dt>', html=True)
        self.assertContains(response, '<dt><a href="/projects/2">Project 2</a></dt>', html=True)
        self.assertContains(response, '<dt><a href="/projects/3">Project 3</a></dt>', html=True)

class ProjectCreateViewTestCase(TestCase):

    def test_valid_form(self):
        response = self.client.post('/projects/create', {
            "name": 'My New Project',
            "description": "This is a test project",
        })
        self.assertRedirects(response, "/projects/1")
        project = Project.objects.get(pk=1)
        self.assertEqual(project.title, 'My New Project')
        self.assertEqual(project.description,  "This is a test project")
