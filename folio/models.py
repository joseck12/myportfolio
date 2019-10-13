from django.db import models

# Create your models here.
"""
Initializing Project Model

"""
class Project(models.Model):
    project_title = models.CharField(max_length=255, null=True, blank=True)
    project_link = models.CharField(max_length=255, null=True, blank=True)
    project_picture = models.ImageField(upload_to='pics/', blank=True, null=True)
    project_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.project_title)

"""
Initializing Skill Model

"""
class Skill(models.Model):
    skill_title = models.CharField(max_length=255, null=True, blank=True)
    skill_description = models.TextField(null=True)
"""
Initializing Personal_Information Model

"""

class Personal_Information(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    github_name = models.CharField(max_length=255, null=True, blank=True)
    linkedin_name = models.CharField(max_length=255, null=True, blank=True)
    my_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True)

    def __str__(self):
        return str(self.email)
