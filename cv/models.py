from django.db import models
from django.utils import timezone

   
class WorkExperience(models.Model):
   job_title = models.CharField(max_length=100, null=False)
   company_name = models.CharField(max_length=50, null=False)
   time_start = models.DateField(default=timezone.now)
   time_end = models.DateField(default=timezone.now)
   employment_type = models.CharField(max_length=50)
   location = models.CharField(max_length=50)
   details = models.TextField()
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return f'{self.job_title} at {self.company_name}'
   
class Project(models.Model):
   name = models.CharField(max_length=100, null=False)
   project_type = models.CharField(max_length=50)
   time_start = models.DateField(default=timezone.now)
   time_end = models.DateField(default=timezone.now)
   details = models.TextField()
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return self.name
   
class Skill(models.Model):
   name = models.CharField(max_length=50, null=False)
   proficiency = models.CharField(max_length=50)
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return self.name
   
class Education(models.Model):
   institution = models.CharField(max_length=50, null=False)
   course = models.CharField(max_length=50)
   time_start = models.DateField(default=timezone.now)
   time_end = models.DateField(default=timezone.now)
   location = models.CharField(max_length=50)
   details = models.TextField()
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return self.institution
   
   