import DownloaderConstants as downloaderConstants

from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class DownloadCompletedPopUp(QDialog):
    """
    Class that creates a pop-up window that appears when the download is completed.

    Attributes:
        parent (QWidget): The parent widget.
    """
    def __init__(self, parent=None):
        """
        The constructor for DownloadCompletedPopUp class.

        Parameters:
            self (QDialog): The DownloadCompletedPopUp object.

        Returns:
            None
        """
        # Call the parent constructor
        super().__init__(parent)

        # Create the layout
        layout = QVBoxLayout()

        # Define the pop-up window properties
        # Set the window title
        self.setWindowTitle(downloaderConstants.DOWNLOAD_COMPLETED_POPUP_TITLE)

        # Set the window width and height
        self.setFixedSize(downloaderConstants.POPUP_WINDOW_WIDTH, downloaderConstants.POPUP_WINDOW_HEIGHT)

        # Set the window font
        self.setFont(QFont(downloaderConstants.FONT, downloaderConstants.FONT_SIZE))

        # Set the window icon
        self.setWindowIcon(QIcon(downloaderConstants.DOWNLOADER_ICON_PATH))

        # Set the window content text
        self.label = QLabel(downloaderConstants.DOWNLOAD_COMPLETED_POPUP_TEXT)

        # Remove the help button from the window
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Define the OK button properties
        # Create the OK button
        self.okButton = QPushButton(downloaderConstants.BUTTON_TEXT_OK)

        # Connect the OK button to the close method
        self.okButton.clicked.connect(self.close)

        # Define the layout properties
        # Add the label widget to the layout
        layout.addWidget(self.label)

        # Add the OK button widget to the layout
        layout.addWidget(self.okButton)

        # Set the layout
        self.setLayout(layout)
