from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djangoapp.models import Dealer, Review, CarMake, CarModel
from django.db import connection


class Command(BaseCommand):
    help = 'Check database setup and table existence'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Checking database setup...')

        # Check database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                self.stdout.write('✅ Database connection successful')
        except Exception as e:
            self.stdout.write(f'❌ Database connection failed: {e}')
            return

        # Check if tables exist
        tables_to_check = [
            ('auth_user', User),
            ('djangoapp_dealer', Dealer),
            ('djangoapp_review', Review),
            ('djangoapp_carmake', CarMake),
            ('djangoapp_carmodel', CarModel),
        ]

        for table_name, model in tables_to_check:
            try:
                count = model.objects.count()
                self.stdout.write(f'✅ {table_name}: {count} records')
            except Exception as e:
                self.stdout.write(f'❌ {table_name}: {e}')

        # List all tables in database
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' ORDER BY name;
                """)
                tables = cursor.fetchall()
                self.stdout.write('📋 All tables in database:')
                for table in tables:
                    self.stdout.write(f'   - {table[0]}')
        except Exception as e:
            self.stdout.write(f'❌ Could not list tables: {e}')

        self.stdout.write('🏁 Database check completed') 