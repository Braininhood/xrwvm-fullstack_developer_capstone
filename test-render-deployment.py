#!/usr/bin/env python3
"""
Test script to verify Render deployment is working correctly
"""
import requests

RENDER_URL = "https://xrwvm-fullstack-developer-capstone-4q3s.onrender.com"


def test_render_deployment():
    print("🚀 TESTING RENDER DEPLOYMENT")
    print("=" * 50)

    # Test 1: Check if the main site is accessible
    print("\n🔍 Testing main site accessibility...")
    try:
        response = requests.get(RENDER_URL, timeout=30)
        if response.status_code == 200:
            print(f"✅ Main site accessible: {response.status_code}")
            if "<!doctype html>" in response.text.lower():
                print("✅ HTML content detected")
            else:
                print("❌ No HTML content found")
        else:
            print(f"❌ Main site error: {response.status_code}")
    except Exception as e:
        print(f"❌ Main site failed: {e}")

    # Test 2: Check Django API endpoints
    print("\n🔍 Testing Django API endpoints...")
    api_endpoints = [
        "/djangoapp/get_dealers/",
        "/djangoapp/get_cars/",
    ]

    for endpoint in api_endpoints:
        try:
            response = requests.get(f"{RENDER_URL}{endpoint}", timeout=30)
            if response.status_code == 200:
                print(f"✅ {endpoint}: {response.status_code}")
                if endpoint == "/djangoapp/get_dealers/":
                    data = response.json()
                    if "dealers" in data:
                        print(f"   📊 Found {len(data['dealers'])} dealers")
            else:
                print(f"❌ {endpoint}: {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint}: {e}")

    # Test 3: Check frontend routes
    print("\n🔍 Testing frontend routes...")
    frontend_routes = [
        "/login/",
        "/register/",
        "/dealers/",
    ]

    for route in frontend_routes:
        try:
            response = requests.get(f"{RENDER_URL}{route}", timeout=30)
            if response.status_code == 200:
                print(f"✅ {route}: {response.status_code}")
                if "<!doctype html>" in response.text.lower():
                    print("   📄 HTML template found")
                else:
                    print("   ❌ No HTML template")
            else:
                print(f"❌ {route}: {response.status_code}")
        except Exception as e:
            print(f"❌ {route}: {e}")

    # Test 4: Check static files
    print("\n🔍 Testing static files...")
    static_files = [
        "/static/css/main.17970e7d.css",
        "/static/js/main.8694aba5.js",
        "/favicon.ico",
    ]

    for static_file in static_files:
        try:
            response = requests.get(f"{RENDER_URL}{static_file}", timeout=30)
            if response.status_code == 200:
                print(f"✅ {static_file}: {response.status_code}")
            else:
                print(f"❌ {static_file}: {response.status_code}")
        except Exception as e:
            print(f"❌ {static_file}: {e}")

    print("\n🎯 DEPLOYMENT TEST SUMMARY")
    print("-" * 30)
    print("If you see ✅ for frontend routes and static files,")
    print("your full-stack application is working correctly!")
    print(f"\n🌐 Visit your app: {RENDER_URL}")


if __name__ == "__main__":
    test_render_deployment()
