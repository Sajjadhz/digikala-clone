from django.db import models
from WebMarketManagementApp.products.models import Product
from django.contrib.auth import get_user_model


# Create your models here.
class Store(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    address = models.CharField(max_length=35)

class Stock(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_in_stock = models.IntegerField(default=0)

