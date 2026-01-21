import os
import re
import glob
import asyncio
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from yt_dlp import YoutubeDL
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import Conflict
import sys
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time

# ====== LOGGING SETUP ======
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ====== CONFIG ======
BOT_TOKEN = os.getenv("BOT_TOKEN", "8519182993:AAHsPvVInLwtKfsYbyKlxWecmej0acT-13s")  # Fallback to hardcoded for local testing
DOWNLOAD_DIR = "downloads"
MAX_SIZE = 49 * 1024 * 1024  # 49MB

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Thread pool for blocking operations
executor = ThreadPoolExecutor(max_workers=4)

# ====== HELPER FUNCTIONS ======
def escape_markdown(text: str) -> str:
    """Escape special characters for Telegram MarkdownV2"""
    # For Markdown (not MarkdownV2), we need to escape: _ * [ ] ( ) ~ ` > # + - = | { } . !
    # But for basic Markdown mode, we mainly need to escape _ and *
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in escape_chars:
        text = text.replace(char, '\\' + char)
    return text

def format_file_size(size_bytes: int) -> str:
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f}TB"

# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Video yuklash", callback_data="download")],
        [InlineKeyboardButton("ℹ️ Yordam", callback_data="help")]
    ]
    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "🤖 *Yuklauz7\\_bot*\n\n"
        "📥 Instagram, YouTube, TikTok va Facebook videolarini\n"
        "*original ovozi bilan* yuklab beraman.\n\n"
        "👇 Tugmalardan foydalaning yoki video link yuboring.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ====== DEBUG ======
async def debug_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in [604138676, 5636041300]: # O'zingizning ID raqamingizni ham qo'shishingiz mumkin
        pass
        
    # Check cookies
    cookie_status = "❌ Yo'q"
    if os.path.exists("cookies.txt"):
        size = os.path.getsize("cookies.txt")
        cookie_status = f"✅ Bor ({size} bytes)"
    
    # Check env
    env_content = os.getenv("COOKIES_CONTENT")
    env_status = "❌ Yo'q"
    if env_content:
        env_status = f"✅ Bor ({len(env_content)} chars)"
        
    await update.message.reply_text(
        f"🛠 *Debug Info*\n\n"
        f"🍪 Cookies fayl: {cookie_status}\n"
        f"🌐 Env Var: {env_status}\n"
        f"📂 Download dir: {len(glob.glob(os.path.join(DOWNLOAD_DIR, '*')))} items",
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

    elif query.data == "download":
        await query.edit_message_text(
            "🔗 Video havolasini yuboring\n\n"
            "Instagram | YouTube | TikTok | Facebook"
        )

# ====== URL CHECK ======
def is_valid_url(url: str) -> bool:
    pattern = r"(instagram\.com|tiktok\.com|youtube\.com|youtu\.be|facebook\.com|fb\.watch|shorts)"
    return bool(re.search(pattern, url, re.IGNORECASE))

def is_youtube_url(url: str) -> bool:
    pattern = r"(youtube\.com|youtu\.be)"
    return bool(re.search(pattern, url, re.IGNORECASE))

# ====== CLEANUP ======
def cleanup_downloads():
    """Downloads papkasidagi barcha fayllarni tozalash"""
    files = glob.glob(os.path.join(DOWNLOAD_DIR, "*"))
    for f in files:
        try:
            if os.path.isfile(f):
                os.remove(f)
                logger.debug(f"Tozalandi: {f}")
        except Exception as e:
            logger.warning(f"Faylni o'chirib bo'lmadi {f}: {e}")

# ====== PROGRESS HOOK ======
class DownloadProgress:
    def __init__(self):
        self.last_update = None
        
    def hook(self, d):
        """yt-dlp progress hook"""
        if d['status'] == 'downloading':
            # Log progress periodically
            if self.last_update is None or (datetime.now() - self.last_update).seconds >= 5:
                percent = d.get('_percent_str', 'N/A')
                speed = d.get('_speed_str', 'N/A')
                logger.info(f"Yuklanmoqda: {percent} @ {speed}")
                self.last_update = datetime.now()
        elif d['status'] == 'finished':
            logger.info(f"Yuklash tugadi: {d.get('filename', 'N/A')}")

# ====== SYNC DOWNLOAD FUNCTION ======
def sync_download(url: str, user_id: int) -> dict:
    """
    Sinxron yuklab olish funksiyasi - threadda ishlaydi
    """
    logger.info(f"Download boshlandi: {url} (user: {user_id})")
    
    # Unique filename uchun user_id ishlatiladi
    output_template = os.path.join(DOWNLOAD_DIR, f"{user_id}_%(title).50s.%(ext)s")
    
    # Progress hook
    progress = DownloadProgress()
    
    # YouTube uchun maxsus sozlamalar
    if is_youtube_url(url):
        ydl_opts = {
            "outtmpl": output_template,
            # UNIVERSAL FORMAT: Har qanday video uchun ishlaydi
            # Eng yaxshi sifat (audio bilan), agar yo'q bo'lsa merge qiladi
            "format": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]/best",
            "merge_output_format": "mp4",
            # Postprocessor OLIB TASHLANDI - tezlik uchun
            "quiet": False,
            "no_warnings": False,
            "noplaylist": True,
            "extract_flat": False,
            
            # 2026 YANGILANGAN: YouTube player extraction fix
            "extractor_args": {
                "youtube": {
                    # Eng ishonchli clientlar (2026)
                    "player_client": ["ios", "android", "web"],
                    # PO Token (recommended for bot detection bypass)
                    "player_skip": ["webpage", "configs"],
                }
            },
            
            # Optimized HTTP headers
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            },
            # Reduced retries for speed
            "retries": 5,
            "fragment_retries": 5,
            "extractor_retries": 3,
            # Longer timeout for YouTube
            "socket_timeout": 30,
            # Progress hook
            "progress_hooks": [progress.hook],
        }
    else:
        # Boshqa saytlar uchun (Instagram, TikTok, Facebook)
        ydl_opts = {
            "outtmpl": output_template,
            # TEZLIK OPTIMIZATSIYASI: past sifat, tez yuklash
            "format": "best[height<=360][ext=mp4]/best[height<=480]/best",
            "merge_output_format": "mp4",
            # Postprocessor OLIB TASHLANDI - tezlik uchun
            "quiet": False,
            "no_warnings": False,
            "noplaylist": True,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            },
            # Reduced retries for speed
            "retries": 3,
            "socket_timeout": 20,
            "progress_hooks": [progress.hook],
        }

    # Cookies qo'shish (Umumiy)
    if os.path.exists("cookies.txt"):
        ydl_opts["cookiefile"] = "cookies.txt"
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # Filepath olish - bir nechta usullar
            filepath = None
            
            # Usul 1: requested_downloads
            if info.get("requested_downloads"):
                filepath = info["requested_downloads"][0].get("filepath")
                logger.debug(f"Filepath (method 1): {filepath}")
            
            # Usul 2: _filename
            if not filepath and info.get("_filename"):
                filepath = info["_filename"]
                logger.debug(f"Filepath (method 2): {filepath}")
            
            # Usul 3: prepare_filename
            if not filepath:
                filepath = ydl.prepare_filename(info)
                logger.debug(f"Filepath (method 3): {filepath}")
                # Agar merge bo'lgan bo'lsa, mp4 bo'ladi
                base, ext = os.path.splitext(filepath)
                if ext != ".mp4":
                    possible_mp4 = base + ".mp4"
                    if os.path.exists(possible_mp4):
                        filepath = possible_mp4
                        logger.debug(f"Filepath corrected to: {filepath}")
            
            # Usul 4: Downloads papkasidan izlash
            if not filepath or not os.path.exists(filepath):
                logger.warning("Filepath topilmadi, downloads papkasidan qidirilmoqda...")
                pattern = os.path.join(DOWNLOAD_DIR, f"{user_id}_*")
                files = glob.glob(pattern)
                if files:
                    # Eng yangi faylni olish
                    filepath = max(files, key=os.path.getctime)
                    logger.info(f"Filepath topildi (method 4): {filepath}")
            
            if not filepath or not os.path.exists(filepath):
                logger.error(f"Fayl topilmadi. Info keys: {info.keys()}")
                raise FileNotFoundError(f"Yuklangan fayl topilmadi. URL: {url}")
            
            logger.info(f"Download muvaffaqiyatli: {filepath}")
            
            return {
                "filepath": filepath,
                "title": info.get("title", "Video"),
                "duration": info.get("duration", 0),
                "filesize": os.path.getsize(filepath),
            }
    except Exception as e:
        logger.error(f"Download xatoligi: {str(e)}", exc_info=True)
        raise

# ====== DOWNLOAD ======
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    user_id = update.effective_user.id
    
    logger.info(f"Video so'rovi: {url} (user: {user_id})")

    if not is_valid_url(url):
        await update.message.reply_text(
            "❌ Noto'g'ri link yuborildi.\n\n"
            "Qo'llab-quvvatlanadigan: Instagram, YouTube, TikTok, Facebook"
        )
        return

    status = await update.message.reply_text("⏳ Yuklanmoqda, kuting...")
    filepath = None

    try:
        # Oldingi fayllarni tozalash
        cleanup_downloads()
        
        # YouTube uchun maxsus xabar
        if is_youtube_url(url):
            await status.edit_text(
                "⏳ YouTube dan yuklanmoqda...\n\n"
                "⚠️ Bu biroz vaqt olishi mumkin."
            )
        
        # Threadda sinxron yuklash
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(executor, sync_download, url, user_id)
        
        filepath = result["filepath"]
        
        # Fayl hajmini tekshirish
        file_size = result["filesize"]
        if file_size > MAX_SIZE:
            os.remove(filepath)
            await status.edit_text(
                f"⚠️ Video hajmi {format_file_size(file_size)}\n\n"
                f"Telegram limiti: {format_file_size(MAX_SIZE)}"
            )
            logger.warning(f"Fayl hajmi katta: {file_size} bytes")
            return
        
        # Videoni yuborish
        await status.edit_text("📤 Video yuborilmoqda...")
        
        # Title'ni tozalash - BARCHA maxsus belgilarni olib tashlash
        safe_title = result['title'][:50]
        # Remove ALL non-ASCII and special characters to avoid Telegram parsing errors
        safe_title = ''.join(char for char in safe_title if char.isalnum() or char.isspace())
        safe_title = safe_title.strip()
        
        # If title is empty after cleaning, use default
        if not safe_title:
            safe_title = "Video"
        
        with open(filepath, "rb") as video_file:
            await update.message.reply_video(
                video=video_file,
                caption=f"✅ {safe_title}\n\n@Yuklauz7_bot",
                # NO parse_mode - plain text only
                read_timeout=120,
                write_timeout=120,
            )
        
        await status.delete()
        logger.info(f"Video muvaffaqiyatli yuborildi: {filepath}")

    except FileNotFoundError as e:
        error_msg = f"❌ Fayl topilmadi:\n{str(e)}"
        await status.edit_text(error_msg)
        logger.error(error_msg)
    
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Download xatoligi: {error_msg}", exc_info=True)
        
        # Xatolik turlarini ajratish
        if "Sign in to confirm" in error_msg or ("bot" in error_msg.lower() and "youtube" in url.lower()):
            await status.edit_text(
                "❌ YouTube bot detection!\n\n"
                "⚠️ YouTube hozirda qo'shimcha tekshiruv talab qilmoqda.\n\n"
                "✅ Instagram, TikTok va Facebook ishlaydi."
            )
        elif "Video unavailable" in error_msg or "Private video" in error_msg:
            await status.edit_text("❌ Video mavjud emas yoki yopiq (private).")
        elif "age" in error_msg.lower() or "age-restricted" in error_msg.lower():
            await status.edit_text("❌ Yosh cheklovi bor, yuklab bo'lmaydi.")
        elif "copyright" in error_msg.lower():
            await status.edit_text("❌ Mualliflik huquqi tufayli yuklab bo'lmaydi.")
        elif "format" in error_msg.lower() or "No video formats" in error_msg:
            await status.edit_text("❌ Video formati qo'llab-quvvatlanmaydi.")
        elif "HTTP Error 403" in error_msg or "HTTP Error 429" in error_msg:
            await status.edit_text("❌ Server ruxsat bermadi. Keyinroq urinib ko'ring.")
        elif "network" in error_msg.lower() or "connection" in error_msg.lower():
            await status.edit_text("❌ Tarmoq xatoligi. Internetni tekshiring.")
        else:
            # Qisqa xatolik xabari
            short_error = error_msg[:200] if len(error_msg) > 200 else error_msg
            await status.edit_text(f"❌ Xatolik:\n{short_error}")
    
    finally:
        # Faylni tozalash
        if filepath and os.path.exists(filepath):
            try:
                os.remove(filepath)
                logger.debug(f"Fayl tozalandi: {filepath}")
            except Exception as e:
                logger.warning(f"Faylni o'chirib bo'lmadi: {e}")

# ====== ERROR HANDLER ======
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Global xatolik handler"""
    logger.error(f"Global xatolik: {context.error}", exc_info=context.error)

# ====== HEALTH CHECK HTTP SERVER ======
class HealthCheckHandler(BaseHTTPRequestHandler):
    """HTTP health check endpoint - UptimeRobot uchun"""
    
    def do_GET(self):
        """GET request handler"""
        if self.path == '/' or self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            status = {
                "status": "ok",
                "bot": "Yuklauz7_bot",
                "uptime": time.time() - start_time,
                "timestamp": datetime.now().isoformat()
            }
            self.wfile.write(str(status).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        """Suppress HTTP server logs"""
        pass

def run_health_check_server():
    """Health check HTTP server ni alohida threadda ishga tushirish"""
    port = int(os.getenv('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    logger.info(f"[HEALTH] HTTP server ishga tushdi: http://0.0.0.0:{port}")
    server.serve_forever()

# ====== KEEP-ALIVE MECHANISM ======
start_time = time.time()

async def keep_alive_ping(context: ContextTypes.DEFAULT_TYPE):
    """
    Har 5 daqiqada bir marta bot aktiv ekanligini log qiladi.
    Bu Render.com va boshqa platformalarda botni uyquga ketishdan saqlaydi.
    """
    uptime_hours = (time.time() - start_time) / 3600
    logger.info(f"🔄 Keep-alive ping: Bot aktiv va ishlayapti | Uptime: {uptime_hours:.2f} soat")

# ====== MAIN ======
def main():
    global start_time
    start_time = time.time()
    
    logger.info("=" * 50)
    logger.info("Yuklauz7_bot ishga tushmoqda...")
    logger.info("=" * 50)
    
    # HTTP Health Check Server ni alohida threadda ishga tushirish
    health_thread = threading.Thread(target=run_health_check_server, daemon=True)
    health_thread.start()
    logger.info("[HEALTH] Health check server thread boshlandi")
    
    # COOKIES SETUP
    cookies_content = os.getenv("COOKIES_CONTENT")
    if cookies_content:
        try:
            with open("cookies.txt", "w", encoding='utf-8') as f:
                f.write(cookies_content)
            logger.info("✅ Cookies fayli yaratildi (Env Var dan)")
        except Exception as e:
            logger.error(f"❌ Cookies faylini yaratishda xatolik: {e}")
    elif os.path.exists("cookies.txt"):
        logger.info("✅ Cookies fayli topildi (fayl tizimdan)")
    else:
        logger.warning("⚠️ Cookies topilmadi! Instagram/YouTube login xatosi berishi mumkin.")
    
    # Clear any existing webhooks/sessions before starting
    try:
        import requests
        logger.info("Telegram webhook va sessiyalarni tozalash...")
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook?drop_pending_updates=true"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logger.info("Webhook muvaffaqiyatli tozalandi")
        else:
            logger.warning(f"Webhook tozalashda xatolik: {response.text}")
    except Exception as e:
        logger.warning(f"Webhook tozalashda xatolik (davom etamiz): {e}")
    
    # Application yaratish - timeout vaqtlarini oshirdik
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .read_timeout(120)      # 60 -> 120 sekund
        .write_timeout(120)     # 60 -> 120 sekund
        .connect_timeout(60)    # 30 -> 60 sekund
        .pool_timeout(60)       # Yangi: connection pool timeout
        .build()
    )

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("debug", debug_bot))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    
    # Error handler
    app.add_error_handler(error_handler)

    # Keep-alive job - har 5 daqiqada ishga tushadi
    from telegram.ext import JobQueue
    job_queue = app.job_queue
    job_queue.run_repeating(keep_alive_ping, interval=300, first=60)  # 300 sekund = 5 daqiqa

    logger.info("[BOT] Yuklauz7_bot ishga tushdi!")
    logger.info("[INFO] Qo'llab-quvvatlanadi: Instagram, YouTube, TikTok, Facebook")
    logger.info("[KEEP-ALIVE] Har 5 daqiqada ping yuboriladi")
    logger.info("[24/7] HTTP health check endpoint faol")
    logger.info("[24/7] UptimeRobot uchun tayyor: http://0.0.0.0:8080/health")
    
    # Polling boshlash - auto-restart bilan
    try:
        app.run_polling(drop_pending_updates=True)
    except Conflict:
        logger.critical("[STOP] Bot boshqa joyda ishga tushirildi (Conflict)!")
        logger.critical("Iltimos, eski botni yoki Render dagi botni o'chiring.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"[ERROR] Polling xatolik: {e}", exc_info=True)
        logger.info("[RESTART] 5 soniyadan keyin qayta ishga tushirish...")
        time.sleep(5)
        main()  # Rekursiv restart

if __name__ == "__main__":
    main()