#!/usr/bin/env python3
# examples/webapp_demo.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""
Demo script showing the complete hworld stack working.
Run with both server and webapp running.
"""

import requests
import time


def Main():
    """Test the webapp and server integration"""

    print("=" * 60)
    print("Hworld WebApp Integration Test")
    print("=" * 60)
    print()

    # Test health endpoint
    print("1. Testing health endpoint...")
    try:
        response = requests.get("http://localhost:8080/health")
        print(f"   Status: {response.json()}")
        print("   ✓ Health check passed")
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return 1

    print()

    # Test login
    print("2. Testing login via webapp...")
    try:
        response = requests.post(
            "http://localhost:8080/api/login",
            json={"username": "demouser", "password": "demopass"}
        )
        data = response.json()
        if data.get("success"):
            print(f"   ✓ Login successful: {data.get('username')}")
        else:
            print(f"   ✗ Login failed: {data}")
            return 1
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return 1

    print()

    # Test server ping
    print("3. Testing server ping...")
    try:
        response = requests.post("http://localhost:8080/api/test")
        data = response.json()
        if data.get("success"):
            print(f"   ✓ Server ping successful: {data.get('pong')}")
        else:
            print(f"   ✗ Ping failed: {data}")
            return 1
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return 1

    print()
    print("=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
    print()
    print("Visit http://localhost:8080 in your browser to use the")
    print("web interface.")
    print()

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(Main())
