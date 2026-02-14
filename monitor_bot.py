#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot Monitoring Script - 24/7 ishlashni kuzatish
"""
import os
import time
import psutil
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN", "8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s")
HEALTH_CHECK_URL = os.getenv("HEALTH_CHECK_URL", "http://localhost:8080/health")

def check_memory():
    """Xotira ishlatilishini tekshirish"""
    try:
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        memory_mb = memory_info.rss / 1024 / 1024
        
        print(f"💾 Memory Usage: {memory_mb:.2f} MB")
        
        if memory_mb > 450:
            print(f"⚠️  WARNING: Memory usage yuqori! (threshold: 450MB)")
            return False
        return True
    except Exception as e:
        print(f"❌ Memory check xatolik: {e}")
        return False

def check_bot_api():
    """Bot API javob berishini tekshirish"""
    try:
        response = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/getMe",
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("ok"):
                print(f"✅ Bot API: Online (@{data['result']['username']})")
                return True
        print(f"❌ Bot API: Error (status: {response.status_code})")
        return False
    except Exception as e:
        print(f"❌ Bot API check xatolik: {e}")
        return False

def check_health_endpoint():
    """Health check endpoint ni tekshirish"""
    try:
        response = requests.get(HEALTH_CHECK_URL, timeout=5)
        if response.status_code == 200:
            print(f"✅ Health Endpoint: OK")
            return True
        print(f"❌ Health Endpoint: Error (status: {response.status_code})")
        return False
    except Exception as e:
        print(f"❌ Health Endpoint xatolik: {e}")
        return False

def check_disk_space():
    """Disk bo'sh joyini tekshirish"""
    try:
        disk = psutil.disk_usage('.')
        free_gb = disk.free / (1024**3)
        total_gb = disk.total / (1024**3)
        used_percent = disk.percent
        
        print(f"💿 Disk: {free_gb:.2f}GB / {total_gb:.2f}GB free ({used_percent}% used)")
        
        if used_percent > 90:
            print(f"⚠️  WARNING: Disk to'lib ketmoqda!")
            return False
        return True
    except Exception as e:
        print(f"❌ Disk check xatolik: {e}")
        return False

def check_log_files():
    """Log fayllarni tekshirish"""
    try:
        if os.path.exists("bot.log"):
            size_mb = os.path.getsize("bot.log") / (1024**2)
            print(f"📄 Log fayl: {size_mb:.2f} MB")
            
            if size_mb > 20:
                print(f"⚠️  WARNING: Log fayl katta (>20MB)")
                return False
        return True
    except Exception as e:
        print(f"❌ Log check xatolik: {e}")
        return False

def main():
    """Barcha tekshiruvlarni amalga oshirish"""
    print("=" * 60)
    print(f"BOT MONITORING - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    checks = {
        "Memory": check_memory(),
        "Bot API": check_bot_api(),
        "Health Endpoint": check_health_endpoint(),
        "Disk Space": check_disk_space(),
        "Log Files": check_log_files(),
    }
    
    print("\n" + "=" * 60)
    print("NATIJA:")
    print("=" * 60)
    
    passed = sum(checks.values())
    total = len(checks)
    
    print(f"\n✅ Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 Barcha tekshiruvlar muvaffaqiyatli!")
        return 0
    else:
        print("⚠️  Ba'zi tekshiruvlar muvaffaqiyatsiz!")
        return 1

if __name__ == "__main__":
    exit(main())
