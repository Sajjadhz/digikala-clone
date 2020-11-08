from rest_framework import serializers
from .models import Store

class StoreGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'address','id']


class AddStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'owner', 'address']
      