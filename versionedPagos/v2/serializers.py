from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from pagos.models import (
    Services,
    Payment_user,
    Expired_payments
)


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class Payment_userSerializer(ModelSerializer):
    class Meta:
        model = Payment_user
        fields = ["id", "user_id", "service_id", "amount",
                  "paymentDate", "expirationDate"]
        # read_only_fields = "id",


class Expired_paymentsSerializer(ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = ["payment_user_id", "penalty_fee_amount"]

# class UsersSerializer(ModelSerializer):
#     class Meta:
#         model = Users
#         fields = "__all__"
