from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model

User= get_user_model()

class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            'phone_number':'09121234567',
            'password': 'password',
            'password2': 'password'
        }
        url = reverse('register')
        response = self.client.post(url, data, 'json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED )
        self.assertEqual(response.data,{'phone_number':data['phone_number']})

class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone_number='09121234567', password='password')
    
    def test_login(self):
        url = reverse('login')
        data = {
            'phone_number':'09121234567', 'password':'password'
        }
        response = self.client.post(url, data, 'json')
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,{'token': token.key })

class LogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone_number='09121234567', password='password')
        Token.objects.create(user=self.user)

    def test_logout(self):
        url = reverse('logout')
        self.client.login(username=self.user.phone_number, password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,{'accept': 'Logout successfully'})
        self.assertEqual(Token.objects.count(), 0)