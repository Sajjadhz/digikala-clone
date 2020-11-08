from WebMarketManagementApp.stores.models import Stock, Store
from rest_framework import  permissions
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import (AddProductToStockSerializer, GetSingleProductSerializer, 
                          CreateProductSerializer,GetProductDetailInStockSerializer,
                         )
from .models import  Product




class ListCreateProductAPI(ListCreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.all()

class GetSingleProductAPI(RetrieveAPIView):
    serializer_class = GetSingleProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return  get_object_or_404(Product.objects.filter(id=self.kwargs['id']))




class CreateStockForProductAPI(CreateAPIView):
    serializer_class = AddProductToStockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product.objects.filter(id=product_id))
        store = get_object_or_404(Store.objects.filter(owner_id=request.user.id))
        if Stock.objects.filter(store=store, product=product).count() != 0:
            return Response({'error':'This product is already registered in stock'})
        request.data['store'] = store.id
        request.data['product'] = product_id
        return super().post(request, *args, **kwargs)


class GetProductDetailInStockAPI(RetrieveAPIView):
    serializer_class = GetProductDetailInStockSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Stock.objects.get(product_id=self.kwargs['product_id']))


class PublicStockListAPI(ListAPIView):
    serializer_class = GetProductDetailInStockSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Stock.objects.all()