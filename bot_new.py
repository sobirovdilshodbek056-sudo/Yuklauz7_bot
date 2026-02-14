import os
import asyncio
import logging
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError

# Configuration from environment variables
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
SESSION = os.getenv("SESSION", "yuklauz7_session")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main bot function with automatic reconnection."""
    client = TelegramClient(SESSION, API_ID, API_HASH)
    
    try:
        await client.start(bot_token=BOT_TOKEN)
        logger.info("✅ Bot connected successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        raise

    @client.on(events.NewMessage(pattern="/start"))
    async def handle_start(event):
        await event.reply("🤖 Bot is alive!")

    @client.on(events.NewMessage())
    async def handle_message(event):
        if event.is_private:
            await event.reply(event.raw_text)

    await client.run_until_disconnected()

async def run_with_reconnect():
    """Run bot with automatic reconnection for 24/7 uptime."""
    reconnect_delay = 5
    while True:
        try:
            await main()
        except FloodWaitError as e:
            logger.warning(f"⏱️ FloodWait: sleeping for {e.seconds} seconds")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            logger.error(f"❌ Connection error: {e}")
            logger.info(f"Reconnecting in {reconnect_delay} seconds...")
            await asyncio.sleep(reconnect_delay)

if __name__ == "__main__":
    try:
        logger.info("🚀 Starting Yuklauz7 Bot...")
        
        if not BOT_TOKEN:
            logger.error("❌ BOT_TOKEN is not set in environment variables!")
            exit(1)
        
        logger.info(f"Configuration: API_ID={API_ID}, SESSION={SESSION}")
        asyncio.run(run_with_reconnect())
        
    except KeyboardInterrupt:
        logger.info("⛔ Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        exit(1)
