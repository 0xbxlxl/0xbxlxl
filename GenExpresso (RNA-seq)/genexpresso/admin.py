from django.contrib import admin

from .models import Project, Dataset

admin.site.register(Project)
admin.site.register(Dataset)