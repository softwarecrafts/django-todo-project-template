from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
        )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "parent_task",
            "assigned_to",
            "project",
            "due_date",
        )
