from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone

from .models import *
from .forms import CvForm

# Create your views here.
def cv_view(request):
   obj = Cv.objects.first()
   if not obj:
      raise Http404
   cv = get_object_or_404(Cv, pk=obj.pk)
   return render(request, 'cv/cv.html', {'cv': cv})
   
def cv_edit(request):
   cv = get_object_or_404(Cv)
   if request.method == "POST":
      form = CvForm(request.POST, instance=cv)
      if form.is_valid():
         cv = form.save(commit=False)
         cv.last_updated = timezone.now()
         cv.save()
         return redirect('/cv', pk=cv.id)
   else:
      form = CvForm()
   return render(request, 'blog/post_edit.html', {'form': form})