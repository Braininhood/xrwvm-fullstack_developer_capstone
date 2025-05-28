from django.core.management.base import BaseCommand
from djangoapp.models import Dealer, Review
from datetime import date


class Command(BaseCommand):
    help = 'Populate database with sample dealers and reviews'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample dealers...')
        
        # Clear existing data
        Dealer.objects.all().delete()
        Review.objects.all().delete()
        
        # Sample dealers data
        dealers_data = [
            {
                "full_name": "Borcelle Dealership",
                "city": "Fremont",
                "state": "California",
                "address": "36 Fremont Blvd",
                "zip_code": "94537",
                "lat": 37.5485,
                "long": -121.9886,
                "short_name": "Borcelle",
                "st": "CA"
            },
            {
                "full_name": "Hayward Ford",
                "city": "Hayward",
                "state": "California", 
                "address": "25101 Mission Blvd",
                "zip_code": "94544",
                "lat": 37.6688,
                "long": -122.0808,
                "short_name": "Hayward Ford",
                "st": "CA"
            },
            {
                "full_name": "Daly City Toyota",
                "city": "Daly City",
                "state": "California",
                "address": "111 Hickey Blvd",
                "zip_code": "94015",
                "lat": 37.7058,
                "long": -122.4594,
                "short_name": "Daly Toyota",
                "st": "CA"
            },
            {
                "full_name": "Golden Gate Audi",
                "city": "Fremont",
                "state": "California",
                "address": "5200 Auto Mall Pkwy",
                "zip_code": "94538",
                "lat": 37.4969,
                "long": -121.9356,
                "short_name": "GG Audi",
                "st": "CA"
            },
            {
                "full_name": "Bay Area BMW",
                "city": "San Jose",
                "state": "California",
                "address": "1350 Automation Pkwy",
                "zip_code": "95131",
                "lat": 37.4419,
                "long": -121.9358,
                "short_name": "BA BMW",
                "st": "CA"
            },
            {
                "full_name": "Elite Motors",
                "city": "Austin",
                "state": "Texas",
                "address": "2500 S IH 35",
                "zip_code": "78741",
                "lat": 30.2672,
                "long": -97.7431,
                "short_name": "Elite Motors",
                "st": "TX"
            },
            {
                "full_name": "Lone Star Chevrolet",
                "city": "Houston",
                "state": "Texas",
                "address": "7500 Katy Fwy",
                "zip_code": "77024",
                "lat": 29.7604,
                "long": -95.3698,
                "short_name": "Lone Star",
                "st": "TX"
            },
            {
                "full_name": "Empire State Motors",
                "city": "New York",
                "state": "New York",
                "address": "123 Broadway",
                "zip_code": "10001",
                "lat": 40.7128,
                "long": -74.0060,
                "short_name": "Empire Motors",
                "st": "NY"
            },
            {
                "full_name": "Sunshine Honda",
                "city": "Miami",
                "state": "Florida",
                "address": "8900 Biscayne Blvd",
                "zip_code": "33138",
                "lat": 25.7617,
                "long": -80.1918,
                "short_name": "Sunshine Honda",
                "st": "FL"
            },
            {
                "full_name": "Mile High Subaru",
                "city": "Denver",
                "state": "Colorado",
                "address": "1400 S Colorado Blvd",
                "zip_code": "80222",
                "lat": 39.7392,
                "long": -104.9903,
                "short_name": "Mile High",
                "st": "CO"
            }
        ]
        
        # Create dealers
        created_dealers = []
        for dealer_data in dealers_data:
            dealer = Dealer.objects.create(**dealer_data)
            created_dealers.append(dealer)
            self.stdout.write(f'Created dealer: {dealer.full_name}')
        
        # Create sample reviews
        sample_reviews = [
            {
                "dealer": created_dealers[0],
                "name": "John Smith",
                "review": "Great service and friendly staff. Highly recommend!",
                "purchase_date": date(2023, 10, 15),
                "car_make": "Toyota",
                "car_model": "Camry",
                "car_year": 2023,
                "sentiment": "positive"
            },
            {
                "dealer": created_dealers[0],
                "name": "Sarah Johnson",
                "review": "Good experience overall, but could improve wait times.",
                "purchase_date": date(2023, 9, 20),
                "car_make": "Honda",
                "car_model": "Civic",
                "car_year": 2022,
                "sentiment": "neutral"
            },
            {
                "dealer": created_dealers[1],
                "name": "Mike Wilson",
                "review": "Excellent customer service and fair pricing.",
                "purchase_date": date(2023, 11, 5),
                "car_make": "Ford",
                "car_model": "F-150",
                "car_year": 2023,
                "sentiment": "positive"
            },
            {
                "dealer": created_dealers[2],
                "name": "Lisa Brown",
                "review": "Very satisfied with my purchase. Professional team.",
                "purchase_date": date(2023, 8, 12),
                "car_make": "Toyota",
                "car_model": "RAV4",
                "car_year": 2023,
                "sentiment": "positive"
            }
        ]
        
        for review_data in sample_reviews:
            Review.objects.create(**review_data)
            dealer_name = review_data['dealer'].full_name
            reviewer_name = review_data['name']
            self.stdout.write(f'Created review by {reviewer_name} '
                              f'for {dealer_name}')
        
        dealer_count = len(created_dealers)
        review_count = len(sample_reviews)
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated database with {dealer_count} '
                f'dealers and {review_count} reviews'
            )
        ) 