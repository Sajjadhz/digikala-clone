from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import CreateProductSerializer
from .models import Product
from rest_framework import permissions

class CreateProductApi(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.IsAuthenticated]
