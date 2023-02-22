import json
import os

import src.downloader as downloader
import src.processor as processor
  
# Open Config File
config_f = open('config.json')
  
# Load config file as JSON
config = json.load(config_f)

# Download a Song
downloaded_files = downloader.download_songs(config, "",False)

# Get difference between files in downloaded_folder and processed_folder
# Process all files that are in downloaded_folder but not in processed_folder
downloaded_files = os.listdir(config["downloaded_folder"])
processed_files = os.listdir(config["processed_folder"])
unprocessed_files = list(set(downloaded_files).difference(processed_files))

# Remove all files that aren't mp3's from the list
unprocessed_files = list(filter(lambda name: name[-4:] == ".mp3",unprocessed_files))

# Apply EQ to new downloaded songs
for unprocessed_file in unprocessed_files:
    processor.EQ_song(config, unprocessed_file)