from django.contrib import admin
from .models import *


class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
admin.site.register(Project, ProjectsAdmin)
