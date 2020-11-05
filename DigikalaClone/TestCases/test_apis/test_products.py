from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from ProductsApp.models import Product, Provider, Stock
from ProductsApp.serializers import GetProductDetailInStockSerializer
from rest_framework import status

User = get_user_model()

class CreateGetProductTestCase(APITestCase):
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

        url = reverse('get-product', kwargs={'id':self.product1.id})

        res = self.client.get(url,)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, self.product1.jsonify())        
        

class AddProductToStoreTestCase(APITestCase):
    
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.store = Provider.objects.create(owner=self.user, name='green', address='address')
        self.client.login(username=self.user.phone_number, password='password')
    
    def test_add_product_to_store(self):
        url = reverse('add-product-to-store', kwargs={'store_id':self.store.id, 'product_id':self.product1.id})
        data = {'product':self.product1.id,
        'store':self.store.id,
        'unit_in_stock': 100
        }

        res = self.client.post(url, data, 'json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, data)



class GetProductFromStockTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.store = Provider.objects.create(owner=self.user, name='green', address='address')
        self.stock = Stock.objects.create(store=self.store, product=self.product1, unit_in_stock=10)
        self.client.login(username=self.user.phone_number, password='password')
  
    def test_get_product_from_store(self):
        url = reverse('get-product-from-stock',kwargs={'product_id':self.product1.id})
        data = GetProductDetailInStockSerializer(self.stock).data
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, data)

class PublicListOfStockTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.store = Provider.objects.create(owner=self.user, name='green', address='address')
        self.stock = Stock.objects.create(store=self.store, product=self.product1, unit_in_stock=10)
        
        
    def test_get_list_of_product(self):
        url = reverse('public-list-of-stock')
        res = self.client.get(url)
        stocks = Stock.objects.all()
        data = GetProductDetailInStockSerializer(stocks, many=True).data
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, data)