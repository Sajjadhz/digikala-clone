from rest_framework import serializers
from .models import ChangeLogProduct, DigiKalaProduct

class DigiKalaProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigiKalaProduct
        fields = ['price','name']

class DigiKalaProductSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model =DigiKalaProduct
        fields = ['name']

class ChangeLogSerializer(serializers.ModelSerializer):
    product = DigiKalaProductSmallSerializer()
    class Meta:
        model = ChangeLogProduct
        fields = ['old_price', 'new_price', 'product'] 