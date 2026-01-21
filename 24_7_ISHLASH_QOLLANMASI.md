# 🤖 Render da 24/7 Ishlatish Bo'yicha Qo'llanma

Render.com **bepul (free)** versiyasida veb-servislar **15 daqiqa** harakatsizlikdan so'ng avtomatik ravishda "uxlab qoladi" (spin down). Bu sizning botingiz ishlashdan to'xtashini anglatadi.

Buni oldini olish va botni **24/7** ishlatish uchun quyidagi qadamlarni bajaring.

## ✅ 1. Kodlar Yangilandi
Men loyihangizdagi `render.yaml` va `Procfile` fayllarini to'g'irladim:
- Bot endi **"Web Service"** sifatida ishlaydi.
- Bot ichida **maxsus HTTP server** (`/health`) yoqilgan.

## 🚀 2. UptimeRobot Sozlash (SHART)
Botingiz uxlab qolmasligi uchun unga har 5 daqiqada tashqaridan "signal" (ping) berib turish kerak. Buni **UptimeRobot** bepul servisi orqali qilamiz.

### Qadamlar:

1.  **[UptimeRobot.com](https://uptimerobot.com/)** saytiga kiring va ro'yxatdan o'ting (Register).
2.  Log in qilgandan so'ng, **"Add New Monitor"** tugmasini bosing.
3.  Quyidagi sozlamalarni kiriting:
    *   **Monitor Type:** `HTTP(s)` ni tanlang.
    *   **Friendly Name:** `Yuklauz7 Bot` (yoki xohlagan nom).
    *   **URL (or IP):** Render bergan sayt manzili, oxiriga `/health` qo'shing.
        *   *Misol uchun:* `https://yuklauz7-bot.onrender.com/health`
        *   **MUHIM:** Render dashboardingizdan botingizning aniq URL manzilini oling!
    *   **Monitoring Interval:** `5 minutes` (yoki `10 minutes`).
    *   **Monitor Timeout:** `30 seconds` (o'zgarishsiz qoldiring).
4.  **"Create Monitor"** tugmasini bosing.

## 🎯 Natija
Endi UptimeRobot har 5 daqiqada sizning botingizga kirib turadi. Bu Renderga "bot ishlatilyapti" degan signal beradi va Render uni o'chirmaydi.

### Tekshirish:
Render Dashboard da **Logs** bo'limiga kiring. Har 5 daqiqada quyidagi yozuvni ko'rishingiz kerak:
`GET /health HTTP/1.1 200`

Bu bot muvaffaqiyatli uyg'oq turganini bildiradi!
