from downloader_window import DownloaderWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloaderWindow()
    window.show()
    sys.exit(app.exec_())