from django_filters import rest_framework as filters

from core import models


# Filtros de pesquisa
LIKE = 'unaccent__icontains'  # Usando unaccent para ignorar acentos e trazer palavras semelhantes
ICONTAINS = 'icontains'       # Usando icontains para trazer palavras semelhantes
UNACCENT_IEXACT = 'unaccent__iexact'  # Usando unaccent para ignorar acentos e trazer palavras exatas
EQUALS = 'exact'              # Usando exact para trazer o campo exatas
STARTS_WITH = 'startswith'    # Usando startswith para trazer palavras que começam com o termo pesquisado
GT = 'gt'                     # maior que
LT = 'lt'                     # menor que
GTE = 'gte'                   # maior ou igual a
LTE = 'lte'                   # menor ou igual a
IN = 'in'                     # Usando in para trazer palavras que estão na lista


class CustomerFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    email = filters.CharFilter(lookup_expr=ICONTAINS)
    cpf = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Customer
        fields = ['name', 'email', 'cpf']

class PhoneFilter(filters.FilterSet):
    number = filters.CharFilter( lookup_expr=LIKE)
    customer= filters.CharFilter(field_name= 'customer__name', lookup_expr=LIKE)

    class Meta:
        model = models.Phone
        fields = ['number', 'customer']

class VehicleFilter(filters.FilterSet):
    license_plate = filters.CharFilter(lookup_expr=EQUALS)
    customer = filters.CharFilter(field_name= 'customer__name', lookup_expr=LIKE)
    model = filters.CharFilter(field_name= 'CarModel__name', lookup_expr=LIKE)
    type = filters.NumberFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Vehicle
        fields = ['license_plate', 'customer', 'model']

class CarModelFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    brand = filters.CharFilter(field_name='brand__name', lookup_expr=LIKE)

    class Meta:
        model = models.CarModel
        fields = ['name', 'brand']

class BrandFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Brand
        fields = ['name']

class ServiceFilter(filters.FilterSet):
    status = filters.NumberFilter(lookup_expr=EQUALS)
    value = filters.DateFilter(lookup_expr=LTE)
    delivery_deadline = filters.DateFilter(lookup_expr=GTE)
    start_date = filters.DateFilter(lookup_expr=GTE)
    end_date = filters.DateFilter(lookup_expr=LTE)
    description = filters.CharFilter(lookup_expr=LIKE)
    vehicle = filters.CharFilter(field_name='vehicle__license_plate', lookup_expr=EQUALS)
    customer = filters.CharFilter(field_name='vehicle__customer__name', lookup_expr=LIKE)

    class Meta:
        model = models.Service
        fields = ['status', 'value', 'delivery_deadline', 'start_date', 'end_date', 'description', 'vehicle', 'customer']

class PaymentFilter(filters.FilterSet):
    total = filters.NumberFilter(lookup_expr=GTE)
    total_min = filters.NumberFilter(field_name='total', lookup_expr=LTE)
    method = filters.CharFilter(field_name='method__payment_type', lookup_expr=LIKE)
    service = filters.CharFilter(field_name='service__status', lookup_expr=EQUALS)

    class Meta:
        model = models.Payment
        fields = ['total', 'total_min', 'method', 'service']

class MethodFilter(filters.FilterSet):
    payment_type = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Method
        fields = ['payment_type']

class AddressFilter(filters.FilterSet):
    cep = filters.NumberFilter(lookup_expr=EQUALS)
    street = filters.CharFilter(lookup_expr=LIKE)
    house_number = filters.NumberFilter(lookup_expr=EQUALS)
    complement = filters.CharFilter(lookup_expr=LIKE)
    reference = filters.CharFilter(lookup_expr=LIKE)
    city = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Address
        fields = ['cep', 'street', 'house_number', 'complement', 'reference', 'city']
