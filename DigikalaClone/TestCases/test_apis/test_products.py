from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from ProductsApp.models import Product, Store, Stock
from ProductsApp.serializers import GetProductDetailInStockSerializer, StoreGetSerializer
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
        

class CreateUserStoreTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.client.login(username=self.user.phone_number, password='password')
    
    def test_create_store(self):
        data = {
            'name':'blue',
            'address':'blue valley',
            'owner':self.user.id
        }

        url = reverse('user-store')
        res = self.client.post(url, data, 'json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, data)
    

class GetUserStoreTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.client.login(username=self.user.phone_number, password='password')
        self.store = Store.objects.create(owner=self.user, name='green', address='address')


    def test_store_of_user(self):
        url = reverse('user-store')
        res = self.client.get(url,)
        

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [StoreGetSerializer(self.store).data])
    
         


class AddProductToStoreTestCase(APITestCase):
    
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.store = Store.objects.create(owner=self.user, name='green', address='address')
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



class GetProductFromStockTestCase(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.store = Store.objects.create(owner=self.user, name='green', address='address')
        self.stock = Stock.objects.create(store=self.store, product=self.product1, unit_in_stock=10)
        self.client.login(username=self.user.phone_number, password='password')
  
    def test_get_product_from_store(self):
        url = reverse('get-product-from-stock',kwargs={'product_id':self.product1.id})
        data = GetProductDetailInStockSerializer(self.stock).data
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, data)

class PublicListOfStockTestCase(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.product2 = Product.objects.create(name='apple', price=300, description='juicy apple')
        self.user = User.objects.create(phone_number='09121234567', password='password')
        self.store = Store.objects.create(owner=self.user, name='green', address='address')
        self.stock1 = Stock.objects.create(store=self.store, product=self.product1, unit_in_stock=10)
        self.stock2 = Stock.objects.create(store=self.store, product=self.product2, unit_in_stock=30)
        
        
    def test_get_list_of_product(self):
        url = reverse('public-list-of-stock')
        res = self.client.get(url,None, 'json')

        stocks = Stock.objects.all()
        data = GetProductDetailInStockSerializer(stocks, many=True).data
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, data)