from django.urls import path
from .apis import *

urlpatterns = [
    path('products/', DigiKalaProductsListAPI.as_view(), name='digikala-list'),
    path('update/', UpdateDigiKalaAPI.as_view(), name='update-site'),
    path('changes/', ChangeLogProductListAPI.as_view(), name='change-log')
]