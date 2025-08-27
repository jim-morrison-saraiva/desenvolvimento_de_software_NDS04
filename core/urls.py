from rest_framework import routers
from core import viewsets

router = routers.DefaultRouter()
router.register('customer', viewsets.CustomerViewSet)
router.register('phone', viewsets.PhoneViewSet)
router.register('vehicle', viewsets.VehicleViewSet)
router.register('carmodel', viewsets.CarModelViewSet)
router.register('brand', viewsets.BrandViewSet)
router.register('service', viewsets.ServiceViewSet)
router.register('payment', viewsets.PaymentViewSet)
router.register('method', viewsets.MethodViewSet)
router.register('address', viewsets.AddressViewSet)
urlpatterns = router.urls