# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime

BOT_TOKEN = "8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s"

print("=" * 60)
print("BOT STATUS TEKSHIRUVI")
print("=" * 60)

# 1. Bot ma'lumotlari
print("\n[1] BOT MA'LUMOTLARI:")
print("-" * 60)
try:
    response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe", timeout=10)
    bot_info = response.json()
    if bot_info.get('ok'):
        result = bot_info['result']
        print(f"[OK] Bot ID: {result['id']}")
        print(f"[OK] Username: @{result['username']}")
        print(f"[OK] Name: {result['first_name']}")
        print(f"[OK] Bot aktiv va ishlayapti!")
    else:
        print("[ERROR] Bot topilmadi yoki token noto'g'ri")
except Exception as e:
    print(f"[ERROR] Xatolik: {e}")

# 2. Oxirgi updatelar
print("\n[2] OXIRGI UPDATELAR (Bot faolmi?):")
print("-" * 60)
try:
    response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?limit=10&offset=-10", timeout=10)
    updates = response.json()
    
    if updates.get('ok') and updates.get('result'):
        print(f"[OK] Jami {len(updates['result'])} ta update topildi")
        
        if len(updates['result']) > 0:
            print("\nOxirgi 5 ta xabar:")
            for i, update in enumerate(updates['result'][-5:], 1):
                if 'message' in update:
                    msg = update['message']
                    user = msg.get('from', {}).get('first_name', 'Unknown')
                    text = msg.get('text', 'No text')[:50]
                    timestamp = msg.get('date', 0)
                    date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"  {i}. {user}: {text} ({date_str})")
        else:
            print("[INFO] Hali hech kim botdan foydalanmagan")
    else:
        print("[INFO] Updatelar topilmadi")
except Exception as e:
    print(f"[ERROR] Xatolik: {e}")

# 3. Webhook status
print("\n[3] WEBHOOK STATUS:")
print("-" * 60)
try:
    response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo", timeout=10)
    webhook_info = response.json()
    
    if webhook_info.get('ok'):
        result = webhook_info['result']
        if result.get('url'):
            print(f"[WARNING] Webhook o'rnatilgan!")
            print(f"  URL: {result['url']}")
            print(f"  Pending updates: {result.get('pending_update_count', 0)}")
            print(f"  Last error: {result.get('last_error_message', 'None')}")
            print("\n[!] MUAMMO: Webhook polling bilan konflikt qiladi!")
            print("[!] Render.com da bot polling rejimida ishlashi kerak!")
        else:
            print("[OK] Webhook yo'q - polling rejimida ishlaydi")
    else:
        print("[ERROR] Webhook ma'lumotini ololmadim")
except Exception as e:
    print(f"[ERROR] Xatolik: {e}")

# 4. Xulosa
print("\n" + "=" * 60)
print("XULOSA:")
print("=" * 60)

if bot_info.get('ok'):
    print("[OK] Bot Telegram da mavjud va faol")
    print(f"[OK] Bot username: @{bot_info['result']['username']}")
    
    if webhook_info.get('ok') and webhook_info['result'].get('url'):
        print("[WARNING] Webhook o'rnatilgan - bu muammo!")
        print("[ACTION] Webhook ni o'chirish kerak:")
        print("         python -c \"import requests; requests.get('https://api.telegram.org/bot8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s/deleteWebhook')\"")
    else:
        print("[OK] Webhook yo'q - to'g'ri sozlangan")
    
    if len(updates.get('result', [])) > 0:
        print(f"[OK] Bot {len(updates['result'])} ta xabar qabul qilgan")
        print("[OK] Bot ishlayapti!")
    else:
        print("[INFO] Bot hali ishlatilmagan")
        print("[ACTION] Telegram da @Yuklauz7_bot ga /start yuboring")
else:
    print("[ERROR] Bot topilmadi - token noto'g'ri!")

print("\n" + "=" * 60)
print("RENDER.COM DA 24/7 ISHLASH:")
print("=" * 60)
print("[INFO] Render.com bepul planda 15 daqiqadan keyin uxlaydi")
print("[ACTION] UptimeRobot qo'shing: https://uptimerobot.com/")
print("[ACTION] Har 5 daqiqada Render service URL ga ping yuboring")
print("=" * 60)
