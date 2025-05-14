import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestLoginView:
    def test_login_success(self, client):
        
        # 회원가입
        client.post(reverse('signup'), {
            "username": "testuser",
            "password": "testpassword",
            "nickname": "testnickname"
        })
        
        # 로그인
        url = reverse('login')
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        
        response = client.post(url, data)
        
        assert response.status_code == status.HTTP_200_OK
        assert "token" in response.data


    def test_login_invalid_credentials(self, client):
        url = reverse('login')
        data = {
            "username": "wronguser",
            "password": "wrongpassword"
        }
        
        response = client.post(url, data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["error"]["code"] == "INVALID_CREDENTIALS"
        assert response.data["error"]["message"] == "아이디 또는 비밀번호가 올바르지 않습니다."