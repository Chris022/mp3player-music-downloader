import os


def EQ_song(config,file_name):

    # Get options for running ffmpeg
    settings = []
    download_folder = config["downloaded_folder"]
    processed_folder = config["processed_folder"]
    eq_settings = config["eq"]

    # Create the command
    command = [
        "ffmpeg",
            " ".join(settings),
            "-i " + "'" + download_folder + file_name + "'",
            "-af " + "\"" + ",".join(eq_settings) + "\"",
            "'" +processed_folder + file_name + "'"
    ]

    # Run the command
    os.system(" ".join(command))