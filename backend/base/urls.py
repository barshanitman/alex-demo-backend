from django.urls import path
from . import views

urlpatterns = [

    path('project/',views.get_projects,name="projects"),

]