#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # exit on error

echo "🚀 Starting Render build process..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
cd server
pip install -r requirements.txt

# Build React frontend
echo "⚛️ Building React frontend..."
cd frontend
npm ci --only=production
npm run build

# Go back to server directory
cd ..

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --settings=djangoproj.production_settings

# Run migrations with verbose output
echo "🗄️ Running database migrations..."
echo "📋 Checking migration status..."
python manage.py showmigrations --settings=djangoproj.production_settings

echo "🔄 Applying migrations..."
python manage.py migrate --verbosity=2 --settings=djangoproj.production_settings

# Check database setup
echo "🔍 Verifying database setup..."
python manage.py check_db --settings=djangoproj.production_settings

# Create superuser if it doesn't exist
echo "👤 Creating superuser..."
python manage.py shell --settings=djangoproj.production_settings <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created')
else:
    print('Superuser already exists')
EOF

# Populate database with sample data
echo "🚗 Populating database with sample data..."
python manage.py populate_db --settings=djangoproj.production_settings

# Populate dealers and reviews
echo "🏪 Populating dealers and reviews..."
python manage.py populate_dealers --settings=djangoproj.production_settings

# Final database check
echo "🔍 Final database verification..."
python manage.py check_db --settings=djangoproj.production_settings

echo "✅ Build completed successfully!" 