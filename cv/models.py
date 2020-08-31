from django.db import models
from django.utils import timezone

class Cv(models.Model):
   work_experiences = models.ManyToManyField('WorkExperience')
   projects = models.ManyToManyField('Project')
   skills = models.ManyToManyField('Skill')
   education = models.ManyToManyField('Education')
   last_updated = models.DateTimeField(default=timezone.now, blank=True)
   
   def publish(self):
      self.save()
      
   def __str__(self):
      return str(self.work_experiences) + ',' + str(self.projects) + ',' + str(self.skills) + ',' + str(self.education) + ',' + str(self.last_updated)
   
class WorkExperience(models.Model):
   job_title = models.CharField(max_length=100)
   company_name = models.CharField(max_length=50)
   time = models.CharField(max_length=50)
   employment_type = models.CharField(max_length=50)
   location = models.CharField(max_length=50)
   details = models.TextField()
   
   def __str__(self):
      return self.job_title
   
class Project(models.Model):
   name = models.CharField(max_length=100)
   project_type = models.CharField(max_length=50)
   time = models.CharField(max_length=50)
   details = models.TextField()
   
   def __str__(self):
      return self.name
   
class Skill(models.Model):
   name = models.CharField(max_length=50)
   proficiency = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name
   
class Education(models.Model):
   institution = models.CharField(max_length=50)
   course = models.CharField(max_length=50)
   time = models.CharField(max_length=50)
   location = models.CharField(max_length=50)
   details = models.TextField()
   
   