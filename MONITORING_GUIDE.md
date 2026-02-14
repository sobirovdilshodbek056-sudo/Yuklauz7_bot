# 🔧 24/7 Monitoring va Troubleshooting Guide

## Bot Monitoring - Botni Kuzatish

Bot uzoq muddatli (1-2 oy+) 24/7 ishlashini ta'minlash uchun monitoring qo'llanmasi.

---

## 1️⃣ UptimeRobot Sozlash

### A. Monitor Yaratish

1. **UptimeRobot.com** ga kiring: https://uptimerobot.com/
2. **Dashboard** → **"+ Add New Monitor"**
3. Quyidagi sozlamalani kiriting:

| Sozlama | Qiymat |
|---------|--------|
| **Monitor Type** | HTTP(s) |
| **Friendly Name** | Yuklauz7 Bot Health |
| **URL** | `https://yuklauz7-bot.onrender.com/health` |
| **Monitoring Interval** | 5 minutes |
| **Monitor Timeout** | 30 seconds |

4. **Alert Contacts** qo'shing (email yoki Telegram)

### B. Monitoring Natijalar

✅ **Normal (Yashil):**
- Status: **Up** (🟢)
- Uptime: **99%+**
- Response Time: **< 2000ms**

⚠️ **Ogohantirish (Sariq):**
- Response Time: **2000-5000ms** (sekin)
- Sabab: Render server yuklanishi mumkin

❌ **Muammo (Qizil):**
- Status: **Down** (🔴)
- Sabab: Bot to'xtagan yoki Render sleep mode

---

## 2️⃣ Render.com Logs Monitoring

### Logs Ochish

1. **Render Dashboard** → **yuklauz7-bot**
2. **Logs** tab
3. **Auto-scroll** ni yoqing

### Normal Loglar (Har 3 daqiqada):

```
🔄 Keep-alive: Bot aktiv | Uptime: 12.5 kun | Memory: 145.2MB
GET /health HTTP/1.1" 200
```

### Xotira Monitoring Loglari:

```
⚠️ Memory threshold oshdi: 455.3MB > 450MB
🧹 Garbage collection ishga tushirilmoqda...
✅ GC dan keyin: 320.1MB (tejaldi: 135.2MB)
```

### Auto-Cleanup Loglari (Har soatda):

```
🧹 Auto-cleanup: 3 ta fayl tozalanmoqda...
✅ Auto-cleanup tugadi
```

---

## 3️⃣ Xotira Muammolarini Hal Qilish

### Muammo: Xotira Oshib Ketmoqda

**Belgilar:**
- Log: `⚠️ Memory threshold oshdi: 480MB > 450MB`
- Bot sekinlashadi
- Render restart qiladi

**Yechim:**

1. **Auto-cleanup ishlayaptimi?** (logs tekshiring)
2. **Downloads papkasi** to'lib ketmagan?
3. **Log fayli** juda katta emas? (>20MB)

### Qo'lda Tozalash:

Render dashboard da **Shell** tab:

```bash
# Downloads tozalash
rm -rf downloads/*

# Log fayllarni tozalash
rm -f bot.log.*
```

---

## 4️⃣ Disk To'lib Ketishi

### Muammo: Disk Space Kam

**Belgilar:**
- Log: `⚠️ Log fayli katta: 25.3MB`
- Bot yozish xatoliklari

**Yechim:**

Log rotation avtomatik ishlashi kerak (10MB max, 3 backup).

Agar problem davom etsa, qo'lda tozalash:

```bash
# Eski loglarni o'chirish
rm -f bot.log.1 bot.log.2 bot.log.3

# Hozirgi logni tozalash (faqat zarurat bo'lsa!)
> bot.log
```

---

## 5️⃣ Bot To'xtab Qolsa (Restart)

### Auto-Restart:

Bot kodida `main()` funksiyada auto-restart mavjud:

```python
except Exception as e:
    logger.error(f"[ERROR] Polling xatolik: {e}")
    logger.info("[RESTART] 5 soniyadan keyin qayta ishga tushirish...")
    time.sleep(5)
    main()  # Rekursiv restart
```

### Qo'lda Restart:

Render dashboard:
1. **Manual Deploy** tugmasi
2. Yoki **Settings** → **Restart**

---

## 6️⃣ Monitoring Skriptlar

### Local Monitoring (kompyuterdan):

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

## 7️⃣ Keng Tarqalgan Muammolar

### ❌ Bot 15 daqiqada to'xtaydi

**Sabab:** UptimeRobot ishlamayapti

**Yechim:**
1. UptimeRobot monitor **Paused** emasligini tekshiring
2. URL to'g'ri: `https://your-bot.onrender.com/health`
3. Interval: **5 minutes**

---

### ❌ "Conflict" xatoligi

**Sabab:** Bot 2 joyda ishlamoqda (local + Render)

**Yechim:**
1. Local botni to'xtating
2. Yoki Render botni pause qiling

---

### ❌ Video yuklanmayapti

**Sabab:** Bu monitoring muammosi emas, lekin:

**Yechim:**
1. Logs tekshiring: xatolik xabari?
2. Bot ishlayaptimi? (`/start` yuborib ko'ring)
3. `VIDEO_YUKLANMAYAPTI_YECHIM.md` ni o'qing

---

## 8️⃣ Performance Metrics

### Ideal Holatda:

| Metrika | Qiymat |
|---------|--------|
| **Memory Usage** | 100-300 MB |
| **Uptime** | 99%+ |
| **Response Time** | < 2000ms |
| **Disk Usage** | < 50% |
| **Log Size** | < 20MB |
| **Downloads Folder** | Bo'sh (auto-cleanup) |

### Ogohantirish Chorasi:

| Metrika | Threshold | Harakat |
|---------|-----------|---------|
| Memory | > 450MB | Auto GC |
| Disk | > 90% | Logs tozalash |
| Log Size | > 20MB | Rotation |
| Uptime | < 95% | Render restart |

---

## 9️⃣ Alerts Setup (Qo'shimcha)

### UptimeRobot Email Alerts:

1. **My Settings** → **Alert Contacts**
2. **Add Alert Contact** → **Email**
3. Email kiriting va tasdiqlang
4. Monitor sozlamalarida **Alert Contacts** tanlang

### Telegram Alerts (UptimeRobot uchun):

1. UptimeRobot dashboard
2. **Integrations** → **Telegram**
3. Ko'rsatmalarga amal qiling

---

## 🎯 Tavsiyalar

### Kunlik Tekshiruv (5 daqiqa):

1. ✅ UptimeRobot status (Yashil bo'lishi kerak)
2. ✅ Render logs (Xatoliklar yo'q)
3. ✅ Bot responseiveness (Telegram test)

### Haftalik Tekshiruv (10 daqiqa):

1. 📊 Uptime percentage (99%+)
2. 💾 Memory trends
3. 📄 Log fayllar hajmi
4. 🔄 Auto-cleanup ishlayaptimi?

### Oylik Tekshiruv:

1. 📈 Render usage (750 soat limit)
2. 🔧 Dependencies yangilash
3. 🧪 Performance test

---

## 📞 Qo'shimcha Yordam

Agar muammolar davom etsa:

1. **Logs** to'liq nusxasini saqlang
2. **Screenshot** oling (error message)
3. **UptimeRobot** status history ko'ring
4. **monitor_bot.py** natijalarini tekshiring

---

**Muvaffaqiyatlar! Bot 1-2 oy yoki undan ko'proq vaqt 24/7 ishlaydi! 🚀**
