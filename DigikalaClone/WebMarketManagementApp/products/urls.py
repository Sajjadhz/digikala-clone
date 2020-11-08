from django.urls import path
from .apis import *


urlpatterns = [
    path('',ListCreateProductAPI.as_view(), name='create-product'),
    path('store/<int:store_id>/add-product/<int:product_id>',CreateStockForProductAPI.as_view(), name='add-product-to-store'),
    path('get/<int:id>', GetSingleProductAPI.as_view(), name='get-product'),
    path('stock/product/<int:product_id>', GetProductDetailInStockAPI.as_view(), name='get-product-from-stock'),
    path('available/', PublicStockListAPI.as_view(), name='public-list-of-stock'),
    
]