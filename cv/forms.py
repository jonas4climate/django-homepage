from django import forms

from .models import *

class WorkExperienceForm(forms.ModelForm):
   class Meta:
      model = WorkExperience
      fields = '__all__'
      exclude = ['last_updated',]
      
class ProjectForm(forms.ModelForm):
   class Meta:
      model = Project
      fields = '__all__'
      exclude = ['last_updated',]
      
class SkillForm(forms.ModelForm):
   class Meta:
      model = Skill
      fields = '__all__'
      exclude = ['last_updated',]
      
class EducationForm(forms.ModelForm):
   class Meta:
      model = Education
      fields = '__all__'
      exclude = ['last_updated',]
      