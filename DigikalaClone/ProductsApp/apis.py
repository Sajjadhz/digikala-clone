from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import CreateProductSerializer, GetSingleProductSerializer
from .models import Product
from rest_framework import permissions

class CreateProductApi(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetSingleProductApi(RetrieveAPIView):
    serializer_class = GetSingleProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return  Product.objects.get(id=self.kwargs['id'])
