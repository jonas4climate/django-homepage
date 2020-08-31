from django import forms

from .models import *

class CvForm(forms.ModelForm):

   class Meta:
      model = Cv
      fields = '__all__'