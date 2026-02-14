#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render Health Check Diagnostika
"""
import requests
import json

# Mumkin bo'lgan Render URLs
POSSIBLE_URLS = [
    "https://yuklauz7-bot.onrender.com",
    "https://yuklauz7bot.onrender.com",
    "https://yuklauz-bot.onrender.com",
]

def check_url(base_url):
    """URL ni tekshirish"""
    print(f"\n[Tekshirilmoqda] {base_url}")
    print("=" * 60)
    
    # 1. Health check endpoint
    health_url = f"{base_url}/health"
    print(f"\n1. Health Check: {health_url}")
    try:
        response = requests.get(health_url, timeout=10)
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print(f"   [OK] Health check ishlayapti!")
            try:
                data = response.json()
                print(f"   Response: {json.dumps(data, indent=2)}")
            except:
                print(f"   Response: {response.text[:200]}")
            return True
        else:
            print(f"   [ERROR] Status code: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
    except requests.exceptions.Timeout:
        print(f"   [ERROR] Timeout - server javob bermayapti")
    except requests.exceptions.ConnectionError:
        print(f"   [ERROR] Connection error - URL mavjud emas")
    except Exception as e:
        print(f"   [ERROR] {e}")
    
    # 2. Root endpoint
    print(f"\n2. Root: {base_url}")
    try:
        response = requests.get(base_url, timeout=10)
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
    except Exception as e:
        print(f"   [ERROR] {e}")
    
    return False

def main():
    print("=" * 60)
    print("RENDER HEALTH CHECK DIAGNOSTIKA")
    print("=" * 60)
    
    working_url = None
    
    for url in POSSIBLE_URLS:
        if check_url(url):
            working_url = url
            break
    
    print("\n" + "=" * 60)
    print("NATIJA")
    print("=" * 60)
    
    if working_url:
        print(f"\n[SUCCESS] Ishlayotgan URL:")
        print(f"   {working_url}/health")
        print(f"\nUptimeRobot ga quyidagini kiriting:")
        print(f"   {working_url}/health")
    else:
        print(f"\n[WARNING] Hech qaysi URL ishlamadi!")
        print(f"\nEhtimoliy sabablar:")
        print(f"   1. Service nomi boshqa")
        print(f"   2. Bot hali to'liq deploy bo'lmagan")
        print(f"   3. Health check endpoint xato")
        print(f"\nRender dashboard dan:")
        print(f"   1. Service URL ni toping")
        print(f"   2. Logs ni tekshiring")

if __name__ == "__main__":
    main()
