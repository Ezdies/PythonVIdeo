from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel



# Define the constants
OK_PUSH_BUTTON = "OK" # The OK push button text
DOWNLOAD_COMPLETED_POPUP_TITLE = "Download Completed" # The download completed popup title
DOWNLOAD_COMPLETED_POPUP_TEXT = "The download has been completed." # The download completed popup text



class DownloadCompletedPopup(QDialog):
    """
    Class that creates a popup window that appears when the download is completed.

    Attributes:
        parent (QWidget): The parent widget.

    Methods:
        runDownloadCompletedPopup: This method runs the download completed popup window.
    """
    def __init__(self):
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
        # Set the layout
        self.setLayout(layout)

        # Create the OK button
        self.ok_button = QPushButton(OK_PUSH_BUTTON)
        # Define the OK button's functionality - closing the popup
        self.ok_button.clicked.connect(self.close)

        # Set the window title
        self.setWindowTitle(DOWNLOAD_COMPLETED_POPUP_TITLE)
        # Set the window content text
        self.label = QLabel(DOWNLOAD_COMPLETED_POPUP_TEXT)

        # Run the download completed popup
        self.runDownloadCompletedPopup()

    def runDownloadCompletedPopup(self):
        """
        This method runs the download completed popup window.

        Parameters:
            self (DownloadCompletedPopup): The DownloadCompletedPopup object.

        Returns:
            None
        """
        # Add the label widget to the layout
        self.layout.addWidget(self.label)

        # Add the OK button widget to the layout
        self.layout.addWidget(self.ok_button)
