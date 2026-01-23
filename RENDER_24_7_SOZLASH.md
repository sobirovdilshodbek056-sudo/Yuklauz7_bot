# 🚀 RENDER.COM DA 24/7 ISHLASH - TEZKOR YO'RIQNOMA

## ✅ Kod Tayyorligi
Bot allaqachon 24/7 ishlash uchun tayyor:
- ✅ HTTP Health Check Server (`/health` endpoint)
- ✅ Keep-alive ping (har 5 daqiqada)
- ✅ Auto-restart mexanizmi
- ✅ Render.yaml sozlangan

---

## 🔥 QADAMLAR (5 daqiqa)

### 1️⃣ Render.com ga Deploy Qilish

#### A. GitHub ga Yuklash (agar qilmagan bo'lsangiz)
```bash
git add .
git commit -m "24/7 ishlash sozlamalari tayyor"
git push origin main
```

#### B. Render.com da Deploy
1. Brauzerni oching: [https://dashboard.render.com/](https://dashboard.render.com/)
2. **Log In** (GitHub orqali)
3. **"New +"** tugmasini bosing → **"Web Service"**
4. GitHub repository ni ulang (yoki "Existing repo"dan tanlang)
5. Sozlamalar:
   - **Name:** `yuklauz7-bot`
   - **Runtime:** `Python 3`
   - **Build Command:** (auto-detect)
   - **Start Command:** `python bot.py`
6. **Environment Variables** bo'limiga:
   ```
   BOT_TOKEN = 8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s
   PORT = 8080
   ```
7. **"Create Web Service"** tugmasini bosing
8. **Deploy** jarayoni boshlanadi (3-5 daqiqa)

#### C. URL Nusxalash
Deploy tugagach, yuqori qismda URL paydo bo'ladi:
```
https://yuklauz7-bot.onrender.com
```
Bu URLni **nusxalang** (copy) - keyingi qadamda kerak bo ladi!

---

### 2️⃣ UptimeRobot.com Sozlash

#### A. Ro'yxatdan O'tish
1. Ochish: [https://uptimerobot.com/](https://uptimerobot.com/)
2. **"Sign Up Free"** tugmasini bosing
3. Email kiriting va ro'yxatdan o'ting
4. Emailni tasdiqlang

#### B. Monitor Qo'shish
1. Dashboard da **"+ Add New Monitor"** ni bosing
2. Quyidagilarni to'ldiring:

| Maydon | Qiymat |
|--------|--------|
| Monitor Type | **HTTP(s)** |
| Friendly Name | **Yuklauz7 Bot** |
| URL | `https://yuklauz7-bot.onrender.com/health` |
| Monitoring Interval | **5 minutes** |

⚠️ **MUHIM:** URL oxirida `/health` bo'lishi SHART!

3. **"Create Monitor"** tugmasini bosing

---

### 3️⃣ Tekshirish

#### ✅ UptimeRobot da:
- Monitor **🟢 Up** (yashil) bo'lishi kerak
- Uptime: **100%**

#### ✅ Render Logs da:
1. Render dashboard → botingiz → **Logs** tab
2. Har 5 daqiqada quyidagi log ko'rinishi kerak:
   ```
   GET /health HTTP/1.1" 200
   ```

#### ✅ Telegram da:
1. Botga `/start` yuboring
2. Bot javob berishi kerak
3. 15-20 daqiqadan keyin yana `/start`
4. Bot tez javob bersa ✅

---

## 📊 24/7 Ishlash Diagrammasi

```
UptimeRobot (har 5 daqiqada)
     ↓
     → GET /health
     ↓
Yuklauz7_bot (Render.com)
     ↓
     → 200 OK (bot aktiv!)
     ↓
Render: "Bot ishlatilmoqda, uxlatmayman"
     ↓
24/7 FAOL ✅
```

---

## ⚠️ Muammolarni Hal Qilish

### ❌ Monitor "Down" ko'rsatadi
**Sabab:**
- Bot hali deploy bo'lmagan
- URL noto'g'ri
- `/health` unutilgan

**Yechim:**
1. Render da bot **"Live"** statusini tekshiring
2. URL to'g'ri ekanligini tekshiring
3. Qo'lda brauzerni ochib tekshiring:
   ```
   https://your-bot.onrender.com/health
   ```
   Ko'rinishi kerak: `{'status': 'ok', ...}`

### ❌ Bot 15 daqiqadan keyin javob bermayapti
**Sabab:**
- UptimeRobot to'g'ri sozlanmagan
- Monitoring interval juda katta

**Yechim:**
1. UptimeRobot monitor **Paused** emasligini tekshiring
2. URL to'g'ri va `/health` borligini tekshiring
3. Monitoring Interval **5 minutes** ekanligini tekshiring

### ❌ Render logs da `/health` ko'rinmayapti
**Sabab:**
- UptimeRobot hali ping yubormagan (5 daqiqa kutish kerak)
- Monitor noto'g'ri sozlangan

**Yechim:**
1. UptimeRobot da monitor statusini tekshiring
2. 5-10 daqiqa kuting
3. Loglarni yangilang (refresh)

---

## 🎯 Tavsiyalar

### ✅ Render Free Plan Cheklovi:
- ⏰ 750 soat/oyga (≈ 31 kun)
- 💾 512MB RAM
- ⚡ Tez deploy (3-5 daqiqa)

### ✅ UptimeRobot Free Plan:
- 📊 50 ta monitor
- ⏱️ 5 daqiqa interval
- 📧 Email alerts

### 💡 Optimizatsiya:
1. **Monitoring interval:** 5 daqiqa (minimal)
2. **Health check:** Oddiy va tez
3. **Bot:** Polling (webhook emas)

---

## 📈 Monitoring

### Real-time Status:
- **UptimeRobot Dashboard:** Bot statusi
- **Render Logs:** Real-time loglar
- **Telegram:** Bot javoblari

### Loglar:
Render Logs da ko'rishingiz kerak:
```
[BOT] Yuklauz7_bot ishga tushdi!
[HEALTH] HTTP server ishga tushdi: http://0.0.0.0:8080
[KEEP-ALIVE] Har 5 daqiqada ping yuboriladi
🔄 Keep-alive ping: Bot aktiv va ishlayapti
GET /health HTTP/1.1" 200
```

---

## 🔗 Foydali Havolalar

- 🌐 **Render Dashboard:** https://dashboard.render.com/
- 📊 **UptimeRobot:** https://uptimerobot.com/
- 📱 **Telegram Bot:** https://t.me/Yuklauz7_bot
- 📚 **Batafsil Qo'llanma:** `UPTIMEROBOT_SOZLASH.md`

---

## ✅ Xulosa

Agar hammasi to'g'ri sozlangan bo'lsa:
1. ✅ Bot Render.com da deploy bo'lган
2. ✅ UptimeRobot har 5 daqiqada ping yuboradi
3. ✅ Bot 24/7 faol turadi
4. ✅ Render bot uxlamaydi

**Muvaffaqiyatlar! 🎉**
