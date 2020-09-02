from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseNotAllowed
from django.utils import timezone

from .models import *
from .forms import *

# Create your views here.
def cv_view(request):
   work_experiences = WorkExperience.objects.all().order_by('-time_end', '-time_start')
   projects = Project.objects.all().order_by('-time_end', '-time_start')
   skills = Skill.objects.all().order_by('skill_type', '-proficiency')
   education = Education.objects.all().order_by('-time_end', '-time_start')
   return render(request, 'cv/cv.html', {'work_experiences': work_experiences, 'projects': projects, 'skills': skills, 'education': education})

def cv_edit_overview(request):
   if not request.user.is_authenticated:
      raise HttpResponseNotAllowed
   work_experiences = WorkExperience.objects.all()
   projects = Project.objects.all()
   skills = Skill.objects.all()
   education = Education.objects.all()
   return render(request, 'cv/cv_edit_overview.html', {'work_experiences': work_experiences, 'projects': projects, 'skills': skills, 'education': education})

def cv_edit(request, sub, pk):
   """Get editing form page for specific CV component uniquely defined by sub and pk

   Args:
       request (HttpRequest): Request
       sub (str): type of CV component
       pk (int): key to identify object in the db

   Raises:
       HttpResponseNotAllowed: Only allowed to be called when authenticated prior

   Returns:
       [type]: [description]
   """
   if not request.user.is_authenticated:
      raise HttpResponseNotAllowed
   if sub == 'work':
      return edit_work_experience(request, pk)
   elif sub == 'project':
      return edit_project(request, pk)
   elif sub == 'skill':
      return edit_skill(request, pk)
   elif sub == 'edu':
      return edit_education(request, pk)
   else:
      raise Http404
   
def cv_add(request, sub):
   if sub == 'work':
      form = WorkExperienceForm(request.POST) if request.method == 'POST' else WorkExperienceForm()
   elif sub == 'project':
      form = ProjectForm(request.POST) if request.method == 'POST' else ProjectForm()
   elif sub == 'skill':
      form = SkillForm(request.POST) if request.method == 'POST' else SkillForm()
   elif sub == 'edu':
      form = EducationForm(request.POST) if request.method == 'POST' else EducationForm()
   else:
      raise Http404
      
   if form.is_valid():
      component = form.save(commit=False)
      component.last_updated = timezone.now()
      component.save()
      return redirect('cv_edit_overview')
   
   return render(request, 'cv/cv_add.html', {'form': form})

def cv_delete(request, sub, pk):
   if sub == 'work':
      WorkExperience.objects.filter(pk=pk).delete()
   elif sub == 'project':
      Project.objects.filter(pk=pk).delete()
   elif sub == 'skill':
      Skill.objects.filter(pk=pk).delete()
   elif sub == 'edu':
      Education.objects.filter(pk=pk).delete()
   else:
      raise Http404
   return redirect('cv_edit_overview')
         
   

def edit_work_experience(request, pk):
   """ Helper function for editing work experience """
   work_experience = get_object_or_404(WorkExperience, pk=pk)
   if request.method == "POST":
      form = WorkExperienceForm(request.POST, instance=work_experience)
      if form.is_valid():
         work_experience = form.save()
         return redirect('/cv/edit')
   else:
      form = WorkExperienceForm(instance=work_experience)
   return render(request, 'cv/cv_edit.html', {'form': form})

def edit_project(request, pk):
   """ Helper function for editing projects """
   project = get_object_or_404(Project, pk=pk)
   if request.method == "POST":
      form = ProjectForm(request.POST, instance=project)
      if form.is_valid():
         project = form.save()
         return redirect('/cv/edit')
   else:
      form = ProjectForm(instance=project)
   return render(request, 'cv/cv_edit.html', {'form': form})

def edit_skill(request, pk):
   """ Helper function for editing skills """
   skill = get_object_or_404(Skill, pk=pk)
   if request.method == "POST":
      form = SkillForm(request.POST, instance=skill)
      if form.is_valid():
         skill = form.save()
         return redirect('/cv/edit')
   else:
      form = SkillForm(instance=skill)
   return render(request, 'cv/cv_edit.html', {'form': form})

def edit_education(request, pk):
   """ Helper function for editing education """
   education = get_object_or_404(Education, pk=pk)
   if request.method == "POST":
      form = EducationForm(request.POST, instance=education)
      if form.is_valid():
         education = form.save()
         return redirect('/cv/edit')
   else:
      form = EducationForm(instance=education)
   return render(request, 'cv/cv_edit.html', {'form': form})