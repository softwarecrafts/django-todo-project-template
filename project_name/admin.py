from django.contrib import admin

from .models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        "name",
        "created_at",
        "updated_at",
        "created_by",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "created_by",
    )

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        "name",
        "project",
        "parent_task",
        "reported_by",
        "assigned_to",
        "created_at",
        "updated_at",
        "due_date",
    )
    list_filter = (
        "project",
        "reported_by",
        "assigned_to",
        "due_date",
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
