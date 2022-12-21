from pagos.models import (
    Services,
    Users,
    Payment_user,
    Expired_payments
)
from rest_framework import viewsets, filters
from .serializers import (
    ServicesSerializer,
    UsersSerializer,
    Payment_userSerializer,
    Expired_paymentsSerializer
)
# from rest_framework.permissions import IsAuthenticated
# from .pagination import StandardResultsSetPagination


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    # pagination_class = StandardResultsSetPagination

    # filter_backends = [filters.SearchFilter]

    # permission_classes = [IsAuthenticated]

    # search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    # throttle_scope = 'pagos'


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class Payment_userViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    # queryset = Payment_user.objects.get_queryset().order_by('id')
    serializer_class = Payment_userSerializer


class Expired_paymentsViewSet(viewsets.ModelViewSet):
    queryset = Expired_payments.objects.all()
    serializer_class = Expired_paymentsSerializer
