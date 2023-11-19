import pytest
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_user_success(client):
    url = reverse('register')
    data = {
        'name': 'Test User',
        'email': 'testuser@example.com',
        'password': 'testpassword123'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == data['email']
    assert 'password' not in response.data

@pytest.mark.django_db
def test_register_user_duplicate_email(client):
    User.objects.create(
        first_name='Existing User',
        username='existinguser@example.com',
        email='existinguser@example.com',
        password=make_password('password123')
    )
    url = reverse('register')
    data = {
        'name': 'Test User',
        'email': 'existinguser@example.com',
        'password': 'testpassword123'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {'detail': 'User with this email already exists'}
