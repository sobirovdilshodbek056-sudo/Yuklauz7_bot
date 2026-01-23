# RENDER.COM DA BOT TEKSHIRISH VA TUZATISH

## Hozirgi Holat

Bot kodi to'g'ri:
- ✅ Instagram, TikTok, Facebook qo'llab-quvvatlanadi
- ✅ yt-dlp sozlamalari to'g'ri
- ✅ HTTP Health Check `/health` ishlaydi
- ✅ Keep-alive mexanizmi bor

## Muammo

Bot Telegram da link yuborilganda video yuklamayapti.

## Ehtimoliy Sabablar

### 1. Render.com da bot ishlamayapti
**Tekshirish:**
1. https://dashboard.render.com/ ga kiring
2. "yuklauz7-bot" ni oching
3. **Status** ni tekshiring:
   - ✅ **Live** - bot ishlayapti
   - ❌ **Failed** - xatolik bor
   - ⏳ **Building** - hali deploy bo'lmagan

4. **Logs** ni tekshiring:
   - Quyidagi log ko'rinishi kerak:
     ```
     [BOT] Yuklauz7_bot ishga tushdi!
     ```

**Agar "Failed" yoki xatolik bo'lsa:**
- Logs da xatolik xabarini ko'ring
- Build xatoligi bo'lishi mumkin (ffmpeg, yt-dlp)
- Environment variable (BOT_TOKEN) yo'q bo'lishi mumkin

### 2. Ikkita bot ishlayapti (Conflict)
**Sabab:** Bir vaqtning o'zida:
- Lokal kompyuterda bot ishlab turib
- Render.com da ham bot ishlab turib
- Ikkalasi ham bir TOKEN dan foydalanmoqda

**Natija:** Telegram faqat birinchi botga ulanadi, ikkinchisi ishlamaydi

**Yechim:**
- **Lokal botni to'xtating** (agar ishlab turgan bo'lsa)
- Faqat Render.com dagi bot ishlashi kerak

### 3. yt-dlp versiyasi eski
**Sabab:** Instagram/TikTok API o'zgargan, eski yt-dlp ishlamaydi

**Yechim:** requirements.txt da versiyani yangilash:
```
yt-dlp>=2025.01.01
```

### 4. Instagram cookies kerak
**Sabab:** Instagram ba'zi videolar uchun login talab qiladi

**Yechim:** COOKIES_CONTENT environment variable qo'shish

## Tezkor Tavsiyalar

### A. Render Logs Tekshirish (ENG MUHIM!)
1. Dashboard.render.com ga kiring
2. Botni oching
3. Logs tabini oching
4. Botga Instagram link yuboring
5. Logda qanday xatolik ko'rinishini qarang

**Kuchli ehtimollik:**
- `HTTP Error 403` - cookies kerak
- `No video formats` - URL noto'g'ri yoki video private
- `Sign in to confirm` - login kerak
- Fayl topilmadi - download xatosi

### B. Lokal Bot To'xtatish
Agar siz lokal kompyuterda `python bot.py` ishlatgan bo'lsangiz:
1. Terminal/CMD ni toping
2. `Ctrl+C` bosing
3. Bot to'xtaydi
4. Faqat Render.com dagi bot ishlaydi

### C. Telegram Test
1. Telegram da botga `/start` yuboring
2. Instagram **public** post linkini yuboring (masalan: https://www.instagram.com/reel/...)
3. Video/Audio tanlang
4. Natijani kuting

**Natijalar:**
- ✅ Video keldi - hammasi to'g'ri!
- ⏳ "Yuklanmoqda" deb aytdi lekin hech narsa kelmadi - Render Logs tekshiring
- ❌ Xatolik xabari - xatolik matnini yuboring
- 🔇 Hech javob bermadi - Bot ishlamayapti (Conflict yoki Failed)

## Keyingi Qadam

**RENDER LOGS NI TEKSHIRING!**

Bu eng muhim qadam. Logs sizga aniq nima xatolik ekanligini ko'rsatadi.

### Logs da qanday xatolik ko'rsatadi?

Menga ayting yoki screenshot yuboring:
1. Render.com Logs screenshot
2. Telegram da bot qanday javob berdi
3. Qaysi platformadan link yubordingiz (Instagram/TikTok/Facebook)

---

## Tez Yechim (Agar hali ham ishlamasa)

Keling, `yt-dlp` versiyasini yangilab, `requirements.txt` ni yaxshilaymiz:

```txt
python-telegram-bot[job-queue]>=20.0
yt-dlp>=2025.01.01
requests>=2.31.0
```

Va `build.sh` ni tekshiramiz:
```bash
#!/usr/bin/env bash
apt-get update && apt-get install -y ffmpeg
pip install --upgrade pip
pip install --upgrade yt-dlp
pip install -r requirements.txt
```

GitHub ga push qilamiz:
```bash
git add .
git commit -m "yt-dlp va build.sh yangilandi"
git push origin main
```

Render.com avtomatik deploy qiladi.

---

**SAVOL:** Render.com Logs da nima ko'rsatilgan?
