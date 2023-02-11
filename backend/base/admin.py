from django.contrib import admin
from .models import Project,Ticket,ProjectUser,Stage

# Register your models here.
admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(ProjectUser)
admin.site.register(Stage)
