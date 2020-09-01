from django import forms

from .models import *

class WorkExperienceForm(forms.ModelForm):
   class Meta:
      model = WorkExperience
      fields = '__all__'
      
class ProjectForm(forms.ModelForm):
   class Meta:
      model = Project
      fields = '__all__'
      
class SkillForm(forms.ModelForm):
   class Meta:
      model = Skill
      fields = '__all__'
      
class EducationForm(forms.ModelForm):
   class Meta:
      model = Education
      fields = '__all__'
      