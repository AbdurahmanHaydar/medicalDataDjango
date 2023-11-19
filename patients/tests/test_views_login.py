import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_my_token_obtain_pair_view():
    user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
    url = reverse('token_obtain_pair')
    client = APIClient()

    request_data = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = client.post(url, request_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data
