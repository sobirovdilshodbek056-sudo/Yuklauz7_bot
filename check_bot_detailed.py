#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot statusini tekshirish - Qaysi bot ishlayapti?
"""
import requests
import sys

BOT_TOKEN = "8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s"

print("=" * 60)
print("BOT STATUS TEKSHIRUVI - Qaysi bot ishlayapti?")
print("=" * 60)

# 1. getMe - bot info
print("\n[1] Bot Ma'lumotlari:")
print("-" * 60)
try:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    response = requests.get(url, timeout=10)
    data = response.json()
    if data['ok']:
        result = data['result']
        print(f"[OK] Bot ID: {result['id']}")
        print(f"[OK] Username: @{result['username']}")
        print(f"[OK] Name: {result['first_name']}")
    else:
        print(f"[ERROR] {data}")
except Exception as e:
    print(f"[ERROR] {e}")

# 2. getUpdates - oxirgi xabarlar
print("\n[2] Oxirgi Xabarlar (Bot faolmi?):")
print("-" * 60)
try:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?limit=5&offset=-5"
    response = requests.get(url, timeout=10)
    data = response.json()
    if data['ok']:
        updates = data['result']
        print(f"[OK] Jami {len(updates)} ta xabar")
        
        if len(updates) > 0:
            print("\nOxirgi 5 ta xabar:")
            for i, upd in enumerate(updates[-5:], 1):
                msg = upd.get('message', {})
                text = msg.get('text', 'N/A')[:50]
                user = msg.get('from', {}).get('first_name', 'Unknown')
                date = msg.get('date', 0)
                
                from datetime import datetime
                dt = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
                print(f"  {i}. {user}: {text} ({dt})")
        else:
            print("[INFO] Hozircha xabar yo'q")
    else:
        print(f"[ERROR] {data}")
except Exception as e:
    print(f"[ERROR] {e}")

# 3. Webhook status
print("\n[3] Webhook Status:")
print("-" * 60)
try:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo"
    response = requests.get(url, timeout=10)
    data = response.json()
    if data['ok']:
        info = data['result']
        webhook_url = info.get('url', '')
        if webhook_url:
            print(f"[WARNING] Webhook AKTIV: {webhook_url}")
            print("[ACTION] Webhook o'chirish kerak - polling uchun!")
            print("[ACTION] Buyruq: curl https://api.telegram.org/bot{TOKEN}/deleteWebhook")
        else:
            print("[OK] Webhook yo'q - polling rejimida ishlaydi")
        
        pending = info.get('pending_update_count', 0)
        if pending > 0:
            print(f"[WARNING] {pending} ta pending update bor")
    else:
        print(f"[ERROR] {data}")
except Exception as e:
    print(f"[ERROR] {e}")

# 4. Test message yuborish
print("\n[4] Test Xabar (Botdan javob kutamiz):")
print("-" * 60)
print("[INFO] Telegram da botga /start yuboring")
print("[INFO] 10 sekund ichida xabar kelishi kerak")
print("[INFO] Agar kelmasa - bot ishlamayapti!")

print("\n" + "=" * 60)
print("XULOSA:")
print("=" * 60)

# Final recommendation
print("\n[IMPORTANT] Agar bot javob bermasa:")
print("1. Render.com Logs ni tekshiring")
print("2. Lokal botni to'xtating (Conflict oldini olish)")
print("3. Telegram da /start yuboring va natijani qarang")
print("4. Render da Status: Live bo'lishi kerak")

print("\n[RENDER] https://dashboard.render.com/ ga boring")
print("[TELEGRAM] https://t.me/Yuklauz7_bot ga boring")

print("=" * 60)
