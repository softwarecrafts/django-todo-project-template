from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import now

from .forms import ProjectForm, TaskForm
from .models import Project, Task


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/projects/'


def project_list(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(created_by=request.user)
    else:
        projects = Project.objects.all()
    return render(
        request,
        "projects/list.html",
        {"projects": projects},
    )


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.created_by != request.user:
        raise Http404()
    return render(
        request,
        "projects/detail.html",
        {"project": project, "tasks": project.tasks.all()},
    )


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task})


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("project_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class TaskCreateView(CreateView):
    model = Project
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy("task_detail", kwargs={"task_id": self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.reported_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProjectUpdateView(UpdateView):
    queryset = Project.objects.all()
    form_class = ProjectForm
    model = Project
    pk_url_kwarg = 'project_id'

    def get_success_url(self):
        return reverse_lazy("project_detail", kwargs={"project_id": self.object.pk})


class TaskUpdateView(UpdateView):
    queryset = Task.objects.all()
    form_class = TaskForm
    model = Task
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse_lazy("task_detail", kwargs={"task_id": self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse_lazy("project_detail", kwargs={"project_id": self.object.project.pk})

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("project_list")
    pk_url_kwarg = 'project_id'

def dashboard(request):
    my_tasks = Task.objects.filter(assigned_to=request.user)
    my_projects = Project.objects.filter(created_by=request.user)
    todays_tasks = Task.objects.filter(due_date__date=now().date())
    return render(
        request,
        "index.html",
        {
            "my_tasks": my_tasks,
            "my_projects": my_projects,
            "todays_tasks": todays_tasks,
        },
    )
