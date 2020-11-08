from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .tasks import update_products
from rest_framework.permissions import AllowAny
from .models import ChangeLogProduct, DigiKalaProduct
from .serializers import DigiKalaProductsSerializer, ChangeLogSerializer

# Create your views here.
class UpdateDigiKalaAPI(ListAPIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        update_products.delay()
        return Response({'status': 'ok'})

class DigiKalaProductsListAPI(ListAPIView):
    serializer_class = DigiKalaProductsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return DigiKalaProduct.objects.refine_by_queryparams(self.request)

class ChangeLogProductListAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChangeLogSerializer

    def get_queryset(self):
        return ChangeLogProduct.objects.all()