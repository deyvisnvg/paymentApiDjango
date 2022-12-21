from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'services', api.ServicesViewSet, 'services')
router.register(r'user', api.UsersViewSet, 'users')
router.register(r'payment_user', api.Payment_userViewSet, 'paymentuser')
router.register(r'expired_payment',
                api.Expired_paymentsViewSet, 'expiredpayment')

api_urlpatterns = router.urls
