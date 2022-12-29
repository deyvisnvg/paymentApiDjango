from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


# Create your models here.
class Pagos(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')
    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    monto = models.FloatField(default=0.0)
    fecha_pago = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'pagos'


# class Users(models.Model):
#     email = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'users'

#     def __str__(self):
#         return self.username


class Services(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NETFLIX', _('Netflix')
        AMAZON = 'AMAZON', _('Amazon Video')
        START = 'START', _('Start+')
        PARAMOUNT = 'PARAMOUNT', _('Paramount+')
    name = models.CharField(
        max_length=15,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    description = models.TextField()
    logo = models.TextField()

    class Meta:
        db_table = 'services'

    def __str__(self):
        return self.name


class Payment_user(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    service_id = models.ForeignKey(
        Services, on_delete=models.CASCADE, related_name='services')
    amount = models.FloatField(default=0.0)
    paymentDate = models.DateField(null=True)
    expirationDate = models.DateField(null=True)

    class Meta:
        db_table = 'payment_user'

    def __str__(self):
        return str(self.id)


class Expired_payments(models.Model):
    id = models.AutoField(primary_key=True)
    payment_user_id = models.ForeignKey(
        Payment_user, on_delete=models.CASCADE, related_name='paymentuser')
    penalty_fee_amount = models.FloatField()

    class Meta:
        db_table = 'expired_payments'
