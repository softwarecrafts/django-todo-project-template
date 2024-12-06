from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import ProjectForm, TaskForm
from .models import Project, Task

def project_list(request):
    return render(request, 'projects/list.html', {
        "projects": Project.objects.filter(created_by=request.user)
    })

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.created_by != request.user:
        raise Http404()
    return render(request, 'projects/detail.html', {
        "project": project,
        "tasks": project.tasks.all()
    })


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {
        "task": task
    })


class ProjectCreateView(CreateView):
    queryset = Project.objects.all()
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

class TaskCreateView(CreateView):
    queryset = Task.objects.all()
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'task_id': self.instance.pk})

class ProjectUpdateView(UpdateView):
    queryset = Project.objects.all()
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'project_id': self.instance.pk})

class TaskUpdateView(UpdateView):
    queryset = Task.objects.all()
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'task_id': self.instance.pk})
