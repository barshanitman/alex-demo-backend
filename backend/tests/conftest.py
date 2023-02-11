import pytest
from base.serializers import UserSerializer
from rest_framework.test import APIClient
from base.models import User,Project


@pytest.fixture
def user():
    user = User.objects.create_user(username = 'john',email="john.doe@gmail.com",password="!Hello123")
    return user

@pytest.fixture
def project():
    user = User.objects.create_user(username = 'john',email="john.doe@gmail.com",password="!Hello123")
    Project.objects.create_project(name="Test Project",description="This is a test project",creator=user)
    project = Project.objects.first()
    return project
    


  
    


        

