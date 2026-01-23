#!/usr/bin/env bash
# Install FFmpeg for video/audio processing
apt-get update && apt-get install -y ffmpeg

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
