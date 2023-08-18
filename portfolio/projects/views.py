from django.shortcuts import render
from .models import Projects
# Create your views here.

def projects(request):
    projects = Projects.objects.all().order_by('-completed_at')

    return render(request, 'projects/projects.html', {'projects':projects})

def project_details(request, slug):
    project_detail = Projects.objects.get(slug=slug)

    return render(request, 'projects/project-details.html', {'project':project_detail})
    