from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseNotAllowed
from django.utils import timezone

from .models import *
from .forms import *

# Create your views here.
def post_cv_view(request):
   work_experiences = WorkExperience.objects.all()
   projects = Project.objects.all()
   skills = Skill.objects.all()
   education = Education.objects.all()
   return render(request, 'cv/cv.html', {'work_experiences': work_experiences, 'projects': projects, 'skills': skills, 'education': education})

def post_cv_edit_overview(request):
   if not request.user.is_authenticated:
      raise HttpResponseNotAllowed
   work_experiences = WorkExperience.objects.all()
   projects = Project.objects.all()
   skills = Skill.objects.all()
   education = Education.objects.all()
   return render(request, 'cv/post_edit_overview.html', {'work_experiences': work_experiences, 'projects': projects, 'skills': skills, 'education': education})

def post_cv_edit(request, sub, pk):
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
      return Http404
   
   
def edit_work_experience(request, pk):
   work_experience = get_object_or_404(WorkExperience, pk=pk)
   if request.method == "POST":
      form = WorkExperienceForm(request.POST, instance=work_experience)
      if form.is_valid():
         work_experience = form.save()
         return redirect('/cv', pk=work_experience.pk)
   else:
      form = WorkExperienceForm()
   return render(request, 'cv/post_edit.html', {'form': form})

def edit_project(request, pk):
   project = get_object_or_404(Project, pk=pk)
   if request.method == "POST":
      form = ProjectForm(request.POST, instance=project)
      if form.is_valid():
         project = form.save()
         return redirect('/cv', pk=project.pk)
   else:
      form = ProjectForm()
   return render(request, 'cv/post_edit.html', {'form': form})

def edit_skill(request, pk):
   skill = get_object_or_404(Skill, pk=pk)
   if request.method == "POST":
      form = SkillForm(request.POST, instance=skill)
      if form.is_valid():
         skill = form.save()
         return redirect('/cv', pk=skill.pk)
   else:
      form = SkillForm()
   return render(request, 'cv/post_edit.html', {'form': form})

def edit_education(request, pk):
   education = get_object_or_404(Education, pk=pk)
   if request.method == "POST":
      form = Education(request.POST, instance=education)
      if form.is_valid():
         education = form.save()
         return redirect('/cv', pk=education.pk)
   else:
      form = Education()
   return render(request, 'cv/post_edit.html', {'form': form})