# 🍪 Instagram "Login Required" Xatosini Tuzatish

Agar botingizda **"Requested content is not available, rate-limit reached or login required"** xatosi chiqayotgan bo'lsa, bu Instagram botni bloklayotganini bildiradi. Buni tuzatish uchun botga **Cookies** (pechenyalar) kerak.

## 1. Cookies olish (Kompyuterda)

Sizga Instagram ga kirgan brauzeringizdan cookielarni olishingiz kerak.

1.  Chrome yoki Edge brauzerini oching va **Instagram.com** ga kiring (logindan o'tgan bo'lishingiz shart).
2.  Chrome Web Store dan **"Get cookies.txt LOCALLY"** kengaytmasini (extension) o'rnating.
    *   [Havola](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflccgommaphmhe)
3.  Instagram sahifasida turib, o'sha extension tugmasini bosing.
4.  **"Export"** tugmasini bosing.
5.  Sizga `instagram.com_cookies.txt` (yoki shunga o'xshash) fayl yuklanadi.
6.  Faylni oching (NotePad da). Ichidagi **hamma matnni nusxalab oling**.

## 2. Render ga joylash

Biz bu maxfiy ma'lumotni kodingizga qo'shmaymiz (xavfsizlik uchun), balki Render Environment Variable ga qo'shamiz.

1.  **Render Dashboard** ga kiring.
2.  Botingizni tanlang (`yuklauz7-bot`).
3.  Chap menyudan **"Environment"** tugmasini bosing.
4.  **"Add Environment Variable"** tugmasini bosing.
5.  Quyidagilarni kiriting:
    *   **Key:** `COOKIES_CONTENT`
    *   **Value:** (Boyagi nusxalab olgan uzun matnni shu yerga tashlang)
6.  **"Save Changes"** tugmasini bosing.

Render avtomatik ravishda qayta deploy qiladi. Deploy tugagach, Instagram yana ishlashni boshlaydi! ✅
