from django.db import models
from django.utils import timezone

   
class WorkExperience(models.Model):
   job_title = models.CharField(max_length=100)
   company_name = models.CharField(max_length=50, null=False)
   time_start = models.CharField(max_length=20)
   time_end = models.CharField(max_length=20, blank=True, null=True)
   employment_type = models.CharField(max_length=50)
   location = models.CharField(max_length=30)
   details = models.TextField()
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return f'{self.job_title} at {self.company_name} ({self.employment_type})'
   
class Project(models.Model):
   name = models.CharField(max_length=100)
   project_type = models.CharField(max_length=50)
   time_start = models.CharField(max_length=20)
   time_end = models.CharField(max_length=20, blank=True, null=True)
   details = models.TextField()
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return f'{self.project_type}: {self.name}'
   
class Skill(models.Model):
   name = models.CharField(max_length=50)
   skill_type = models.CharField(max_length=25, choices=[('Programming', 'Programming'), ('Markup', 'Markup'), ('Technologies and Tools', 'Technologies and Tools'), ('Languages', 'Languages')])
   proficiency = models.IntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')], blank=True, null=True)
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return f'{self.skill_type}: {self.name}'
   
class Education(models.Model):
   institution = models.CharField(max_length=50)
   course = models.CharField(max_length=50)
   time_start = models.CharField(max_length=20)
   time_end = models.CharField(max_length=20, blank=True, null=True)
   location = models.CharField(max_length=30)
   details = models.TextField()
   last_updated = models.DateTimeField(default=timezone.now)
   show = models.BooleanField(default=True)
   
   def __str__(self):
      return f'{self.course} at {self.institution}'
   
   