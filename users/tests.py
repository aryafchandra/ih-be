from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import Analyst

class AnalystAuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('serve-register-analyst')
        self.login_url = reverse('serve-login-analyst')
        self.valid_registration_data = {
            'email': 'test@example.com',
            'password': 'TestPassword123',
            'confirmed_password': 'TestPassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '+62123456789'
        }
        self.invalid_email_data = {
            **self.valid_registration_data,
            'email': ''
        }

    def test_register_analyst_success(self):
        response = self.client.post(self.register_url, self.valid_registration_data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_register_analyst_missing_email(self):
        response = self.client.post(self.register_url, self.invalid_email_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)

    def test_register_analyst_password_mismatch(self):
        data = {
            **self.valid_registration_data,
            'confirmed_password': 'WrongPassword123'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('detail', response.data)

    def test_login_analyst_success(self):
        # Register first
        self.client.post(self.register_url, self.valid_registration_data, format='json')
        # Then login
        login_data = {
            'email': self.valid_registration_data['email'],
            'password': self.valid_registration_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_credentials(self):
        login_data = {
            'email': 'nonexistent@example.com',
            'password': 'WrongPassword'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        

