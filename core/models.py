from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = True


class Customer(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        db_column='tx_email',
        null=False,
        blank=False,
    )
    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=11,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.cpf} + {self.name}'

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Phone(ModelBase):
    number = models.CharField(
        db_column='tx_number',
        max_length=12,
        null=False,
        blank=False,
    )

    customer = models.ForeignKey(
        Customer,
        db_column='id_customer',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        db_table = 'phone'
        verbose_name = 'Phone'
        verbose_name_plural = 'Phone'


class Vehicle(ModelBase):
    class VehicleType(models.IntegerChoices):
        CAR = 1
        MOTORCYCLE = 2
        TRUCK = 3

    year = models.IntegerField(
        db_column='nb_year',
        null=False,
        blank=False,
        validators=[MaxValueValidator(9999), MinValueValidator(1500)]
    )
    type = models.IntegerField(
        db_column='nb_type',
        choices=VehicleType.choices,
        default=VehicleType.CAR,
        null=False,
        blank=False,
    )
    color = models.CharField(
        db_column='tx_color',
        null=False,
        blank=False,
    )
    license_plate = models.CharField(
        db_column='nb_license_plate',
        max_length=7,
        null=False,
        blank=False,
    )
    km = models.IntegerField(
        db_column='nb_km',
        null=False,
        blank=False,
        validators=[MinValueValidator(0)]
    )
    customer = models.ForeignKey(
        Customer,
        db_column='id_customer',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    car_model = models.ForeignKey(
        'CarModel',
        db_column='id_car_model',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.car_model.name} - {self.license_plate}'

    class Meta:
        db_table = 'vehicle'
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class CarModel(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )

    brand = models.ForeignKey(
        'Brand',
        db_column='id_brand',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.id} + {self.name}'

    class Meta:
        db_table = 'model'
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Brand(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.id} + {self.name}'

    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Service(ModelBase):
    class Status(models.IntegerChoices):
        NOT_STARTED = 1
        IN_PROGRESS = 2
        FINISHED = 3

    value = models.DecimalField(
        db_column='nb_amount',
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    status = models.IntegerField(
        db_column='nb_status',
        choices=Status.choices,
        default=Status.NOT_STARTED,
        null=False,
        blank=False,
    )
    delivery_deadline = models.DateTimeField(
        db_column='dt_delivery_deadline',
        null=False,
        blank=False,
    )
    start_date = models.DateTimeField(
        db_column='dt_start_date',
        null=False,
        blank=False,
    )
    end_date = models.DateTimeField(
        db_column='dt_end_date',
        null=False,
        blank=False,
    )
    description = models.TextField(
        db_column='tx_description',
        max_length=240,
        null=False,
        blank=False,
    )

    vehicle = models.ForeignKey(
        Vehicle,
        db_column='id_vehicle',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'{self.id}'


class Payment(ModelBase):
    discount = models.DecimalField(
        db_column='nb_discount',
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    total = models.DecimalField(
        db_column='nb_total',
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )

    service = models.ForeignKey(
        Service,
        db_column='id_service',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    method = models.ForeignKey(
        'Method',
        db_column='id_method',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'payment'
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f'{self.id} + {self.total}'


class Method(ModelBase):
    payment_type = models.CharField(
        db_column='tx_payment_type',
        max_length=120,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'payment_type'
        verbose_name = 'Payment_type'
        verbose_name_plural = 'Payment_types'

    def __str__(self):
        return f'{self.id} + {self.payment_type}'


class Address(ModelBase):
    cep = models.CharField(
        db_column='tx_cep',
        max_length=8,
        null=False,
        blank=False,
    )
    street = models.CharField(
        db_column='tx_street',
        max_length=120,
        null=False,
        blank=False,
    )
    city = models.CharField(
        db_column='tx_city',
        max_length=120,
        null=True,
        blank=True,
    )
    neighborhood = models.CharField(
        db_column='tx_neighborhood',
        max_length=120,
        null=False,
        blank=False,
    )
    house_number = models.IntegerField(
        db_column='nb_house_number',
        null=False,
        blank=False,
    )
    complement = models.CharField(
        db_column='tx_complement',
        max_length=120,
        null=False,
        blank=False,
    )
    reference = models.CharField(
        db_column='tx_reference',
        max_length=120,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return f'{self.street} - {self.neighborhood} - {self.house_number} - {self.complement} - {self.cep}'

class Employer(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        db_column='tx_email',
        null=False,
        blank=False,
    )
    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=11,
        null=False,
        blank=False,
    )
    salary = models.DecimalField(
        db_column='nb_salary',
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )
    class Meta:
        db_table = 'employer'
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

        def __str__(self):
            return f'{self.name} + {self.salary}'

class Position(ModelBase):
    position = models.CharField(
        db_column='tx_position',
        max_length=120,
        null=False,
        blank=False,
    )
    employer = models.ForeignKey(
        Employer,
        db_column='id_employer',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'position'
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

        def __str__(self):
            return f'{self.position}'