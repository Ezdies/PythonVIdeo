from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QProgressBar
from download_popup import DownloadCompletedPopup
from pytube import YouTube
import time
import vlc
import os


class DownloaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Downloader")
        self.setGeometry(100, 100, 800, 600)

        self.set_url()
        self.set_filename()
        self.browse_button()
        self.download_button()
        self.filetype_box()
        self.filetype = "MP4"
        self.progress_bar()
        self.video_player()
        self.stop_button()
        
    def set_url(self):
        url_label = QLabel("YouTube Video URL:", self)
        url_label.move(20, 20)
        url_label.resize(200, 30)
        self.url_entry = QLineEdit(self)
        self.url_entry.setGeometry(20, 60, 640, 30)

    def filetype_box(self):
        filetype_box = QComboBox(self)
        filetype_box.addItems(["MP4", "MP3", "AVI"])
        filetype_box.setGeometry(680, 60, 100, 30)
        filetype_box.currentTextChanged.connect(self.text_changed)

    def text_changed(self, str):
        self.filetype = str

    def set_filename(self):
        filename_label = QLabel("Save As:", self)
        filename_label.move(20, 100)
        filename_label.resize(200, 30)
        self.filename_entry = QLineEdit(self)
        self.filename_entry.setGeometry(20, 140, 640, 30)

    def browse_button(self):
        browse_button = QPushButton("Browse", self)
        browse_button.setGeometry(680, 140, 100, 30)
        browse_button.clicked.connect(self.browse_files)

    def download_button(self):
        download_button = QPushButton("Download", self)
        download_button.setGeometry(20, 250, 640, 30)
        download_button.clicked.connect(self.download_video)

    def progress_bar(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(20, 200, 640, 30)

    def progress_bar_loading(self):
        self.progress_bar.setValue(0)
        for i in range(101):
            time.sleep(0.05)
            self.progress_bar.setValue(i)

    def show_popup(self):
        popup = DownloadCompletedPopup(self)
        popup.exec_()

    def browse_files(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save As", ".", self.filetype + " files (*." + self.filetype.lower() + ");;All files (*.*)")
        if filename:
            self.filename_entry.setText(filename)

    def message_box(self):
        self.statusBar().showMessage("Download Complete")
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Download Complete")
        msg_box.setText("The video has been downloaded successfully.")
        msg_box.exec_()

    def video_player(self):
        self.play_video_button = QPushButton("Play", self)
        self.play_video_button.setGeometry(20, 300, 340, 30)
        self.play_video_button.clicked.connect(self.play_video)

    def play_video(self):
        url = self.url_entry.text()
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        media = vlc.MediaPlayer(stream.url)
        media.play()

    # jeszcze nic nie robi
    def stop_button(self):
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(360, 300, 300, 30)
        # self.stop_button.clicked.connect(self.stop_video)
    
    def download_video(self):
        url = self.url_entry.text()
        output_path = self.filename_entry.text()
        try:
            if not os.path.isdir(os.path.dirname(output_path)):
             raise ValueError("Invalid output path")
            if not os.access(os.path.dirname(output_path), os.W_OK):
                raise ValueError("Output path is not writable")

            yt = YouTube(url)
            if self.filetype in ["MP4", "AVI"]:
                stream = yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.filter(only_audio=True).first()
            if stream:
                self.progress_bar_loading()
                stream.download(filename=output_path + '.' + self.filetype.lower())
                self.show_popup()
                self.statusBar().showMessage("Download Complete")
            else:
                self.statusBar().showMessage("Error: Stream not available")
        except Exception as e:
            self.statusBar().showMessage(f"Error: {str(e)}")
