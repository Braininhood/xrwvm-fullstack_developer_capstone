#!/usr/bin/env python3
"""
Test script to demonstrate the complete solution.
This script will:
1. Check if services are running
2. Start services if needed
3. Run Django tests
4. Show the results
"""

import subprocess
import sys
import time
import requests
from pathlib import Path

def check_service(url, name):
    """Check if a service is running"""
    try:
        response = requests.get(url, timeout=2)
        print(f"✅ {name} is running at {url}")
        return True
    except requests.exceptions.RequestException:
        print(f"❌ {name} is not running at {url}")
        return False

def run_django_tests():
    """Run Django tests and show results"""
    print("\n🧪 Running Django tests...")
    print("=" * 50)
    
    try:
        result = subprocess.run([
            sys.executable, "manage.py", "test", "djangoapp", "--verbosity=2"
        ], capture_output=True, text=True, cwd=Path(__file__).parent)
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print(f"❌ Tests failed with exit code {result.returncode}")
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

def main():
    """Main test function"""
    print("🚗 Django Backend Test Suite")
    print("=" * 40)
    
    # Check if services are running
    print("\n🔍 Checking microservices...")
    dealer_running = check_service("http://localhost:3030", "Dealer Service")
    sentiment_running = check_service("http://localhost:5050", "Sentiment Analyzer")
    
    if not dealer_running or not sentiment_running:
        print("\n⚠️  Some services are not running.")
        print("💡 To start services, run:")
        print("   Windows: start_services.bat")
        print("   Cross-platform: python start_services.py")
        print("\n📝 Note: Tests will still pass with fallback data")
    
    # Run tests regardless
    success = run_django_tests()
    
    print("\n📊 Summary:")
    print(f"  - Dealer Service: {'✅' if dealer_running else '❌'}")
    print(f"  - Sentiment Analyzer: {'✅' if sentiment_running else '❌'}")
    print(f"  - Django Tests: {'✅' if success else '❌'}")
    
    if success:
        print("\n🎉 Django backend is working correctly!")
        if not dealer_running or not sentiment_running:
            print("💡 For full functionality, start the microservices")
    else:
        print("\n❌ There are issues with the Django backend")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main()) 