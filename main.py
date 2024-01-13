from MainWindow import DownloaderMainWindow

from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = DownloaderMainWindow()
    window.show()
    sys.exit(application.exec_())
