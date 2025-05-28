# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.

# Dealer model
class Dealer(models.Model):
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    st = models.CharField(max_length=10, blank=True, null=True)  # State abbreviation

    def __str__(self):
        return self.full_name

# Review model
class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    purchase = models.BooleanField(default=True)
    review = models.TextField()
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    sentiment = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} for {self.dealer.full_name}"


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
