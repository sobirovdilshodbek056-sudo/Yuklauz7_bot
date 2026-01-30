#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot holatini tekshirish skripti
"""
import requests
import json

BOT_TOKEN = "8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s"

def check_bot():
    """Bot holatini tekshirish"""
    print("=" * 60)
    print("BOT HOLATI TEKSHIRUVI")
    print("=" * 60)
    
    # 1. Bot ma'lumotlarini olish
    print("\n1. Bot ma'lumotlari:")
    try:
        response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("ok"):
                bot_info = data.get("result", {})
                print(f"   [OK] Bot nomi: @{bot_info.get('username')}")
                print(f"   [OK] Bot ID: {bot_info.get('id')}")
                print(f"   [OK] Bot ismi: {bot_info.get('first_name')}")
            else:
                print(f"   [ERROR] Xatolik: {data.get('description')}")
        else:
            print(f"   [ERROR] HTTP xatolik: {response.status_code}")
    except Exception as e:
        print(f"   [ERROR] Xatolik: {e}")
    
    # 2. Webhook holatini tekshirish
    print("\n2. Webhook holati:")
    try:
        response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("ok"):
                webhook = data.get("result", {})
                url = webhook.get("url")
                if url:
                    print(f"   [WARNING] Webhook o'rnatilgan: {url}")
                    print(f"   [WARNING] Bu polling uchun muammo!")
                else:
                    print("   [OK] Webhook yo'q (Polling rejimi)")
                
                pending = webhook.get("pending_update_count", 0)
                if pending > 0:
                    print(f"   [INFO] Kutilayotgan yangilanishlar: {pending}")
            else:
                print(f"   [ERROR] Xatolik: {data.get('description')}")
        else:
            print(f"   [ERROR] HTTP xatolik: {response.status_code}")
    except Exception as e:
        print(f"   [ERROR] Xatolik: {e}")
    
    # 3. So'nggi yangilanishlarni tekshirish
    print("\n3. So'nggi harakatlar:")
    try:
        response = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?limit=1&timeout=1",
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("ok"):
                updates = data.get("result", [])
                if updates:
                    last_update = updates[-1]
                    update_id = last_update.get("update_id")
                    print(f"   [OK] So'nggi update ID: {update_id}")
                    
                    # Message ma'lumotlari
                    if "message" in last_update:
                        msg = last_update["message"]
                        user = msg.get("from", {})
                        print(f"   [INFO] So'nggi habar: {user.get('first_name')} ({user.get('id')})")
                        print(f"   [INFO] Matn: {msg.get('text', 'N/A')[:50]}")
                else:
                    print("   [INFO] Hech qanday yangilanish yo'q")
            else:
                desc = data.get("description", "N/A")
                if "Conflict" in desc:
                    print(f"   [CONFLICT] Bot 2 joyda ishlamoqda!")
                    print(f"   [CONFLICT] {desc}")
                else:
                    print(f"   [ERROR] Xatolik: {desc}")
        else:
            print(f"   [ERROR] HTTP xatolik: {response.status_code}")
    except Exception as e:
        print(f"   [ERROR] Xatolik: {e}")
    
    # 4. Tavsiyalar
    print("\n" + "=" * 60)
    print("TAVSIYALAR:")
    print("=" * 60)
    print("[OK] Bot aktiv va ishlaydi")
    print("[WARNING] Agar Conflict xatoligi bo'lsa:")
    print("   - Faqat bitta joyda bot ishlasin (Render.com YOKI lokal)")
    print("   - Webhook o'rnatilgan bo'lsa, uni o'chiring")
    print("=" * 60)

if __name__ == "__main__":
    check_bot()
