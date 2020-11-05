from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import AddProductToStockSerializer, GetSingleProductSerializer, CreateProductSerializer,GetProductDetailInStockSerializer
from django.shortcuts import get_object_or_404
from .models import Product, Provider, Stock
from rest_framework import permissions



class CreateProductAPI(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetSingleProductAPI(RetrieveAPIView):
    serializer_class = GetSingleProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return  Product.objects.get(id=self.kwargs['id'])


class CreateStockForProductAPI(CreateAPIView):
    serializer_class = AddProductToStockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        store_id = self.kwargs['store_id']
        product_id = self.kwargs['product_id']
        get_object_or_404(Product.objects.filter(id=product_id))
        
        if get_object_or_404(Provider.objects.filter(id=store_id)).owner != request.user:
            return Response({'error': 'You are not owner of store'}, status=status.HTTP_403_FORBIDDEN)

        request.data['store'] = store_id
        return super().post(request, *args, **kwargs)


class GetProductDetailInStockAPI(RetrieveAPIView):
    serializer_class = GetProductDetailInStockSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_object(self):
        return Stock.objects.get(product_id=self.kwargs['product_id'])

class PublicStockListAPI(ListAPIView):
    serializer_class = GetProductDetailInStockSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Stock.objects.all()



