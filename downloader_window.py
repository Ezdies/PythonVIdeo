from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from pytube import YouTube
from download_widget import DownloadStatusWidget

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
        self.download_status = DownloadStatusWidget(self)
        

    def set_url(self):
        url_label = QLabel("YouTube Video URL:", self)
        url_label.move(20, 20)
        url_label.resize(200, 30)
        self.url_entry = QLineEdit(self)
        self.url_entry.setGeometry(20, 60, 640, 30)

    def filetype_box(self):
        filetype_box = QComboBox(self)
        filetype_box.addItems(["MP4", "MP3"])
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
        download_button.setGeometry(20, 200, 100, 30)
        download_button.clicked.connect(self.download_video)

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

    def download_video(self):
        url = self.url_entry.text()
        output_path = self.filename_entry.text()
        try:
            yt = YouTube(url)
            if self.filetype == "MP4":
                stream = yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.filter(only_audio=True).first()
            stream.download(filename=output_path + '.' + self.filetype.lower())
            self.statusBar().showMessage("Download Complete")
            self.download_status.show_popup()
        except Exception as e:
            self.statusBar().showMessage(f"Error: {str(e)}")

 #          print(f"Error: {str(e)}")