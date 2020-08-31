from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Cv)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)