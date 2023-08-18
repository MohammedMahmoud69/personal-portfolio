from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:slug>/', views.project_details, name='project'),
]