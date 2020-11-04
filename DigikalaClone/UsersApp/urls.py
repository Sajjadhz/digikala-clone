from django.urls import path
from .apis import *


urlpatterns = [
    path('login/', LoginUserAPI.as_view(), name='login'),
    path('logout/', LogoutUserApi.as_view(), name='logout'),
    path('register/', RegisterUserApi.as_view(), name='register')
]