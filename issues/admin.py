from django.contrib import admin
from .models import Type, Status, Issue, Project

admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Issue)
admin.site.register(Project)
