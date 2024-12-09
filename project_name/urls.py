from django.contrib import admin
from django.urls import path, include

from .views import (
    project_list,
    project_detail,
    task_detail,
    ProjectCreateView,
    TaskCreateView,
    TaskUpdateView,
    ProjectUpdateView,
    RegisterView,
    TaskDeleteView,
    ProjectDeleteView,
    dashboard
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register", RegisterView.as_view(), name='register'),
    path("projects/", project_list, name="project_list"),
    path("projects/<int:project_id>", project_detail, name="project_detail"),

    path("projects/create", ProjectCreateView.as_view(), name="project_create"),
    path(
        "projects/<int:project_id>/edit",
        ProjectUpdateView.as_view(),
        name="project_update",
    ),
    path(
        "projects/<int:project_id>/delete",
        ProjectDeleteView.as_view(),
        name="project_delete",
    ),
    path("tasks/<int:task_id>", task_detail, name="task_detail"),
    path("tasks/create", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:task_id>/edit", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:task_id>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("", dashboard, name="dashboard")
]
