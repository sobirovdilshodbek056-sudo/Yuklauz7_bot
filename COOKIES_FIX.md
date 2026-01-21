# 🍪 Instagram va YouTube "Login" Xatolarini Tuzatish

Agar botingizda quyidagi xatolar chiqayotgan bo'lsa:
*   **Instagram:** "Login required", "Rate-limit reached"
*   **YouTube:** "Sign in to confirm", "Bot detection"

Buni yechimi bitta: **Cookies** (ruxsatnoma) qo'shish kerak.

## 1. Cookies olish (Kompyuterda)

Sizga bitta faylda ham Instagram, ham YouTube cookielari kerak.

1.  Chrome brauzerini oching.
2.  **Instagram.com** ga kiring va login qiling (akkauntingiz ochiq tursin).
3.  **YouTube.com** ga kiring va login qiling (Google akkauntingiz bilan).
4.  Chrome Web Store dan **"Get cookies.txt LOCALLY"** kengaytmasini o'rnating.
    *   [Havola](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflccgommaphmhe)
5.  **Instagram** sahifasida turib extensionni bosing va **"Export"** qiling. (`instagram.txt`)
6.  **YouTube** sahifasida turib extensionni bosing va **"Export"** qiling. (`youtube.txt`)
7.  Ikkala faylni oching (Notepad da).
8.  Ikkinchi fayldagi matnni nusxalab, birinchi faylning oxiriga tashlang (bitta katta fayl qiling).

> **Alternativ:** Agar extension barcha ochiq tablar uchun export qilsa, shunchaki bitta katta fayl olasiz.

Maksad: Qo'lingizda shunday matn bo'lsin-ki, ichida `.instagram.com` ham, `.youtube.com` ham bor bo'lsin.

## 2. Render ga joylash

1.  Hosil bo'lgan uzun matnni nusxalab oling.
2.  **Render Dashboard** ga kiring.
3.  Botingizni tanlang (`yuklauz7-bot`).
4.  **Environment** bo'limiga o'ting.
5.  Agar oldin `COOKIES_CONTENT` qo'shgan bo'lsangiz, "Edit" qiling. Yo'q bo'lsa "Add Environment Variable":
    *   **Key:** `COOKIES_CONTENT`
    *   **Value:** (Boyagi umumiy, uzun matn)
6.  **"Save Changes"** tugmasini bosing.

Render qayta deploy qiladi. Endi Instagram ham, YouTube ham ishlaydi! 🚀
