"""
This module contains the pop-up window class for the downloader application.
"""

import Source.Constants.DownloaderConstants as downloaderConstants

from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class DownloadCompletedPopUp(QDialog):
    """
    Creates a pop-up window that appears when the download is completed.

    Methods:
        __init__: The constructor for DownloadCompletedPopUp class.
        initializeLabel: Initializes the label.
        initializeOkButton: Initializes the ok button.
        setPopUpPropertiesToSuccess: Sets the pop-up window download properties to success.
        setPopUpPropertiesToFailure: Sets the pop-up window download properties to failure.

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
        super().__init__(parent)
        self.setWindowTitle(None)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowIcon(QIcon(downloaderConstants.DOWNLOADER_ICON_PATH))
        self.setFixedSize(downloaderConstants.POPUP_WINDOW_WIDTH, downloaderConstants.POPUP_WINDOW_HEIGHT)
        self.setFont(QFont(downloaderConstants.FONT, downloaderConstants.FONT_SIZE, QFont.Bold))

        self.label = None
        self.okButton = None

        self.initializeLabel()
        self.initializeOkButton()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.okButton)
        self.setLayout(layout)


    def initializeLabel(self):
        """
        Initializes the label.

        Parameters:
            self (DownloadCompletedPopUp): The DownloadCompletedPopUp object.

        Returns:
            None
        """
        self.label = QLabel(None)
        self.label.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)


    def initializeOkButton(self):
        """
        Initializes the ok button.

        Parameters:
            self (DownloadCompletedPopUp): The DownloadCompletedPopUp object.

        Returns:
            None
        """
        self.okButton = QPushButton(downloaderConstants.BUTTON_TEXT_OK)
        self.okButton.setStyleSheet(downloaderConstants.DOWNLOADER_COLOR_LIGHT)
        self.okButton.clicked.connect(self.close)


    def setPopUpPropertiesToSuccess(self):
        """
        Sets the pop-up window download properties to success.

        Parameters:
            self (DownloadCompletedPopUp): The DownloadCompletedPopUp object.

        Returns:
            None
        """
        self.setWindowTitle(downloaderConstants.DOWNLOAD_COMPLETED_POPUP_TITLE)
        self.label.setText(downloaderConstants.DOWNLOAD_COMPLETED_POPUP_TEXT)


    def setPopUpPropertiesToFailure(self):
        """
        Sets the pop-up window download properties to failure.

        Parameters:
            self (DownloadCompletedPopUp): The DownloadCompletedPopUp object.

        Returns:
            None
        """
        self.setWindowTitle(downloaderConstants.DOWNLOAD_FAILED_POPUP_TITLE)
        self.label.setText(downloaderConstants.DOWNLOAD_FAILED_POPUP_TEXT)
