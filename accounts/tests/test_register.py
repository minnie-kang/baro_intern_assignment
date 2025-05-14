import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestRegisterView:
    def test_register_success(self, client):
        url = reverse('signup')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "nickname": "testnickname"
        }
        
        response = client.post(url, data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert "username" in response.data
        assert "nickname" in response.data
        assert response.data["username"] == "testuser"
        assert response.data["nickname"] == "testnickname"

    def test_register_duplicate_user(self, client):
        url = reverse('signup')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "nickname": "testnickname"
        }
        
        client.post(url, data)
        response = client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        