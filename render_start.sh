#!/usr/bin/env bash
set -e

# Start keepalive in background to respond to health checks
python keepalive.py &

# Start the bot
python bot.py
