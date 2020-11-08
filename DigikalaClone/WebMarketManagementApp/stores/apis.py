from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import AddStoreSerializer, StoreGetSerializer
from .models import Store


class CreateStoreAPI(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddStoreSerializer

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        return super().post(request, *args, **kwargs)


class GetUserstorAPI(ListAPIView):
    serializer_class = StoreGetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)

class StockListInStoreAPI(ListAPIView):
    pass

