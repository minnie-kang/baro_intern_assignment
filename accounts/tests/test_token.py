import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestTokenVerifyView:
    def test_verify_valid_token(self, client):
        client.post(reverse('signup'), {
            "username": "testuser",
            "password": "testpass123",
            "nickname": "testnick"
        })
        
        login_response = client.post(reverse('login'), {
            "username": "testuser",
            "password": "testpass123"
        })
        
        token = login_response.data['token']
        
        url = reverse('verify')
        response = client.post(url, {"token": token})
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "유효한 토큰입니다."

    def test_verify_invalid_token(self, client):
        url = reverse('verify')
        response = client.post(url, {"token": "invalid_token"})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["error"]["code"] == "INVALID_TOKEN"