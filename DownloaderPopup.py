from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel



# Define the constants
OK_PUSH_BUTTON_TEXT = "OK" # The OK push button text
DOWNLOAD_COMPLETED_POPUP_TITLE = "Download Completed" # The download completed popup title
DOWNLOAD_COMPLETED_POPUP_TEXT = "The download has been completed." # The download completed popup text



class DownloadCompletedPopup(QDialog):
    """
    Class that creates a popup window that appears when the download is completed.

    Attributes:
        parent (QWidget): The parent widget.
    """
    def __init__(self, parent=None):
        """
        The constructor for DownloadCompletedPopup class.

        Parameters:
            self (DownloadCompletedPopup): The DownloadCompletedPopup object.

        Returns:
            None
        """
        # Call the parent constructor
        super().__init__(parent)

        # Create the layout
        layout = QVBoxLayout()

        # Set the window title
        self.setWindowTitle(DOWNLOAD_COMPLETED_POPUP_TITLE)
        # Set the window content text
        self.label = QLabel(DOWNLOAD_COMPLETED_POPUP_TEXT)

        # Create the OK button
        self.okButton = QPushButton(OK_PUSH_BUTTON_TEXT)
        # Define the OK button's functionality - closing the popup
        self.okButton.clicked.connect(self.close)

        # Add the label widget to the layout
        layout.addWidget(self.label)
        # Add the OK button widget to the layout
        layout.addWidget(self.okButton)

        # Set the layout
        self.setLayout(layout)
