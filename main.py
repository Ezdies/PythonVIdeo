from PyQt5.QtWidgets import QApplication
from Downloader import Downloader
import sys



# Main function
if __name__ == '__main__':
    # Create the QApplication object
    application = QApplication(sys.argv)
    # Create the Downloader object
    window = Downloader()
    # Show the window
    window.show()
    # Execute the app
    sys.exit(application.exec_())
