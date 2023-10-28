import DownloaderConstants as downloaderConstants

from DownloaderPopupWindow import DownloadCompletedPopup
from Downloader import Downloader

from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel

import time

class DownloaderMainWindow(QMainWindow):
    """
    Class that creates the main window of the downloader application.

    Attributes:
        Main window (QMainWindow): The parent class.

    Methods:
        __init__: The constructor for Downloader class.
        urlLabel: This method creates the URL label and entry.
        filenameLabel: This method creates the filename label and entry.
        filetypeBox: This method creates the filetype box.
        browseFilesButton: This method creates the browse files button.
        browseFilesWindow: This method opens the browse files window.
        progressBar: This method creates the progress bar.
        progressBarLoading: This method updates the progress bar as the video is downloading.
        showDownloadCompletedPopup: This method shows the download completed popup.
        downloadCompletedMessageBox: This method shows the download completed message box.
        downloadButton: This method creates the download video button.
        downloadVideo: This method downloads the video.
    """
    def __init__(self):
        """
        The constructor for DownloaderMainWindow class.

        Parameters:
            self (DownloaderMainWindow): The DownloaderMainWindow object.

        Returns:
            None
        """
        # Call the parent constructor
        super().__init__()

        # Set downloader main window components
        # Set the window title
        self.setWindowTitle(downloaderConstants.DOWNLOADER_WINDOW_TITLE)

        # Set the window width and height
        self.setFixedSize(downloaderConstants.WINDOW_WIDTH, downloaderConstants.WINDOW_HEIGHT)

        # Set downloader window size
        self.setGeometry(100, 100, downloaderConstants.WINDOW_WIDTH, downloaderConstants.WINDOW_HEIGHT)

        # Call the application components
        # Set the URL label and entry
        self.urlLabel()

        # Set the filename label and entry
        self.filenameLabel()

        # Set the progress bar
        self.filetypeBox()

        # Set the browse button
        self.browseFilesButton()

        # Set the progress bar
        self.progressBar()

        # Set the download button
        self.downloadButton()

        # Set the default filetype
        self.filetype = downloaderConstants.DEFAULT_FILETYPE


    def urlLabel(self):
        """
        This method creates the URL label and entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create URL label
        url_label = QLabel(downloaderConstants.DOWNLOADER_VIDEO_URL_LABEL, self)

        # Move URL label
        url_label.move(20, 20)

        # Resize URL label
        url_label.resize(200, 30)

        # Create URL entry
        self.urlEntry = QLineEdit(self)

        # Set URL entry geometry
        self.urlEntry.setGeometry(20, 60, 350, 30)


    def filenameLabel(self):
        """
        This method creates the filename label and entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create filename label
        filename_label = QLabel(downloaderConstants.LABEL_SAVE_AS, self)

        # Move filename label
        filename_label.move(20, 100)

        # Resize filename label
        filename_label.resize(200, 30)

        # Create filename entry
        self.filenameEntry = QLineEdit(self)

        # Set filename entry geometry
        self.filenameEntry.setGeometry(20, 140, 350, 30)


    def filetypeBox(self):
        """
        This method creates the filetype box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create filetype label
        filetype_box = QComboBox(self)

        # Set filetype label geometry
        filetype_box.setGeometry(385, 60, 100, 30)

        # Add items to the filetype box
        filetype_box.addItems([downloaderConstants.FILETYPE_MP4, downloaderConstants.FILETYPE_MP3, downloaderConstants.FILETYPE_AVI])

        # Connect the filetype box to the text_changed method
        filetype_box.currentTextChanged.connect(self.textChanged)


    def textChanged(self, changedTextString):
        """
        This method sets the filetype attribute to the selected item in the filetype box.

        Parameters:
            self (Downloader): The Downloader object.
            changedTextString (str): The selected item in the filetype box.

        Returns:
            None
        """
        # Set the filetype attribute to the selected item in the filetype box
        self.filetype = changedTextString


    def browseFilesButton(self):
        """
        This method creates the browse files button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create browse button
        browse_files_button = QPushButton(downloaderConstants.BUTTON_TEXT_BROWSE_FILES, self)

        # Set browse button geometry
        browse_files_button.setGeometry(385, 140, 100, 30)

        # Connect the browse button to the browseFiles method
        browse_files_button.clicked.connect(self.browseFilesWindow)


    def browseFilesWindow(self):
        """
        This method opens the browse files window.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set the filename entry text to the selected file
        filename, _ = QFileDialog.getSaveFileName(self, "Save As", ".", self.filetype + " files (*." + self.filetype.lower() + ");;All files (*.*)")

        # If the filename is not empty
        if filename:
            # Set the filename entry text to the selected file
            self.filenameEntry.setText(filename)


    def progressBar(self):
        """
        This method creates the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create progress bar
        self.downloadProgressBar = QProgressBar(self)

        # Set progress bar geometry
        self.downloadProgressBar.setGeometry(20, 200, 500, 30)


    def progressBarLoading(self):
        """
        This method updates the progress bar as the video is downloading.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set progress bar value to 0
        self.downloadProgressBar.setValue(0)

        # Loop through the progress bar values
        for i in range(101):
            # Wait 0.05 seconds
            time.sleep(0.05)

            # Set progress bar value to iteration value
            self.downloadProgressBar.setValue(i)


    def showDownloadCompletedPopup(self):
        """
        This method shows download completed popup.

        Returns:
            None
        """
        # Create completed download popup
        popup = DownloadCompletedPopup(self)

        # Show completed download popup
        popup.exec_()


    def downloadCompletedMessageBox(self):
        """
        This method shows the download completed message box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set status bar message
        self.statusBar().showMessage(downloaderConstants.MESSAGE_DOWNLOAD_COMPLETED)

        # Create message box
        messageBox = QMessageBox()

        # Set message box title
        messageBox.setWindowTitle(downloaderConstants.MESSAGE_DOWNLOAD_COMPLETED)

        # Set message box text
        messageBox.setText(downloaderConstants.MESSAGE_BOX_TEXT)

        # Show message box
        messageBox.exec_()


    def downloadButton(self):
        """
        This method creates the download video button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create download button
        downloadButton = QPushButton(downloaderConstants.BUTTON_TEXT_DOWNLOAD, self)

        # Set download button geometry
        downloadButton.setGeometry(20, 250, 465, 30)

        # Connect the download button to the download_video method
        downloadButton.clicked.connect(self.downloadVideo)


    def downloadVideo(self):
        """
        This method downloads the video.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the Downloader object
        downloader = Downloader()

        # Get the URL
        url = self.urlEntry.text()

        # Get the output path
        outputPath = self.filenameEntry.text()

        # Download youtube video
        resultMessage = downloader.downloadYoutubeVideo(url, outputPath)

        # If the result message is download completed message
        if resultMessage is downloaderConstants.MESSAGE_DOWNLOAD_COMPLETED:
            # Start the progress bar
            self.progressBarLoading()

            # Show the download completed popup
            self.showDownloadCompletedPopup()

        # Show the result message in the status bar
        self.statusBar().showMessage(resultMessage)
