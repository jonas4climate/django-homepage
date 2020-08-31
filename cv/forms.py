from django import forms

from .models import *

class CvForm(forms.ModelForm):

   class Meta:
      model = Cv
      fields = (
         'work_experiences',
         'projects',
         'skills',
         'education',
         )