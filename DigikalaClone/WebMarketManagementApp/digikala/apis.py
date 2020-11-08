from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .tasks import update_products
from rest_framework.permissions import AllowAny
from .models import DigiKalaProducts
from .serializers import DigiKalaProductsSerializer

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
        return DigiKalaProducts.objects.refine_by_queryparams(self.request)