# README - Render Deployment (24/7)

## Setup

1. **Create Render account:** https://render.com
2. **Connect GitHub repo** to Render
3. **Set environment variables** in Render dashboard:
   - `API_ID` — Telegram App ID
   - `API_HASH` — Telegram App Hash
   - `BOT_TOKEN` — Telegram Bot Token
   - `OWNER_ID` — Your Telegram User ID

## How it works

- `render-manifest.yaml` defines the service (starter plan for always-on)
- `render_start.sh` starts both `keepalive.py` (health check) and `bot.py` (bot)
- `keepalive.py` responds to `/health` requests to keep the service alive
- `bot.py` runs with automatic reconnection on errors

## Deploy

1. Push to GitHub
2. Render auto-deploys (if `autoDeploy: true`)
3. Or manually deploy from Render dashboard

## Monitor

- Check logs: Render Dashboard → Service → Logs
- Health check: `curl https://<your-service-url>/health`
