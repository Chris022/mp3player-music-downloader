#!/bin/bash

apt update

# install ffmpeg
apt install ffmpeg

# install python3
apt install python3

# start by making yt-dlp executable
chmod +x ./yt-dlp