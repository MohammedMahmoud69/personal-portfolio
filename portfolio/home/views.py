from django.shortcuts import render
from about.models import About
from services.models import Services
from projects.models import Projects
from opinions.models import Opinions
from django.contrib import messages
# Create your views here.

def home(request):
    about = About.objects.all()

    services = Services.objects.all()

    projects = Projects.objects.all()

    opinions = Opinions.objects.all()

    return render(request, 'home/index.html', {'abouts':about, 'services':services, 'projects':projects, 'opinions':opinions})