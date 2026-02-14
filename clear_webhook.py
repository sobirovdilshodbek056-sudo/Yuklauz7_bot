import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s")

print("=" * 60)
print("WEBHOOK TOZALASH")
print("=" * 60)

# Delete webhook
url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook?drop_pending_updates=true"
response = requests.get(url, timeout=10)

if response.status_code == 200:
    result = response.json()
    if result.get("ok"):
        print("✅ Webhook muvaffaqiyatli tozalandi!")
        print(f"   Natija: {result.get('description', 'OK')}")
    else:
        print(f"❌ Xatolik: {result.get('description', 'Unknown error')}")
else:
    print(f"❌ HTTP xatolik: {response.status_code}")

# Get webhook info to verify
url2 = f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo"
response2 = requests.get(url2, timeout=10)

if response2.status_code == 200:
    info = response2.json().get("result", {})
    webhook_url = info.get("url", "")
    if webhook_url:
        print(f"⚠️  Webhook hali o'rnatilgan: {webhook_url}")
    else:
        print("✅ Webhook to'liq tozalangan!")
        
print("=" * 60)
print("Render.com endi muvaffaqiyatli restart bo'lishi kerak!")
print("=" * 60)
