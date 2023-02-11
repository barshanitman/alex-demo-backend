from django.urls import path
from . import views

urlpatterns = [

    path('project/',views.get_projects,name="projects"),
    path('project/<str:id>',views.get_project_by_id,name="projects"),
    path('user/',views.get_all_users,name="users"),

]