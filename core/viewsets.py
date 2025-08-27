from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from core import models, serializers, filters


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filterset_class = filters.CustomerFilter
    permission_classes = [IsAuthenticated]

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer
    filterset_class = filters.PhoneFilter
    permission_classes = [IsAuthenticated]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    filterset_class = filters.VehicleFilter
    permission_classes = [IsAuthenticated]

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = models.CarModel.objects.all()
    serializer_class = serializers.CarModelSerializer
    filterset_class = filters.CarModelFilter
    permission_classes = [IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    filterset_class = filters.BrandFilter
    permission_classes = [IsAuthenticated]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    filterset_class = filters.ServiceFilter
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    filterset_class = filters.PaymentFilter
    permission_classes = [IsAuthenticated]

class MethodViewSet(viewsets.ModelViewSet):
    queryset = models.Method.objects.all()
    serializer_class = serializers.MethodSerializer
    permission_classes = [IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [IsAuthenticated]

