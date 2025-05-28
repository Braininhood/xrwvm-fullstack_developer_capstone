#!/usr/bin/env python3
"""
Test script to verify Render deployment is working with Django-only solution
"""

import requests
import json
import time

BASE_URL = "https://xrwvm-fullstack-developer-capstone-4q3s.onrender.com"

def test_dealers_api():
    """Test the dealers API endpoint"""
    print("🔍 Testing Dealers API...")
    try:
        response = requests.get(f"{BASE_URL}/djangoapp/get_dealers", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 200 and data.get('dealers'):
                dealers = data['dealers']
                print(f"   ✅ Found {len(dealers)} dealers")
                
                # Check if dealers have the correct Django format (no _id field)
                if dealers and 'id' in dealers[0] and '_id' not in dealers[0]:
                    print("   ✅ Dealers using Django model format")
                    return True
                else:
                    print("   ❌ Dealers still using Node.js format")
                    return False
            else:
                print(f"   ❌ API returned: {data}")
                return False
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_dealer_details():
    """Test dealer details endpoint"""
    print("\n🔍 Testing Dealer Details API...")
    try:
        response = requests.get(f"{BASE_URL}/djangoapp/dealer/1", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 200 and data.get('dealer'):
                dealer = data['dealer']
                print(f"   ✅ Dealer: {dealer.get('full_name', 'Unknown')}")
                return True
            else:
                print(f"   ❌ API returned: {data}")
                return False
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_cars_api():
    """Test cars API endpoint"""
    print("\n🔍 Testing Cars API...")
    try:
        response = requests.get(f"{BASE_URL}/djangoapp/get_cars", timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('CarModels'):
                cars = data['CarModels']
                print(f"   ✅ Found {len(cars)} car models")
                return True
            else:
                print(f"   ❌ No car models found: {data}")
                return False
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_registration():
    """Test user registration"""
    print("\n🔍 Testing User Registration...")
    try:
        test_user = {
            "userName": f"testuser_{int(time.time())}",
            "password": "testpass123",
            "firstName": "Test",
            "lastName": "User",
            "email": f"test_{int(time.time())}@example.com"
        }
        
        response = requests.post(
            f"{BASE_URL}/djangoapp/register",
            json=test_user,
            timeout=10
        )
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'Authenticated':
                print("   ✅ Registration and authentication working")
                return True
            else:
                print(f"   ❌ Registration failed: {data}")
                return False
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("🚀 Testing Render Deployment with Django-only Solution")
    print(f"🌐 URL: {BASE_URL}")
    print("=" * 60)
    
    # Wait a moment for deployment to be ready
    print("⏳ Waiting for deployment to be ready...")
    time.sleep(5)
    
    # Run tests
    dealers_ok = test_dealers_api()
    details_ok = test_dealer_details()
    cars_ok = test_cars_api()
    registration_ok = test_registration()
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print(f"   Dealers API: {'✅ Working' if dealers_ok else '❌ Issues'}")
    print(f"   Dealer Details: {'✅ Working' if details_ok else '❌ Issues'}")
    print(f"   Cars API: {'✅ Working' if cars_ok else '❌ Issues'}")
    print(f"   Registration: {'✅ Working' if registration_ok else '❌ Issues'}")
    
    all_working = dealers_ok and details_ok and cars_ok and registration_ok
    
    if all_working:
        print("\n🎉 All APIs working! PostReview should now work correctly.")
        print("\n📝 To test PostReview:")
        print(f"   1. Go to {BASE_URL}")
        print("   2. Register a new account")
        print("   3. Browse dealers (should show 10 dealers)")
        print("   4. Click on any dealer")
        print("   5. Click 'Post Review' icon")
        print("   6. Fill out and submit the review form")
    else:
        print("\n⚠️  Some issues detected. The deployment may still be in progress.")
        print("   Wait 5-10 minutes and run this test again.")

if __name__ == "__main__":
    main() 