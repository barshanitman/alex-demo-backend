import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_get_all_projects():
    response  = client.get("/api/project/")
    assert response.status_code == 200


    
    


    
    

    
    


