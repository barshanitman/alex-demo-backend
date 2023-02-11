from django.urls import path
from . import views

urlpatterns = [
    path('project/',views.projects,name="projects"),
    path('project/<str:id>',views.get_project_by_id,name="projects"),
    path('user/',views.users,name="users"),
    path('ticket/',views.tickets,name="tickets"),
]
