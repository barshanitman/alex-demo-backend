import pytest
import json
from rest_framework.test import APIClient
from django.test import Client
from base.models import User

client = APIClient()

@pytest.mark.django_db
def test_get_all_users():
    response  = client.get("/api/user/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_user():
    User.objects.create_user(username = 'john',email="john.doe@gmail.com",password="!Hello123")
    number_of_users = User.objects.all().count()
    assert number_of_users == 1


@pytest.mark.django_db
def test_get_all_projects():
    response  = client.get("/api/project/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_new_project(user):
    new_project = dict(name="Test Project",description="This is a test project",creator=user.id)
    response = client.post("/api/project/",new_project)
    print(response)
    assert response.status_code == 201
    
   
  


    
    

    
    


