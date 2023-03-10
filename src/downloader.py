import os

def download_songs(config,url,playlist):

    # Path to the executable
    yt_dlp_path = config["yt-dlp-path"]

    # Get options for running the downloader
    settings = ["-x","--audio-format mp3", "--embed-metadata", "-o \"%(title)s.mp3\""]
    # Add the playlist option
    if playlist:
        settings.append("--yes-playlist")
    download_path = config["downloaded_folder"]

    # Create the command
    command = [yt_dlp_path," ".join(settings), "--path " + download_path, " " + url]

    # Before downloading any files, get all files currently in the download folder
    files_in_folder_before = os.listdir(download_path)

    # Run the command
    os.system(" ".join(command))

    os.system("fs")

    # Afte downloading, get all files in downloadfolder again - get newly added ones and return their names
    files_in_folder_after = os.listdir(download_path)

    new_files = list(set(files_in_folder_after).symmetric_difference(set(files_in_folder_before)))

    # Remove all files from the new files that aren't mp3's
    new_files = list(filter(lambda name: name[-4:] == ".mp3",new_files))

    return new_files

