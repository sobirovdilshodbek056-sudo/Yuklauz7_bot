# 🚀 UptimeRobot Sozlash - Render.com 24/7 Ishlash

> **Maqsad:** Botingiz Render.com bepul versiyasida 15 daqiqadan keyin uxlab qolishini oldini olish.

---

## 📋 Kerakli Ma'lumotlar

1. **Render Bot URL:** Render.com dashboarddan oling
   - Misol: `https://yuklauz7-bot.onrender.com`
   
2. **Health Check Endpoint:** `/health` qo'shiladi
   - To'liq URL: `https://yuklauz7-bot.onrender.com/health`

---

## ⚡ 1-QADAM: Render URL Topish

### A. Render.com ga kirish
1. Brauzeringizda ochish: [https://render.com/](https://render.com/)
2. **Log In** tugmasini bosish
3. GitHub orqali kirish

### B. Bot URL topish
1. Dashboard da **"yuklauz7-bot"** (yoki sizning bot nomingiz) ni bosing
2. Yuqori qismda **URL** manzili ko'rinadi:
   ```
   https://your-bot-name.onrender.com
   ```
3. Bu URLni **nusxalang** (copy qiling)

---

## ⚡ 2-QADAM: UptimeRobot.com da Monitor Qo'shish

### A. Ro'yxatdan o'tish (birinchi marta)
1. Brauzeringizda ochish: [https://uptimerobot.com/](https://uptimerobot.com/)
2. **"Sign Up Free"** yoki **"Get Started"** tugmasini bosing
3. Email manzilingizni kiriting va ro'yxatdan o'ting
4. Email tasdiqdan o'tkazing (inbox ni tekshiring)

### B. Dashboard ga kirish
1. Kirganingizdan keyin, **Dashboard** ga tushadi
2. **"+ Add New Monitor"** tugmasini bosing (yuqori chap tomonda)

---

## ⚡ 3-QADAM: Monitor Sozlamalari

Monitor qo'shish oynasida quyidagi sozlamalarni kiriting:

### 🔧 Asosiy Sozlamalar:

| Maydon | Qiymat | Izoh |
|--------|--------|------|
| **Monitor Type** | `HTTP(s)` | Dropdown dan tanlang |
| **Friendly Name** | `Yuklauz7 Bot` | Istalgan nom |
| **URL (or IP)** | `https://your-bot.onrender.com/health` | **MUHIM:** `/health` ni unutmang! |
| **Monitoring Interval** | `5 minutes` | Bepul versiyada 5 daqiqa minimal |
| **Monitor Timeout** | `30 seconds` | O'zgarishsiz qoldiring |

### ✅ Misol URL (o'zingizniki bilan almashtiring):
```
https://yuklauz7-bot.onrender.com/health
```

### 📸 Screenshot:
```
Monitor Type:         [HTTP(s)          ▼]
Friendly Name:        [Yuklauz7 Bot         ]
URL (or IP):          [https://your-bot.onrender.com/health]
Monitoring Interval:  [5 minutes        ▼]
```

---

## ⚡ 4-QADAM: Monitor Yaratish

1. Barcha maydonlarni to'ldirgandan keyin
2. Pastda **"Create Monitor"** tugmasini bosing
3. Monitor ro'yxatida **"Yuklauz7 Bot"** paydo bo'ladi

---

## ✅ Tekshirish

### 1. UptimeRobot Dashboardda:
- Monitor statusi: **🟢 Up** (yashil) bo'lishi kerak
- Uptime: **100%** ko'rsatsa, hammasi to'g'ri

### 2. Render.com Logs da:
1. Render dashboardga qaytish
2. **"Logs"** tabini ochish
3. Har **5 daqiqada** quyidagi log ko'rinishi kerak:
   ```
   GET /health HTTP/1.1 200
   ```

### 3. Bot Telegram da:
- Telegram da `/start` buyrug'ini yuboring
- Bot javob berishi kerak
- 15-20 daqiqadan keyin yana `/start` yuboring
- Bot tez javob bersa, 24/7 ishlayapti demak ✅

---

## 🎯 Natija

Agar hammasi to'g'ri sozlangan bo'lsa:

✅ UptimeRobot har **5 daqiqada** botga ping yuboradi  
✅ Render bot **ishlab turganini** ko'radi  
✅ Bot **hech qachon uxlamaydi**  
✅ Bot **24/7 faol** bo'ladi  

---

## ⚠️ Tez-tez Beriladigan Savollar

### ❓ Monitor qizil (Down) ko'rsatsa?
**Sabab:** Bot deploy bo'lmagan yoki URL noto'g'ri.

**Yechim:**
1. Render.com da bot **"Live"** statusida ekanligini tekshiring
2. URL to'g'ri yozilganligini tekshiring
3. `/health` qo'shilganligini tekshiring

### ❓ Bot baribir uxlab qolyaptimi?
**Sabab:** UptimeRobot URL noto'g'ri yoki monitoring interval juda katta.

**Yechim:**
1. URL oxirida `/health` borligini tekshiring
2. Monitoring Interval **5 minutes** ekanligini tekshiring
3. Monitor **Paused** holatida emasligini tekshiring

### ❓ Render logs da `/health` ko'rinmayapti?
**Sabab:** UptimeRobot hali ping yubormagan yoki monitor noto'g'ri sozlangan.

**Yechim:**
1. UptimeRobot dashboardda monitor **aktiv (Up)** ekanligini tekshiring
2. 5-10 daqiqa kuting va loglarni yangilang
3. Qo'lda brauzerdanda `https://your-bot.onrender.com/health` ni ochib ko'ring

---

## 🔗 Foydali Havolalar

- [UptimeRobot.com](https://uptimerobot.com/) - Bepul monitoring
- [Render.com Dashboard](https://dashboard.render.com/) - Bot statusini ko'rish
- [Telegram Bot](https://t.me/Yuklauz7_bot) - Botingiz

---

## 📞 Yordam

Agar muammo yoki savol bo'lsa, quyidagilarni tekshiring:
1. Render.com da bot **deploy bo'lgan** va **Live** statusida
2. UptimeRobot da monitor **URL to'g'ri** va `/health` bor
3. Monitor **aktiv (Up)** holatda
4. Monitoring Interval **5 minutes**

**Hammasi ishlayapti lekin hali ham savol bormi?** 
Bot kodida LOG mavjud - Render.com **Logs** bo'limidan tekshiring! 🔍
