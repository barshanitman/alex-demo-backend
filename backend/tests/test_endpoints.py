import pytest
from rest_framework.test import APIClient
from base.models import User

client = APIClient()

@pytest.mark.django_db
def test_get_all_users():
    response  = client.get("/api/user/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_user():
    new_user = dict(username="John",email="John.Doe@gmail.com",password="!Hello123")
    response = client.post("/api/user/",new_user)
    assert response.status_code == 201
   
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

@pytest.mark.django_db
def test_get_project_by_id(project):
    response = client.get(f"/api/project/{project.id}")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_all_tickets():
    response  = client.get("/api/ticket/")
    assert response.status_code == 200








