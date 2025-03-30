from django.shortcuts import render, redirect
from django.core.mail import send_mail  # ✅ Import send_mail
from django.contrib import messages  # ✅ Import messages
from .models import Project, Skill  # ✅ Import Skill model

def home(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'portfolio_app/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_app/about.html')

def projects(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'portfolio_app/projects.html', {'projects': projects})

def skills(request):
    skills_list = Skill.objects.all()  # ✅ Fetch skills from database
    return render(request, 'portfolio_app/skills.html', {'skills_list': skills_list})

def contact(request):
    return render(request, 'portfolio_app/contact.html')
