from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    price = models.BigIntegerField()

class Provider(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    address = models.CharField(max_length=35)

class Stock(models.Model):
    store = models.ForeignKey('provider', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    unit_in_stock = models.IntegerField(default=0)
