#!/usr/bin/env python3
"""
Comprehensive test script for both local and Render deployments
"""
import requests
import json

LOCAL_URL = "http://localhost:8000"
RENDER_URL = "https://xrwvm-fullstack-developer-capstone-4q3s.onrender.com"


def test_endpoint(url, endpoint, name):
    """Test a single endpoint and return status"""
    try:
        response = requests.get(f"{url}{endpoint}", timeout=30)
        if response.status_code == 200:
            print(f"✅ {name}: {response.status_code}")
            return True, response
        else:
            print(f"❌ {name}: {response.status_code}")
            return False, response
    except Exception as e:
        print(f"❌ {name}: {e}")
        return False, None


def test_deployment(url, name):
    """Test a complete deployment"""
    print(f"\n🚀 TESTING {name.upper()}")
    print("=" * 50)
    
    # Test Django API
    print(f"\n🔍 Testing Django API at {url}...")
    success, response = test_endpoint(url, "/djangoapp/get_dealers/", "Get Dealers API")
    if success and response:
        try:
            data = response.json()
            if "dealers" in data and data["dealers"]:
                print(f"   📊 Found {len(data['dealers'])} dealers")
            else:
                print("   ⚠️  No dealers data found")
        except:
            print("   ⚠️  Invalid JSON response")
    
    # Test frontend routes
    print(f"\n🔍 Testing Frontend Routes...")
    routes = ["/", "/login/", "/register/", "/dealers/"]
    for route in routes:
        success, response = test_endpoint(url, route, f"Route {route}")
        if success and response:
            if "<!doctype html>" in response.text.lower():
                print(f"   📄 HTML template found for {route}")
            else:
                print(f"   ❌ No HTML template for {route}")
    
    # Test static files (only for Render)
    if "render" in url:
        print(f"\n🔍 Testing Static Files...")
        static_files = [
            "/static/css/main.17970e7d.css",
            "/static/js/main.8694aba5.js",
            "/favicon.ico"
        ]
        for static_file in static_files:
            test_endpoint(url, static_file, f"Static {static_file}")


def main():
    print("🌐 COMPREHENSIVE DEPLOYMENT TEST")
    print("=" * 60)
    
    # Test local deployment
    test_deployment(LOCAL_URL, "Local Docker")
    
    # Test Render deployment
    test_deployment(RENDER_URL, "Render Cloud")
    
    print("\n🎯 SUMMARY")
    print("-" * 30)
    print("Local Docker: Full-stack with all microservices")
    print("Render Cloud: Django + React frontend only")
    print(f"\n🌐 Local: {LOCAL_URL}")
    print(f"🌐 Render: {RENDER_URL}")


if __name__ == "__main__":
    main() 