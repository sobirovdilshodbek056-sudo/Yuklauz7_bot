# 🚀 RENDER.COM DA 24/7 UZOQ MUDDATLI ISHLASH

> [!IMPORTANT]
> Bot endi **1-2 oy yoki undan ko'proq** vaqt to'xtovsiz ishlash uchun optimallashtirilgan!

## ✅ Yangi Imkoniyatlar (2026-02-14)

- ✅ **Xotira monitoring** - Avtomatik xotira nazorati va GC
- ✅ **Auto-cleanup** - Har soatda downloads tozalanadi
- ✅ **Log rotation** - Maksimal 40MB (10MB × 4 fayl)
- ✅ **Graceful shutdown** - To'g'ri to'xtash mexanizmi
- ✅ **Memory threshold** - 450MB dan oshsa avtomatik tozalash
- ✅ **3 daqiqalik keep-alive** - Tezlashtirilgan ping (5→3 min)

---

## 🔥 TEZKOR QADAMLAR (5 daqiqa)

### 1️⃣ Render.com ga Deploy

#### A. GitHub ga Yuklash
```bash
git add .
git commit -m "24/7 uzoq muddatli ishlash - optimallashtirilgan"
git push origin main
```

#### B. Render Deploy
1. [Render Dashboard](https://dashboard.render.com/) ga kiring
2. **"New +"** → **"Web Service"**
3. Repository ni ulang
4. Sozlamalar:
   - **Name:** `yuklauz7-bot`
   - **Runtime:** `Python 3`
   - **Build Command:** Auto-detect
   - **Start Command:** `python bot.py`
5. **Environment Variables:**
   ```
   BOT_TOKEN = 8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s
   PORT = 8080
   MEMORY_THRESHOLD_MB = 450
   AUTO_CLEANUP_INTERVAL = 3600
   MAX_LOG_SIZE_MB = 20
   ```
6. **Create Web Service** → Deploy (3-5 min)

#### C. URL Saqlash
Deploy tugagach URL ko'rinadi:
```
https://yuklauz7-bot.onrender.com
```

---

### 2️⃣ UptimeRobot Sozlash

#### A. Ro'yxatdan O'tish
1. [UptimeRobot.com](https://uptimerobot.com/)
2. **Sign Up Free** → Email tasdiqlash

#### B. Monitor Qo'shish

| Maydon | Qiymat |
|--------|--------|
| **Monitor Type** | HTTP(s) |
| **Friendly Name** | Yuklauz7 Bot |
| **URL** | `https://yuklauz7-bot.onrender.com/health` |
| **Interval** | **5 minutes** |

> [!WARNING]
> URL oxirida `/health` bo'lishi **SHART**!

---

### 3️⃣ Tekshirish

#### ✅ UptimeRobot:
- Status: **🟢 Up**
- Uptime: **100%**

#### ✅ Render Logs:
Har 3 daqiqada:
```
🔄 Keep-alive: Bot aktiv | Uptime: 5.2 kun | Memory: 145.3MB
GET /health HTTP/1.1" 200
```

Har soatda:
```
🧹 Auto-cleanup: 2 ta fayl tozalanmoqda...
✅ Auto-cleanup tugadi
```

#### ✅ Telegram:
```
/start → Bot javob beradi ✅
```

---

## 📊 Ishlash Diagrammasi

```mermaid
graph TD
    A[UptimeRobot] -->|Har 3 min ping| B[/health endpoint]
    B --> C{Bot aktiv?}
    C -->|Ha| D[200 OK qaytaradi]
    C -->|Yo'q| E[Auto-restart]
    D --> F[Render: Bot ishlatilmoqda]
    F --> G[24/7 FAOL]
    
    H[Keep-alive Job] -->|Har 3 min| I[Memory tekshirish]
    I -->|>450MB| J[GC ishga tushadi]
    I -->|<450MB| G
    
    K[Auto-cleanup Job] -->|Har soat| L[Downloads tozalash]
    L --> G
```

---

## 🔧 Xotira va Resource Monitoring

### Avtomatik Xotira Nazorati

Bot har 3 daqiqada xotirani tekshiradi:

```
Memory < 450MB: ✅ Normal
Memory > 450MB: ⚠️ GC ishga tushadi
```

**Namuna log:**
```
🔄 Keep-alive: Bot aktiv | Uptime: 12.5 kun | Memory: 455.2MB
⚠️ Memory threshold oshdi: 455.2MB > 450MB
🧹 Garbage collection ishga tushirilmoqda...
✅ GC dan keyin: 320.1MB (tejaldi: 135.1MB)
```

### Auto-Cleanup (Har Soat)

Downloads papkasi avtomatik tozalanadi:

```
🧹 Auto-cleanup: 5 ta fayl tozalanmoqda...
✅ Auto-cleanup tugadi
```

Bu disk to'lib ketmasligini ta'minlaydi.

---

## ⚠️ Muammolarni Hal Qilish

### ❌ Monitor "Down"

**Sabab:**
- Bot hali deploy bo'lmagan
- URL xato
- `/health` unutilgan

**Yechim:**
1. Render → **Live** status?
2. URL to'g'ri?
3. Brauzerni ochib test qiling:
   ```
   https://yuklauz7-bot.onrender.com/health
   ```
   Ko'rinishi kerak: `{"status": "ok", ...}`

---

### ❌ Xotira To'lib Ketmoqda

**Belgi:** Logs da `⚠️ Memory threshold oshdi`

**Yechim:**
- ✅ Auto GC avtomatik ishlaydi
- ✅ Qayta ishga tushish kerak emas
- 📊 Logsda `✅ GC dan keyin` ni kuzating

---

### ❌ Disk To'lib Ketdi

**Sabab:** Log fayllar yoki downloads

**Yechim:**
1. Auto-cleanup ishlayaptimi? (logsda `🧹 Auto-cleanup` izlang)
2. Log rotation ishlayaptimi? (max 40MB)
3. Agar davom etsa, Render **Shell** tab:
   ```bash
   rm -rf downloads/*
   rm -f bot.log.*
   ```

---

## 📈 Monitoring Skript

Qo'lda tekshirish uchun:

```bash
python monitor_bot.py
```

Natija:
```
💾 Memory Usage: 145.23 MB
✅ Bot API: Online (@Yuklauz7_bot)
✅ Health Endpoint: OK
💿 Disk: 8.5GB / 10GB free (15% used)
📄 Log fayl: 8.34 MB

✅ Passed: 5/5
🎉 Barcha tekshiruvlar muvaffaqiyatli!
```

---

## 🎯 Render Free Plan Cheklovi

| Resurs | Limit |
|--------|-------|
| **Uptime** | 750 soat/oy (≈31 kun) |
| **RAM** | 512MB |
| **Disk** | Cheklangan |
| **Deploy** | Tez (3-5 min) |

> [!TIP]
> UptimeRobot bilan bot doimo aktiv bo'ladi va uyquga ketmaydi!

---

## 🔗 Foydali Havolalar

- 🌐 [Render Dashboard](https://dashboard.render.com/)
- 📊 [UptimeRobot](https://uptimerobot.com/)
- 📱 [Telegram Bot](https://t.me/Yuklauz7_bot)
- 📚 Batafsil: [`MONITORING_GUIDE.md`](MONITORING_GUIDE.md)
- 📋 UptimeRobot setup: [`UPTIMEROBOT_SOZLASH.md`](UPTIMEROBOT_SOZLASH.md)

---

## ✅ Xulosa

Agar hammasi to'g'ri sozlangan bo'lsa:

1. ✅ Bot Render.com da deploy bo'lgan
2. ✅ UptimeRobot har 5 daqiqada ping yuboradi
3. ✅ Xotira avtomatik nazorat qilinadi
4. ✅ Downloads har soatda tozalanadi
5. ✅ Log fayllar maksimal 40MB
6. ✅ Bot **1-2 oy yoki undan ko'proq** vaqt 24/7 ishlaydi

**Bot endi uzoq muddatli 24/7 ishlash uchun tayyor! 🎉🚀**

