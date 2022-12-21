# Generated by Django 4.1.4 on 2022-12-21 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pagos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "servicio",
                    models.CharField(
                        choices=[
                            ("NF", "Netflix"),
                            ("AP", "Amazon Video"),
                            ("ST", "Start+"),
                            ("PM", "Paramount+"),
                        ],
                        default="NF",
                        max_length=2,
                    ),
                ),
                ("monto", models.FloatField(default=0.0)),
                ("fecha_pago", models.DateField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "pagos",
            },
        ),
    ]
