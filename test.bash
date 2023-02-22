#!/bin/bash


# load .env
export $(cat .env | xargs)

# make shure specified Download folder exists
mkdir $DOWNLOAD_FOLDER  > /dev/null 2>&1

# start by downloading some music as a test
./yt-dlp -x --audio-format mp3 --embed-metadata --paths $DOWNLOAD_FOLDER -o "%(title)s.mp3" https://music.youtube.com/watch?v=ikIcl2q3oP8

# next EQ the file to boos the bass
ffmpeg -i 'Skrillex, PinkPantheress & Trippie Redd - Way Back [Official Audio].mp3' -af "equalizer=f=10125:width_type=h:width=9875:g=-50" output.mp3
