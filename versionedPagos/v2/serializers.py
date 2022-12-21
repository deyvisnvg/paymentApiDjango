from rest_framework.serializers import ModelSerializer
from pagos.models import (
    Services,
    Users,
    Payment_user,
    Expired_payments
)


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class Payment_userSerializer(ModelSerializer):
    class Meta:
        model = Payment_user
        fields = "__all__"


class Expired_paymentsSerializer(ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = "__all__"
