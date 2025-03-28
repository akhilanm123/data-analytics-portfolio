from django.shortcuts import render, redirect
from django.core.mail import send_mail  # ✅ Import send_mail
from django.contrib import messages  # ✅ Import messages
from .models import Project  # Import the Project model

def home(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'portfolio_app/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_app/about.html')

def projects(request):  # ✅ Add this function
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'portfolio_app/projects.html', {'projects': projects})

def skills(request):  # ✅ Add this function
    return render(request, 'portfolio_app/skills.html')


def contact(request):
    return render(request, 'portfolio_app/contact.html')
