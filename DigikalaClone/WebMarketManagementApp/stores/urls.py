from django.urls import path
from .apis import *

urlpatterns = [
    path('create/', CreateStoreAPI.as_view(), name='create-store'),
    path('detail/', GetUserstorAPI.as_view(), name='user-store')
]