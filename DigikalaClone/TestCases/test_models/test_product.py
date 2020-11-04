from django.test import TestCase
from django.contrib.auth import get_user_model
from ProductsApp.models import Product, Provider, Stock

User = get_user_model()

class ProductModelTestCase(TestCase):
    def test_create_model(self):
        data = {
            'name': 'apple',
            'price': '300',
          'description': 'nice, juicy apple'
        }

        product = Product.objects.create(**data)

        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product, Product.objects.get(**data))

class ProviderModelTestCase(TestCase):
    def setUp(self):
        self.owner = User.objects.create(phone_number='09121234567', password='password')
    
    def test_create_model(self):
        data = {
            'owner':self.owner,
            'name': 'green garden',
            'address': 'green alley'
        }

        store = Provider.objects.create(**data)

        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(store, Provider.objects.get(**data))


class StockModelTestCase(TestCase):
    def setUp(self):
        self.owner = User.objects.create(phone_number='09121234567', password='password')
        self.store = Provider.objects.create(owner = self.owner, name='green garden',
                                             address = 'green alley')
        self.product = Product.objects.create(name= 'apple', price= '300',
                                              description='nice, juicy apple')
    
    def test_create_model(self):
        data = {
            'store':self.store,
            'product': self.product,
            'unit_in_stock': 20
        }