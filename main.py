import json

import downloader
  
# Open Config File
config_f = open('config.json')
  
# Load config file as JSON
config = json.load(config_f)

downloader.download_song(config, "")