from django.db import models
from django.contrib.auth import get_user_model
from .managers import DigiKalaManager

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=40, null=True, blank=True)
    price = models.BigIntegerField()

    def __str__(self):
        return f'{self.name}'

    def jsonify(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'description':self.description
        }

class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    address = models.CharField(max_length=35)

class Stock(models.Model):
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    unit_in_stock = models.IntegerField(default=0)


class DigiKalaProducts(models.Model):
    objects = DigiKalaManager()
    name = models.CharField(max_length=50)
    price = models.BigIntegerField(default=0)