from django.contrib import admin
from .models import DevelopmentProject, ProjectUpdate, ProjectImage

admin.site.register(DevelopmentProject)
admin.site.register(ProjectUpdate)
admin.site.register(ProjectImage)