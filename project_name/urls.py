from django.urls import path

from .views import project_list, project_detail, task_detail, ProjectCreateView, TaskCreateView, TaskUpdateView, ProjectUpdateView

urlpatterns = [
    path("projects/", project_list, name="project_list"),
    path("projects/<pk:project_id>", project_detail, name="project_detail"),
    path("tasks/<pk:task_id>", task_detail, name="task_detail"),
    path("projects/create", ProjectCreateView.as_view(), name="project_create"),
    path("tasks/create", TaskCreateView.as_view(), name="task_create"),
    path("projects/<pk:project_id>/edit ", ProjectUpdateView.as_view(), name="project_update"),
    path("tasks/<pk:task_id>/edit", TaskUpdateView.as_view(), name="task_update"),
]
