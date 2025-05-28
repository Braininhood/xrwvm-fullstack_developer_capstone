#!/usr/bin/env python3
"""
Test script to verify PostReview functionality on Render deployment
"""

import requests
import json
import time

# Render deployment URL
BASE_URL = "https://xrwvm-fullstack-developer-capstone-4q3s.onrender.com"

def test_api_endpoints():
    """Test all API endpoints that PostReview depends on"""
    print("🔍 Testing API endpoints for PostReview functionality...")
    
    # Test 1: Check if Django API is responding
    try:
        response = requests.get(f"{BASE_URL}/djangoapp/get_dealers", timeout=10)
        print(f"✅ Django API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Dealers available: {len(data.get('dealers', []))}")
    except Exception as e:
        print(f"❌ Django API Error: {e}")
        return False
    
    # Test 2: Check specific dealer endpoint
    try:
        response = requests.get(f"{BASE_URL}/djangoapp/dealer/1", timeout=10)
        print(f"✅ Dealer Details Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            dealer = data.get('dealer', {})
            print(f"   Dealer: {dealer.get('full_name', 'Unknown')}")
    except Exception as e:
        print(f"❌ Dealer Details Error: {e}")
    
    # Test 3: Check cars endpoint
    try:
        response = requests.get(f"{BASE_URL}/djangoapp/get_cars", timeout=10)
        print(f"✅ Cars API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Car models available: {len(data.get('CarModels', []))}")
    except Exception as e:
        print(f"❌ Cars API Error: {e}")
    
    # Test 4: Test registration endpoint (needed for authentication)
    try:
        test_user_data = {
            "userName": f"testuser_{int(time.time())}",
            "password": "testpass123",
            "firstName": "Test",
            "lastName": "User",
            "email": f"test_{int(time.time())}@example.com"
        }
        
        response = requests.post(
            f"{BASE_URL}/djangoapp/register",
            json=test_user_data,
            timeout=10
        )
        print(f"✅ Registration Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'Authenticated':
                print("   ✅ User registration and authentication working")
                
                # Test 5: Try to post a review with the authenticated session
                session = requests.Session()
                
                # First register/login
                login_response = session.post(
                    f"{BASE_URL}/djangoapp/register",
                    json=test_user_data,
                    timeout=10
                )
                
                if login_response.status_code == 200:
                    # Now try to post a review
                    review_data = {
                        "name": "Test User",
                        "dealership": "1",
                        "review": "Test review for API functionality",
                        "purchase": True,
                        "purchase_date": "2023-12-01",
                        "car_make": "Toyota",
                        "car_model": "Camry",
                        "car_year": "2023"
                    }
                    
                    review_response = session.post(
                        f"{BASE_URL}/djangoapp/add_review",
                        json=review_data,
                        timeout=10
                    )
                    print(f"✅ Add Review Status: {review_response.status_code}")
                    
                    if review_response.status_code == 200:
                        print("   ✅ Review posting is working correctly!")
                        return True
                    else:
                        print(f"   ❌ Review posting failed: {review_response.text}")
                        return False
            else:
                print(f"   ❌ Authentication failed: {data}")
                return False
    except Exception as e:
        print(f"❌ Registration/Review Test Error: {e}")
        return False

def test_frontend_config():
    """Test if frontend is properly configured"""
    print("\n🔍 Testing frontend configuration...")
    
    try:
        # Check if the main page loads
        response = requests.get(BASE_URL, timeout=10)
        print(f"✅ Frontend Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            if "Dealership Management System" in content:
                print("   ✅ Frontend is loading correctly")
                return True
            else:
                print("   ❌ Frontend content not found")
                return False
    except Exception as e:
        print(f"❌ Frontend Error: {e}")
        return False

def main():
    print("🚀 Testing PostReview functionality on Render deployment")
    print(f"🌐 URL: {BASE_URL}")
    print("=" * 60)
    
    # Test frontend
    frontend_ok = test_frontend_config()
    
    # Test API endpoints
    api_ok = test_api_endpoints()
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print(f"   Frontend: {'✅ Working' if frontend_ok else '❌ Issues'}")
    print(f"   API & PostReview: {'✅ Working' if api_ok else '❌ Issues'}")
    
    if frontend_ok and api_ok:
        print("\n🎉 All tests passed! PostReview should be working on Render.")
        print("\n📝 To test manually:")
        print(f"   1. Go to {BASE_URL}")
        print("   2. Register a new account")
        print("   3. Browse dealers and click 'Post Review' icon")
        print("   4. Fill out the review form and submit")
    else:
        print("\n⚠️  Some issues detected. Check the logs above for details.")
        print("\n🔧 Common fixes:")
        print("   - Wait a few minutes for Render deployment to complete")
        print("   - Check if all environment variables are set correctly")
        print("   - Verify that the build completed successfully")

if __name__ == "__main__":
    main() 