from django.contrib import admin
from .models import Project,Skill,Personal_Information,Contact

# Register your models here.
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Personal_Information)
admin.site.register(Contact)
