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
