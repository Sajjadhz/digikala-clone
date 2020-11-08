from rest_framework import serializers
from .models import DigiKalaProducts

class DigiKalaProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigiKalaProducts
        fields = ['price','name']