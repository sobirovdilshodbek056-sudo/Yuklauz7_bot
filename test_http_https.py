#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UptimeRobot Test - HTTP vs HTTPS
"""
import requests

urls = [
    "http://yuklauz7-bot.onrender.com/health",   # HTTP (noto'g'ri)
    "https://yuklauz7-bot.onrender.com/health",  # HTTPS (to'g'ri)
]

print("=" * 60)
print("HTTP vs HTTPS TEST")
print("=" * 60)

for url in urls:
    print(f"\n[TEST] {url}")
    print("-" * 60)
    try:
        response = requests.get(url, timeout=10, allow_redirects=False)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        if response.status_code == 200:
            print("[OK] Ishlayapti!")
        elif response.status_code == 301 or response.status_code == 302:
            print(f"[REDIRECT] {response.headers.get('Location')}")
        else:
            print(f"[ERROR] Xatolik: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] {e}")

print("\n" + "=" * 60)
print("XULOSA")
print("=" * 60)
print("UptimeRobot ga HTTPS URL kiriting:")
print("https://yuklauz7-bot.onrender.com/health")
