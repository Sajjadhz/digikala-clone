from django.contrib.auth import get_user_model
from WebMarketManagementApp.stores.models import Store, Stock
from WebMarketManagementApp.stores.serializers import StoreGetSerializer
from rest_framework import serializers
from .models import  Product
from rest_framework.validators import UniqueTogetherValidator

class GetProductSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'name',]

            

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['price', 'description', 'name','id']
        extra_kwargs = {'id':{'read_only':True}}


class AddProductToStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['store', 'product', 'unit_in_stock']


class GetProductDetailInStockSerializer(serializers.ModelSerializer):
    store = StoreGetSerializer()
    product = GetProductSmallSerializer()
    class Meta:
        model  = Stock
        fields = ['store', 'product', 'unit_in_stock']


class GetSingleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'description', 'name']

