from django.db import models
from .managers import DigiKalaManager
# Create your models here.

class DigiKalaProducts(models.Model):
    objects = DigiKalaManager()
    name = models.CharField(max_length=50)
    price = models.BigIntegerField(default=0)