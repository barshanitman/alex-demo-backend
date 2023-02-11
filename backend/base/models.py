from django.db import models
from django.contrib.auth.models import User



# Managers
class ProjectManager(models.Manager):
    def create_project(self,creator:int,name:str,description:str):
        project = self.create(creator=creator,name=name,description=description)
        return project

# Create your models here.

class Project(models.Model):
    creator:int = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    name:str = models.CharField(max_length=256,null=False)
    description:str  = models.TextField(null=True,blank=True)
    createdAt:str = models.DateTimeField(auto_now_add=True)

    objects = ProjectManager()

    def __str__(self) -> str:
        return str(self.name)
    
class Ticket(models.Model):
    project:int = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    issueType:str = models.CharField(max_length=200,null=False)
    status:str = models.CharField(max_length=200,null=False)
    summary:str  = models.TextField(null=True,blank=True)
    description:str  = models.TextField(null=True,blank=True)
    assignee:int = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="assignee") 
    reporter:int = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="reporter") 

    def __str__(self) -> str:
        return str(self.summary)
    
class ProjectUser(models.Model):
    project:int = models.ForeignKey(Project,on_delete=models.CASCADE)
    user:int = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} in {self.project}"
    
class Stage(models.Model):
    name:str = models.CharField(max_length=200,null=False)
    project:int = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__() -> str:
        pass

