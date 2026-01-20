# Yuklauz7_bot - Telegram Video Downloader

Telegram bot for downloading videos from Instagram, YouTube, TikTok, and Facebook with original audio.

## Features

- 📥 Download videos from multiple platforms
- 🎵 Preserves original audio
- 🚀 Fast and reliable
- 📊 Detailed logging
- ⚡ Async/await architecture
- 🛡️ Robust error handling

## Supported Platforms

- YouTube (including Shorts)
- Instagram
- TikTok
- Facebook

## Requirements

- Python 3.12+
- FFmpeg
- See `requirements.txt` for Python dependencies

## Local Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install FFmpeg:
   - Windows: `winget install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`
4. Set your bot token in `yuklauz7_bot.py` (line 31)
5. Run the bot:
   ```bash
   python yuklauz7_bot.py
   ```

## Deploy to Render

1. Fork/upload this repository to GitHub
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Render will automatically detect the configuration
5. Add environment variable:
   - Key: `BOT_TOKEN`
   - Value: Your Telegram bot token from [@BotFather](https://t.me/BotFather)
6. Deploy!

### Render Configuration

The following files configure Render deployment:

- `Procfile` - Defines the start command
- `runtime.txt` - Specifies Python version
- `build.sh` - Installs FFmpeg during build
- `requirements.txt` - Python dependencies

## Environment Variables

For production deployment, set these environment variables:

- `BOT_TOKEN` - Your Telegram bot token (required)

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send a video URL from any supported platform
4. Wait for the bot to download and send the video

## Limitations

- Maximum file size: 50MB (Telegram limit)
- Video quality: Up to 720p (to stay within size limits)
- Private/age-restricted videos may not work

## Keep-Alive Mechanism

⚠️ **MUHIM: Bepul hosting platformalarda bot 10-15 daqiqadan keyin "uxlashi" mumkin!**

### Yechimlar:

1. **Keep-alive mexanizmi** - Bot har 5 daqiqada avtomatik ping yuboradi
2. **Railway.app** - Oyiga 5$ kredit bepul (tavsiya etiladi)
3. **Render.com** - Free plan: 15 daqiqadan keyin inactive bo'ladi
4. **Koyeb.com** - Bepul va doimo aktiv (eng yaxshi variant!)

### Deployment platformalari:

| Platform | Bepul plan | Keep-alive | Tavsiya |
|----------|-----------|------------|---------|
| **Koyeb** | ✅ Ha | ✅ Doimo aktiv | ⭐⭐⭐⭐⭐ |
| **Railway** | ✅ 5$/oy | ✅ Yaxshi | ⭐⭐⭐⭐ |
| **Render** | ✅ Ha | ⚠️ 15 min keyin uxlaydi | ⭐⭐⭐ |
| **Heroku** | ❌ Yo'q | - | ❌ |

## Logging

All bot activity is logged to `bot.log` for debugging and monitoring.

## License

MIT License

## Author

@Yuklauz7_bot
