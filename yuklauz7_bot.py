import os
import re
import asyncio
from yt_dlp import YoutubeDL
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters
)

BOT_TOKEN = "8519182993:AAEqQyQ-8kretAf67crR5VCohQuPVEZGivg"
DOWNLOAD_DIR = "downloads"
MAX_SIZE = 49 * 1024 * 1024  # 49MB (Telegram limitdan past)

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Video yuklash", callback_data="download")],
        [InlineKeyboardButton("ℹ️ Yordam", callback_data="help")]
    ]
    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "🤖 *Yuklauz7_bot*\n\n"
        "📥 Instagram, YouTube, TikTok va Facebook videolarini\n"
        "*original ovozi bilan* yuklab beraman.\n\n"
        "👇 Tugmalardan foydalaning yoki video link yuboring.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ====== BUTTONS ======
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        await query.edit_message_text(
            "📌 *Qanday ishlaydi?*\n\n"
            "1️⃣ Video linkni yuboring\n"
            "2️⃣ Kuting ⏳\n"
            "3️⃣ Video tayyor ✅\n\n"
            "⚠️ Private akkaunt videolari yuklanmaydi.",
            parse_mode="Markdown"
        )

    if query.data == "download":
        await query.edit_message_text(
            "🔗 Video havolasini yuboring\n\n"
            "Instagram | YouTube | TikTok | Facebook"
        )

# ====== LINK CHECK ======
def is_valid_url(url: str):
    pattern = r"(instagram\.com|tiktok\.com|youtube\.com|facebook\.com|fb\.watch)"
    return re.search(pattern, url)

# ====== DOWNLOAD ======
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    if not is_valid_url(url):
        await update.message.reply_text("❌ Noto‘g‘ri link!\nIltimos, video link yuboring.")
        return

    status = await update.message.reply_text("⏳ Yuklanmoqda, kuting...")

    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "format": "mp4/best",
        "merge_output_format": "mp4",
        "quiet": True,
        "noplaylist": True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        if os.path.getsize(filename) > MAX_SIZE:
            os.remove(filename)
            await status.edit_text("⚠️ Video hajmi juda katta (50MB dan oshdi).")
            return

        await update.message.reply_video(
            video=open(filename, "rb"),
            caption="✅ Video tayyor\n@Yuklauz7_bot"
        )

        os.remove(filename)

    except Exception as e:
        await status.edit_text("❌ Xatolik yuz berdi.\nBoshqa link bilan urinib ko‘ring.")

# ====== MAIN ======
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if name == "main":
    main()