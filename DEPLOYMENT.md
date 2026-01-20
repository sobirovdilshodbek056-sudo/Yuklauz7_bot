# 🚀 Yuklauz7_bot - Deployment Qo'llanmasi

## ⚠️ MUHIM: Bot 10 daqiqadan keyin ishlamay qolish muammosi

Agar botingiz 10-15 daqiqadan keyin ishlamay qolayotgan bo'lsa, bu **hosting platformaning bepul plan cheklovi** tufayli.

### 🔍 Muammo sabablari:

1. **Render.com FREE plan** - 15 daqiqadan keyin "uxlaydi" (inactive)
2. **Railway.app FREE plan** - Oyiga 5$ kredit tugagach to'xtaydi
3. **Heroku** - Bepul plan yo'q (2022-yildan boshlab)

---

## ✅ YECHIM: Eng yaxshi bepul platformalar

### 1️⃣ **KOYEB.COM** (⭐⭐⭐⭐⭐ ENG YAXSHI!)

**Afzalliklari:**
- ✅ 100% BEPUL
- ✅ Doimo aktiv (uxlamaydi!)
- ✅ Tez deployment
- ✅ Avtomatik SSL
- ✅ Global CDN

**Deployment:**

```bash
# 1. GitHub ga yuklang
git add .
git commit -m "Keep-alive mexanizmi qo'shildi"
git push origin main

# 2. Koyeb.com ga kiring
# 3. "Create App" tugmasini bosing
# 4. GitHub repository ni tanlang
# 5. Environment variable qo'shing:
#    BOT_TOKEN = <sizning_bot_tokeningiz>
# 6. Deploy!
```

**Link:** https://www.koyeb.com/

---

### 2️⃣ **RAILWAY.APP** (⭐⭐⭐⭐ YAXSHI)

**Afzalliklari:**
- ✅ Oyiga 5$ kredit BEPUL
- ✅ Oson deployment
- ✅ Yaxshi monitoring

**Kamchiliklari:**
- ⚠️ 5$ tugagach to'xtaydi (odatda 1 oyga yetadi)

**Deployment:**

```bash
# 1. GitHub ga yuklang
git add .
git commit -m "Keep-alive mexanizmi qo'shildi"
git push origin main

# 2. Railway.app ga kiring
# 3. "New Project" -> "Deploy from GitHub repo"
# 4. Repository ni tanlang
# 5. Environment variable qo'shing:
#    BOT_TOKEN = <sizning_bot_tokeningiz>
# 6. Deploy!
```

**Link:** https://railway.app/

---

### 3️⃣ **RENDER.COM** (⭐⭐⭐ O'RTACHA)

**Afzalliklari:**
- ✅ BEPUL

**Kamchiliklari:**
- ❌ 15 daqiqadan keyin uxlaydi
- ❌ Keep-alive mexanizmi to'liq ishlamaydi

**Deployment:**

```bash
# 1. GitHub ga yuklang
git add .
git commit -m "Keep-alive mexanizmi qo'shildi"
git push origin main

# 2. Render.com ga kiring
# 3. "New" -> "Worker"
# 4. GitHub repository ni tanlang
# 5. Environment variable qo'shing:
#    BOT_TOKEN = <sizning_bot_tokeningiz>
# 6. Deploy!
```

**Link:** https://render.com/

---

## 🔧 Kod o'zgarishlari (ALLAQACHON QILINGAN!)

Quyidagi o'zgarishlar **allaqachon qilingan**:

### 1. Keep-alive mexanizmi qo'shildi
```python
# bot.py - 395-qator
async def keep_alive_ping(context: ContextTypes.DEFAULT_TYPE):
    """Har 5 daqiqada ping yuboradi"""
    logger.info("🔄 Keep-alive ping: Bot aktiv va ishlayapti")
```

### 2. Job scheduler qo'shildi
```python
# bot.py - 438-qator
job_queue.run_repeating(keep_alive_ping, interval=300, first=60)
```

### 3. Timeout vaqtlari oshirildi
```python
# bot.py - 421-424-qatorlar
.read_timeout(120)      # 60 -> 120 sekund
.write_timeout(120)     # 60 -> 120 sekund
.connect_timeout(60)    # 30 -> 60 sekund
.pool_timeout(60)       # Yangi
```

### 4. YouTube cookie o'chirildi
```python
# bot.py - 166-167-qatorlar
# "cookiesfrombrowser": ("chrome",),  # Serverlarda ishlamaydi
```

### 5. Railway restart policy yaxshilandi
```json
// railway.json
"restartPolicyType": "ALWAYS",
"restartPolicyMaxRetries": 999
```

---

## 📊 Monitoring

Botning ishlayotganini tekshirish uchun:

1. **Koyeb:** Dashboard -> Logs
2. **Railway:** Dashboard -> Deployments -> Logs
3. **Render:** Dashboard -> Logs

Har 5 daqiqada quyidagi xabarni ko'rishingiz kerak:
```
🔄 Keep-alive ping: Bot aktiv va ishlayapti
```

---

## 🎯 Tavsiya

**KOYEB.COM** dan foydalaning - bu eng yaxshi bepul variant!

- ✅ Doimo aktiv
- ✅ Tez
- ✅ Ishonchli
- ✅ 100% BEPUL

---

## ❓ Savol-javoblar

**S: Bot hali ham 10 daqiqadan keyin to'xtayapti?**

J: Qaysi platformadan foydalanyapsiz?
- **Render.com** - Bu normal, bepul planda shunday. Koyeb.com ga o'ting.
- **Railway.app** - 5$ kredit tugagan bo'lishi mumkin.
- **Koyeb.com** - Bunday bo'lmasligi kerak. Loglarni tekshiring.

**S: Keep-alive ishlayaptimi?**

J: Loglarni tekshiring. Har 5 daqiqada "Keep-alive ping" xabarini ko'rishingiz kerak.

**S: Qaysi platform eng yaxshi?**

J: **Koyeb.com** - 100% bepul va doimo aktiv!

---

## 📞 Yordam

Agar muammo davom etsa:
1. Loglarni tekshiring
2. Bot tokenni tekshiring
3. GitHub repository yangilanganini tekshiring
4. Platformani qayta deploy qiling

**Muvaffaqiyatlar! 🚀**
