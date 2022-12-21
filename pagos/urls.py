from django.urls import path, re_path, include
from . import views
from rest_framework import routers

from versionedPagos.v2.router import api_urlpatterns as api_v2

router = routers.DefaultRouter()


router.register(r'pagos', views.PagoViewSet, 'pagos')

urlpatterns = [
    re_path(r'^api/v2/', include(api_v2)),
]

urlpatterns += router.urls
