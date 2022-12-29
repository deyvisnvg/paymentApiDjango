from .models import Pagos
from rest_framework import viewsets, filters
from .serializers import PagoSerializer
from rest_framework.permissions import DjangoModelPermissions
from .pagination import StandardResultsSetPagination


# Create your views here.
class PagoViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter]

    # permission_classes = [IsAuthenticated]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'
