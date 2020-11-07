from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import (AddProductToStockSerializer, AddStoreSerializer, GetSingleProductSerializer, 
                          CreateProductSerializer,GetProductDetailInStockSerializer,DigiKalaProductsSerializer,
                          AddStoreSerializer, StoreGetSerializer)
from .models import DigiKalaProducts, Product, Store, Stock
from .tasks import update_products



class CreateProductAPI(CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetSingleProductAPI(RetrieveAPIView):
    serializer_class = GetSingleProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return  Product.objects.get(id=self.kwargs['id'])

class GetCreateStoreAPI(ListCreateAPIView):
    serializer_class = AddStoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddStoreSerializer
        else:
            return StoreGetSerializer

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        return super().post(request, *args, **kwargs)

class GetUserstorAPI(ListAPIView):
    serializer_class = StoreGetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)

class CreateStockForProductAPI(CreateAPIView):
    serializer_class = AddProductToStockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        store_id = self.kwargs['store_id']
        product_id = self.kwargs['product_id']
        get_object_or_404(Product.objects.filter(id=product_id))
        
        if get_object_or_404(Store.objects.filter(id=store_id)).owner != request.user:
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


class UpdateDigiKalaAPI(ListAPIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        update_products.delay()
        return Response({'status': 'ok'})

class DigiKalaProductsListAPI(ListAPIView):
    serializer_class = DigiKalaProductsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return DigiKalaProducts.objects.refine_by_queryparams(self.request)


