#!/usr/bin/env python3
"""
Instagram yuklab olishni test qilish
"""
import os
import sys
from yt_dlp import YoutubeDL

# Test URL - public Instagram reel/post
TEST_URL = "https://www.instagram.com/reel/C2VxqZ-yPeM/"  # Public reel

print("=" * 60)
print("INSTAGRAM DOWNLOAD TEST")
print("=" * 60)

# yt-dlp versiyasini tekshirish
try:
    import yt_dlp
    print(f"[OK] yt-dlp versiyasi: {yt_dlp.version.__version__}")
except:
    print("[WARNING] yt-dlp versiyasi aniqlanmadi")

# Test download
print(f"\n🔍 Test URL: {TEST_URL}")
print("📥 Yuklanmoqda...\n")

ydl_opts = {
    "quiet": False,
    "no_warnings": False,
    "format": "bestvideo[height<=480]+bestaudio/best[height<=480]",
    "merge_output_format": "mp4",
    "outtmpl": "test_video.%(ext)s",
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    },
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        print("📊 Ma'lumot olish...")
        info = ydl.extract_info(TEST_URL, download=True)
        
        print("\n" + "=" * 60)
        print("✅ MUVAFFAQIYATLI!")
        print("=" * 60)
        print(f"📹 Sarlavha: {info.get('title', 'N/A')}")
        print(f"⏱️ Davomiyligi: {info.get('duration', 0)} soniya")
        print(f"👤 Muallif: {info.get('uploader', 'N/A')}")
        print(f"📁 Fayl: test_video.mp4")
        
        # File size
        if os.path.exists("test_video.mp4"):
            size = os.path.getsize("test_video.mp4")
            print(f"💾 Hajmi: {size / (1024*1024):.2f} MB")
        
except Exception as e:
    print("\n" + "=" * 60)
    print("❌ XATOLIK!")
    print("=" * 60)
    print(f"📛 Xatolik: {str(e)}")
    print("\n🔍 Batafsil:")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("TEST TUGADI")
print("=" * 60)
