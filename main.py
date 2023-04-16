import ffmpeg
import os
from pytube import YouTube

# Get the value of the $WIN_DIR_DOC environment variable, or use a default value
win_dir = os.environ.get('WIN_DIR_DOC', 'C:/Documents')

# Create the download directory if it does not exist
path_to_download_dir = os.path.join(win_dir, 'YouTubeDownloads')
if not os.path.exists(path_to_download_dir):
    os.makedirs(path_to_download_dir)

url = 'https://www.youtube.com/watch?v=PjDgKXe8gxs'

# Create a YouTube object and get the video information
yt = YouTube(url)
yt.check_availability()

# Find the highest resolution progressive stream
stream = yt.streams.get_highest_resolution()

# Specify the download directory and filename
filename = 'output.mp4'
output_path = os.path.join(path_to_download_dir, filename)

# Download the video to the specified path
stream.download(output_path)



