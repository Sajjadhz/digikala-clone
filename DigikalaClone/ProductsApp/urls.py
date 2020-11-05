from django.urls import path
from .apis import *


urlpatterns = [
    path('create/',CreateProductApi.as_view(), name='create-product')
]