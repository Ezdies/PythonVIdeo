import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton
from pytube import YouTube

class DownloaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Downloader")

        # Create the URL input field
        url_label = QLabel("YouTube Video URL:", self)
        url_label.move(20, 20)
        self.url_entry = QLineEdit(self)
        self.url_entry.setGeometry(20, 40, 400, 30)

        # Create the filename input field and "Browse" button
        filename_label = QLabel("Save As:", self)
        filename_label.move(20, 80)
        self.filename_entry = QLineEdit(self)
        self.filename_entry.setGeometry(20, 100, 320, 30)
        browse_button = QPushButton("Browse", self)
        browse_button.setGeometry(350, 100, 70, 30)
        browse_button.clicked.connect(self.browse_files)

        # Create the "Download" button
        download_button = QPushButton("Download", self)
        download_button.setGeometry(20, 150, 100, 30)
        download_button.clicked.connect(self.download_video)

    def browse_files(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save As", ".", "MP4 files (*.mp4);;All files (*.*)")
        if filename:
            self.filename_entry.setText(filename)

    def download_video(self):
        url = self.url_entry.text()
        output_path = self.filename_entry.text()

        # Create a YouTube object and get the highest resolution video stream
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        stream.download(output_path)

        # Show a message box when the download is complete
        self.statusBar().showMessage("Download Complete")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloaderWindow()
    window.show()
    sys.exit(app.exec_())
