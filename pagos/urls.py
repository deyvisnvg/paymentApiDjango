from django.urls import path, re_path, include
from . import views
from users.views import LoginView
from rest_framework import routers

from versionedPagos.v2.router import router as api_v2

router = routers.DefaultRouter()

router.register(r'pagos', views.PagoViewSet, 'pagos')

urlpatterns = [
    path(r"api/v2/login/", LoginView.as_view(), name="signup"),
    re_path(r'^api/v2/', include(api_v2.urls)),
]

urlpatterns += router.urls
