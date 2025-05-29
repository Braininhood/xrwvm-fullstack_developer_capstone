from django.core.management.base import BaseCommand
from djangoapp.models import CarMake, CarModel, Dealer, Review
from django.contrib.auth.models import User
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate database with sample car data, dealers, and reviews'

    def handle(self, *args, **options):
        self.stdout.write("🚗 POPULATING DATABASE")
        self.stdout.write("=" * 40)

        # Sample car makes and models
        car_data = [
            {
                'make': 'Toyota',
                'description': 'Japanese automotive manufacturer known for reliability',
                'country': 'Japan',
                'founded_year': 1937,
                'models': ['Camry', 'Corolla', 'Prius', 'RAV4', 'Highlander']
            },
            {
                'make': 'Honda',
                'description': 'Japanese automotive manufacturer',
                'country': 'Japan',
                'founded_year': 1946,
                'models': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit']
            },
            {
                'make': 'Ford',
                'description': 'American automotive manufacturer',
                'country': 'USA',
                'founded_year': 1903,
                'models': ['F-150', 'Mustang', 'Explorer', 'Escape', 'Focus']
            },
            {
                'make': 'BMW',
                'description': 'German luxury automotive manufacturer',
                'country': 'Germany',
                'founded_year': 1916,
                'models': ['3 Series', '5 Series', 'X3', 'X5', 'i3']
            },
            {
                'make': 'Mercedes-Benz',
                'description': 'German luxury automotive manufacturer',
                'country': 'Germany',
                'founded_year': 1926,
                'models': ['C-Class', 'E-Class', 'GLC', 'GLE', 'A-Class']
            }
        ]

        # Sample dealers
        dealer_data = [
            {
                'full_name': 'Luxury Motors Dallas',
                'city': 'Dallas',
                'state': 'Texas',
                'address': '123 Main Street',
                'zip': '75201',
                'short_name': 'Luxury Dallas'
            },
            {
                'full_name': 'Premium Auto Houston',
                'city': 'Houston',
                'state': 'Texas',
                'address': '456 Oak Avenue',
                'zip': '77001',
                'short_name': 'Premium Houston'
            },
            {
                'full_name': 'Elite Cars Austin',
                'city': 'Austin',
                'state': 'Texas',
                'address': '789 Pine Road',
                'zip': '73301',
                'short_name': 'Elite Austin'
            },
            {
                'full_name': 'Metro Motors NYC',
                'city': 'New York',
                'state': 'New York',
                'address': '321 Broadway',
                'zip': '10001',
                'short_name': 'Metro NYC'
            },
            {
                'full_name': 'Golden Gate Auto',
                'city': 'San Francisco',
                'state': 'California',
                'address': '654 Market Street',
                'zip': '94102',
                'short_name': 'Golden Gate'
            },
            {
                'full_name': 'Sunshine Motors Miami',
                'city': 'Miami',
                'state': 'Florida',
                'address': '987 Ocean Drive',
                'zip': '33101',
                'short_name': 'Sunshine Miami'
            }
        ]

        # Sample reviews
        sample_reviews = [
            "Excellent service and great cars! Highly recommend.",
            "Good experience overall, staff was helpful.",
            "Outstanding dealership with competitive prices.",
            "Professional service, will definitely return.",
            "Great selection of vehicles and financing options.",
            "Friendly staff and smooth transaction process.",
            "Very satisfied with my purchase experience.",
            "Could be better, but decent service.",
            "Amazing customer service and quality vehicles.",
            "Fair prices and honest dealing."
        ]

        created_makes = 0
        created_models = 0
        created_dealers = 0
        created_reviews = 0

        # Create car makes and models
        for make_data in car_data:
            car_make, created = CarMake.objects.get_or_create(
                name=make_data['make'],
                defaults={
                    'description': make_data['description'],
                    'country': make_data['country'],
                    'founded_year': make_data['founded_year']
                }
            )

            if created:
                created_makes += 1
                self.stdout.write(f"✅ Created car make: {car_make.name}")
            else:
                self.stdout.write(f"📋 Car make exists: {car_make.name}")

            # Create car models
            for model_name in make_data['models']:
                car_model, created = CarModel.objects.get_or_create(
                    name=model_name,
                    car_make=car_make,
                    defaults={
                        'type': random.choice(['SEDAN', 'SUV', 'COUPE', 'HATCHBACK']),
                        'year': random.randint(2020, 2023),
                        'dealer_id': random.randint(1, 6),
                        'engine_type': '4-Cylinder',
                        'fuel_type': 'Gasoline',
                        'transmission': random.choice(['Automatic', 'Manual']),
                        'color': random.choice(['White', 'Black', 'Silver', 'Blue', 'Red']),
                        'price': random.randint(20000, 60000)
                    }
                )

                if created:
                    created_models += 1
                    self.stdout.write(f"  ✅ Created model: {model_name}")

        # Create dealers
        for dealer_info in dealer_data:
            dealer, created = Dealer.objects.get_or_create(
                full_name=dealer_info['full_name'],
                defaults=dealer_info
            )

            if created:
                created_dealers += 1
                self.stdout.write(f"✅ Created dealer: {dealer.full_name}")
            else:
                self.stdout.write(f"📋 Dealer exists: {dealer.full_name}")

        # Create sample reviews
        dealers = list(Dealer.objects.all())
        car_makes = list(CarMake.objects.all())
        
        if dealers and car_makes:
            for i in range(20):  # Create 20 sample reviews
                dealer = random.choice(dealers)
                car_make = random.choice(car_makes)
                car_models = list(CarModel.objects.filter(car_make=car_make))
                car_model = random.choice(car_models) if car_models else None
                
                review_text = random.choice(sample_reviews)
                sentiment = "positive" if "excellent" in review_text.lower() or "outstanding" in review_text.lower() or "amazing" in review_text.lower() else \
                           "negative" if "could be better" in review_text.lower() else "neutral"
                
                review, created = Review.objects.get_or_create(
                    dealer=dealer,
                    name=f"Customer {i+1}",
                    review=review_text,
                    defaults={
                        'purchase': random.choice([True, False]),
                        'purchase_date': date.today() - timedelta(days=random.randint(1, 365)),
                        'car_make': car_make.name,
                        'car_model': car_model.name if car_model else None,
                        'car_year': random.randint(2020, 2023),
                        'sentiment': sentiment
                    }
                )
                
                if created:
                    created_reviews += 1

        self.stdout.write("\n🎯 SUMMARY")
        self.stdout.write(f"Created {created_makes} new car makes")
        self.stdout.write(f"Created {created_models} new car models")
        self.stdout.write(f"Created {created_dealers} new dealers")
        self.stdout.write(f"Created {created_reviews} new reviews")
        self.stdout.write(f"Total makes: {CarMake.objects.count()}")
        self.stdout.write(f"Total models: {CarModel.objects.count()}")
        self.stdout.write(f"Total dealers: {Dealer.objects.count()}")
        self.stdout.write(f"Total reviews: {Review.objects.count()}")
        self.stdout.write(
            self.style.SUCCESS('✅ Database populated successfully!')
        )
