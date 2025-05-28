from django.core.management.base import BaseCommand
from djangoapp.models import CarMake, CarModel


class Command(BaseCommand):
    help = 'Populate database with sample car data'

    def handle(self, *args, **options):
        self.stdout.write("🚗 POPULATING DATABASE")
        self.stdout.write("=" * 40)

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
                self.stdout.write(f"✅ Created car make: {car_make.name}")
            else:
                self.stdout.write(f"📋 Car make exists: {car_make.name}")

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
                    self.stdout.write(f"  ✅ Created model: {model_name}")

        self.stdout.write("\n🎯 SUMMARY")
        self.stdout.write(f"Created {created_makes} new car makes")
        self.stdout.write(f"Created {created_models} new car models")
        self.stdout.write(f"Total makes: {CarMake.objects.count()}")
        self.stdout.write(f"Total models: {CarModel.objects.count()}")
        self.stdout.write(
            self.style.SUCCESS('✅ Database populated successfully!')
        )
