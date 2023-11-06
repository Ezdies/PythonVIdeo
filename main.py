from DownloaderMainWindow import DownloaderMainWindow

from PyQt5.QtWidgets import QApplication

import sys

# Main function
if __name__ == '__main__':
    # Create the QApplication object
    application = QApplication(sys.argv)

    # Create the Downloader Main Window object
    window = DownloaderMainWindow()

    # Show the window
    window.show()

    # Execute the app
    sys.exit(application.exec_())
