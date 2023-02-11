import pytest
from base.serializers import UserSerializer
from rest_framework.test import APIClient
from base.models import User 


@pytest.fixture
def user():
    user = User.objects.create_user(username = 'john',email="john.doe@gmail.com",password="!Hello123")
    return user

   
    


        

