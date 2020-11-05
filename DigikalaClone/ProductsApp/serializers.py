from rest_framework import serializers
from .models import Product, Store, Stock


class GetProductSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'name',]


class StoreGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name']


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['price', 'description', 'name',]


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
