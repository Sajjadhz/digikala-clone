from django.urls import path
from .apis import *


urlpatterns = [
    path('create/',CreateProductApi.as_view(), name='create-product'),
    path('get/<int:id>', GetSingleProductApi.as_view(), name='get-product')
]