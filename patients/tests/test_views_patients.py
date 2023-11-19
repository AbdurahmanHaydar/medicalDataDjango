import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='12345')
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def patient_data():
    return {
        'Name': 'John Doe',
        'DateOfBirth': '1990-01-01',
        'AppointmentDate': '2023-12-01',
        'Gender': 'Male',
        'ContactInformation': '+27 712345698, johndoe@gmail.com'
    }

@pytest.mark.django_db
def test_create_patient(api_client, patient_data):
    url = reverse('create-patient')
    response = api_client.post(url, patient_data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['Name'] == patient_data['Name']
