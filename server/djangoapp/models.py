# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Additional fields for car make
    country = models.CharField(max_length=50, blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Refers to a dealer created in Cloudant database
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    # Additional fields for car model
    engine_type = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(max_length=20, blank=True, null=True)
    transmission = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
