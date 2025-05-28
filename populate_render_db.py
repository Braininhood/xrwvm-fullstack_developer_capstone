#!/usr/bin/env python3
"""
Script to populate Render database with sample data
"""
import os
import sys
import django

# Add the server directory to Python path
sys.path.append('server')

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'djangoproj.production_settings')

# Setup Django
django.setup()

from server.djangoapp.models import CarMake, CarModel  # noqa: E402


def populate_database():
    """Populate the database with sample car data"""
    print("🚗 POPULATING RENDER DATABASE")
    print("=" * 40)

    # Sample car makes and models
    car_data = [
        {
            'make': 'Toyota',
            'models': ['Camry', 'Corolla', 'Prius', 'RAV4', 'Highlander']
        },
        {
            'make': 'Honda',
            'models': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit']
        },
        {
            'make': 'Ford',
            'models': ['F-150', 'Mustang', 'Explorer', 'Escape', 'Focus']
        },
        {
            'make': 'BMW',
            'models': ['3 Series', '5 Series', 'X3', 'X5', 'i3']
        },
        {
            'make': 'Mercedes-Benz',
            'models': ['C-Class', 'E-Class', 'GLC', 'GLE', 'A-Class']
        }
    ]

    created_makes = 0
    created_models = 0

    for make_data in car_data:
        # Create or get car make
        car_make, created = CarMake.objects.get_or_create(
            name=make_data['make'],
            defaults={'description': f'{make_data["make"]} vehicles'}
        )

        if created:
            created_makes += 1
            print(f"✅ Created car make: {car_make.name}")
        else:
            print(f"📋 Car make exists: {car_make.name}")

        # Create car models
        for model_name in make_data['models']:
            car_model, created = CarModel.objects.get_or_create(
                name=model_name,
                car_make=car_make,
                defaults={
                    'type': 'Sedan',  # Default type
                    'year': 2023,     # Default year
                    'dealer_id': 1    # Default dealer
                }
            )

            if created:
                created_models += 1
                print(f"  ✅ Created model: {model_name}")

    print("\n🎯 SUMMARY")
    print(f"Created {created_makes} new car makes")
    print(f"Created {created_models} new car models")
    print(f"Total makes: {CarMake.objects.count()}")
    print(f"Total models: {CarModel.objects.count()}")


if __name__ == "__main__":
    populate_database()
