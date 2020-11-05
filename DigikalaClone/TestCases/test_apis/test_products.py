from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from ProductsApp.models import Product
from rest_framework import status

User = get_user_model()

class CreateGetProduct(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.client.login(username=self.user.phone_number, password='password')

    def test_create_product(self):
        
        url = reverse('create-product')
        data = {
            'name':'orange',
            'price':400,
            'description': 'juicy orange'
        }

        res = self.client.post(url, data, 'json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, data)

    def test_get_product(self):

        url = reverse('get-product',kwargs={'id':self.product1.id})

        res = self.client.get(url,)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, self.product1.jsonify())        
        


