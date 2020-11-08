from django.db import models
from django.contrib.auth import get_user_model


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

