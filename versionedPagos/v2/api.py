from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly,
    DjangoModelPermissions
)
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from .pagination import StandardResultsSetPagination
# from drf_roles.mixins import RoleViewSetMixin
from rest_framework_roles.granting import is_self
from pagos.models import (
    Services,
    Payment_user,
    Expired_payments
)
from .serializers import (
    ServicesSerializer,
    Payment_userSerializer,
    Expired_paymentsSerializer
)

import datetime


class ServicesViewSet(viewsets.ModelViewSet):
    # Descomentar para que funcionen los roles
    # permission_classes = [DjangoModelPermissions]
    serializer_class = ServicesSerializer

    pagination_class = StandardResultsSetPagination
    throttle_scope = 'pagos_2'
    # throttle_scope = 'pagos_2_prueba'

    http_method_names = ['get', ]

    def get_queryset(self):
        queryset = Services.objects.all()
        return queryset


class Payment_userViewSet(viewsets.ModelViewSet):
    # Descomentar para que funcionen los roles
    # permission_classes = [DjangoModelPermissions]
    queryset = Payment_user.objects.all()
    serializer_class = Payment_userSerializer

    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['paymentDate', 'expirationDate']
    throttle_scope = 'pagos'
    # throttle_scope = 'pagos_prueba'

    def create(self, request, *args, **kwargs):
        user = request.user

        if len(request.data['paymentDate']) > 0 and len(request.data['expirationDate']) > 0:
            print("holaaaaaaaa", request.data)

            serializer = self.serializer_class(
                data=request.data, context={'author': user})

            data = {
                "paymentDate": datetime.date.fromisoformat(request.data['paymentDate']),
                "expirationDate": datetime.date.fromisoformat(request.data['expirationDate']),
                "penalidad": float(request.data['amount']) * 0.5,
            }

            if serializer.is_valid():
                serializer.save()

                if data["paymentDate"] > data["expirationDate"]:
                    # payment_id = Payment_user.objects.get(
                    #     pk=serializer.data['id'])
                    expiration = Expired_payments(
                        penalty_fee_amount=data['penalidad'], payment_user_id_id=serializer.data['id'])
                    expiration.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Expired_paymentsViewSet(viewsets.ModelViewSet):
    # Descomentar para que funcionen los roles
    # permission_classes = [DjangoModelPermissions]
    queryset = Expired_payments.objects.all()
    serializer_class = Expired_paymentsSerializer

    pagination_class = StandardResultsSetPagination
    throttle_scope = 'pagos_2'
    # throttle_scope = 'pagos_2_prueba'
