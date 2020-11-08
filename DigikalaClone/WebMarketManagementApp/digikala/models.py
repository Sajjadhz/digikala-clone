from django.db import models
from .managers import DigiKalaManager
# Create your models here.

class DigiKalaProduct(models.Model):
    objects = DigiKalaManager()
    name = models.CharField(max_length=50)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def update_and_log(self,price):
        ChangeLogProduct.objects.create(product=self, old_price=self.price, new_price=price)
        return self.update(price=price)


class ChangeLogProduct(models.Model):
    product = models.ForeignKey('DigiKalaProduct', on_delete=models.CASCADE)
    old_price = models.BigIntegerField()
    new_price = models.BigIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)