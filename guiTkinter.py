import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def browse_files():
    filename = filedialog.asksaveasfilename(initialdir = "/", title = "Save As", filetypes = (("MP4 files", "*.mp4"), ("all files", "*.*")))
    filename_entry.delete(0, tk.END)
    filename_entry.insert(0, filename)

def download_video():
    url = url_entry.get()
    output_path = filename_entry.get()

    # Create a YouTube object and get the highest resolution video stream
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()

    # Download the video to the specified path
    stream.download(output_path)

    # Show a message box when the download is complete
    tk.messagebox.showinfo("Download Complete", "The video has been downloaded successfully!")

root = tk.Tk()
root.title("YouTube Video Downloader")

# Create the URL input field
url_label = tk.Label(root, text="YouTube Video URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create the filename input field and "Browse" button
filename_label = tk.Label(root, text="Save As:")
filename_label.pack()
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(side=tk.LEFT, padx=5)
browse_button = tk.Button(root, text="Browse", command=browse_files)
browse_button.pack(side=tk.LEFT)

# Create the "Download" button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

root.mainloop()
