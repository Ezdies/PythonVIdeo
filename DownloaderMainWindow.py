import DownloaderConstants as downloaderConstants

from DownloaderPopUpWindow import DownloadCompletedPopUp
from Downloader import Downloader

from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

import time
import re

class DownloaderMainWindow(QMainWindow):
    """
    Class that creates the main window of the downloader application and all of its components.

    Attributes:
        Main window (QMainWindow): The parent class.

    Methods:
        __init__: The constructor for DownloaderMainWindow class.
        initializeMainWindowComponents: This method initializes the main window components.
        initializeUrlLabel: This method initializes the URL label.
        initializeUrlEntry: This method initializes the URL entry.
        initializeFileNameLabel: This method initializes the file name label.
        initializeFileNameEntry: This method initializes the file name entry.
        initializeFileTypeBox: This method initializes the file type box.
        initializeBrowseFilesButton: This method initializes the browse files button.
        initializeProgressBar: This method initializes the progress bar.
        initializeDownloadButton: This method initializes the download video button.
        initializeDownloadCompletedPopup: This method initializes the download completed popup.
        showBrowseFilesWindow: This method shows the browse files window.
        showDownloadCompletedPopUp: This method shows download completed popup.
        progressBarLoader: This method loads the progress bar while the video is downloading.
        progressBarReset: This method resets the progress bar.
        downloadVideo: This method downloads the video.
        changeFileType: This method changes the file type attribute to the selected item in the file type box.
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

        # Initialize main window properties
        # Set the window title
        self.setWindowTitle(downloaderConstants.DOWNLOADER_WINDOW_TITLE)

        # Set the window width and height
        self.setFixedSize(downloaderConstants.MAIN_WINDOW_WIDTH, downloaderConstants.MAIN_WINDOW_HEIGHT)

        # Set the window font
        self.setFont(QFont(downloaderConstants.DOWNLOADER_FONT, downloaderConstants.DOWNLOADER_FONT_SIZE))

        # Set the window icon
        self.setWindowIcon(QIcon(downloaderConstants.DOWNLOADER_ICON_PATH))

        # Initialize the main window components and attributes
        self.urlLabel = None                                    # URL label
        self.urlEntry = None                                    # URL entry
        self.fileNameLabel = None                               # File name label
        self.fileNameEntry = None                               # File name entry
        self.fileTypeBox = None                                 # File type box
        self.browseFilesButton = None                           # Browse files button
        self.progressBar = None                                 # Progress bar
        self.downloadButton = None                              # Download button
        self.downloadCompletedPopUp = None                      # Download completed pop-up
        self.fileType = downloaderConstants.DEFAULT_FILE_TYPE   # File type

        # Initialize the downloader components attributes
        self.downloader = Downloader()                          # Downloader object

        # Initialize the main window components
        self.initializeMainWindowComponents()


    def initializeMainWindowComponents(self):
        """
        This method initializes the main window components.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Initialize the main window components
        self.initializeUrlLabel()                               # URL label
        self.initializeUrlEntry()                               # URL entry
        self.initializeFileNameLabel()                          # File name label
        self.initializeFileNameEntry()                          # File name entry
        self.initializeFileTypeBox()                            # File type box
        self.initializeBrowseFilesButton()                      # Browse files button
        self.initializeProgressBar()                            # Progress bar
        self.initializeDownloadButton()                         # Download button
        self.initializeDownloadCompletedPopup()                 # Download completed pop-up


    def initializeUrlLabel(self):
        """
        This method initializes the URL label.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create URL label
        self.urlLabel = QLabel(downloaderConstants.VIDEO_URL_LABEL, self)

        # Set URL label geometry
        self.urlLabel.setGeometry(downloaderConstants.URL_LABEL_X_AXIS,
                                  downloaderConstants.URL_LABEL_Y_AXIS,
                                  downloaderConstants.URL_LABEL_WIDTH,
                                  downloaderConstants.URL_LABEL_HEIGHT)


    def initializeUrlEntry(self):
        """
        This method initializes the URL entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create URL entry
        self.urlEntry = QLineEdit(self)

        # Set URL entry geometry
        self.urlEntry.setGeometry(downloaderConstants.URL_ENTRY_X_AXIS,
                                  downloaderConstants.URL_ENTRY_Y_AXIS,
                                  downloaderConstants.URL_ENTRY_WIDTH,
                                  downloaderConstants.URL_ENTRY_HEIGHT)


    def initializeFileNameLabel(self):
        """
        This method initializes the file name label and entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create file name label
        self.fileNameLabel = QLabel(downloaderConstants.FILE_NAME_LABEL_SAVE_AS, self)

        # Set file name label geometry
        self.fileNameLabel.setGeometry(downloaderConstants.FILE_NAME_LABEL_X_AXIS,
                                       downloaderConstants.FILE_NAME_LABEL_Y_AXIS,
                                       downloaderConstants.FILE_NAME_LABEL_WIDTH,
                                       downloaderConstants.FILE_NAME_LABEL_HEIGHT)


    def initializeFileNameEntry(self):
        """
        This method initializes the file name entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create file name entry
        self.fileNameEntry = QLineEdit(self)

        # Set file name entry geometry
        self.fileNameEntry.setGeometry(downloaderConstants.FILE_NAME_ENTRY_X_AXIS,
                                       downloaderConstants.FILE_NAME_ENTRY_Y_AXIS,
                                       downloaderConstants.FILE_NAME_ENTRY_WIDTH,
                                       downloaderConstants.FILE_NAME_ENTRY_HEIGHT)


    def initializeFileTypeBox(self):
        """
        This method initializes the file type box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create file type label
        self.fileTypeBox = QComboBox(self)

        # Set file type label geometry
        self.fileTypeBox.setGeometry(downloaderConstants.FILE_TYPE_BOX_X_AXIS,
                                     downloaderConstants.FILE_TYPE_BOX_Y_AXIS,
                                     downloaderConstants.FILE_TYPE_BOX_WIDTH,
                                     downloaderConstants.FILE_TYPE_BOX_HEIGHT)

        # Add items to the file type box
        self.fileTypeBox.addItems([downloaderConstants.FILE_TYPE_MP3,  # MP3 file type string - selected by default
                                   downloaderConstants.FILE_TYPE_MP4,  # MP4 file type string
                                   downloaderConstants.FILE_TYPE_AVI]) # AVI file type string

        # Connect the file type box to the change file type method
        self.fileTypeBox.currentTextChanged.connect(self.changeFileType)


    def initializeBrowseFilesButton(self):
        """
        This method initializes the browse files button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create browse button
        self.browseFilesButton = QPushButton(downloaderConstants.BUTTON_TEXT_BROWSE_FILES, self)

        # Set browse button geometry
        self.browseFilesButton.setGeometry(downloaderConstants.BROWSE_FILES_BUTTON_X_AXIS,
                                           downloaderConstants.BROWSE_FILES_BUTTON_Y_AXIS,
                                           downloaderConstants.BROWSE_FILES_BUTTON_WIDTH,
                                           downloaderConstants.BROWSE_FILES_BUTTON_HEIGHT)

        # Connect the browse button to the browse files method
        self.browseFilesButton.clicked.connect(self.showBrowseFilesWindow)


    def initializeProgressBar(self):
        """
        This method initializes the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create progress bar
        self.progressBar = QProgressBar(self)

        # Set progress bar geometry
        self.progressBar.setGeometry(downloaderConstants.PROGRESS_BAR_X_AXIS,
                                     downloaderConstants.PROGRESS_BAR_Y_AXIS,
                                     downloaderConstants.PROGRESS_BAR_WIDTH,
                                     downloaderConstants.PROGRESS_BAR_HEIGHT)


    def initializeDownloadButton(self):
        """
        This method initializes the download video button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create download button
        self.downloadButton = QPushButton(downloaderConstants.BUTTON_TEXT_DOWNLOAD, self)

        # Set download button geometry
        self.downloadButton.setGeometry(downloaderConstants.DOWNLOAD_BUTTON_X_AXIS,
                                        downloaderConstants.DOWNLOAD_BUTTON_Y_AXIS,
                                        downloaderConstants.DOWNLOAD_BUTTON_WIDTH,
                                        downloaderConstants.DOWNLOAD_BUTTON_HEIGHT)

        # Connect the download button to the download video method
        self.downloadButton.clicked.connect(self.downloadVideo)


    def initializeDownloadCompletedPopup(self):
        """
        This method initializes the download completed popup.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create download completed pop-up
        self.downloadCompletedPopUp = DownloadCompletedPopUp(self)

        # Reset the progress bar
        self.downloadCompletedPopUp.finished.connect(self.progressBarReset)


    def showBrowseFilesWindow(self):
        """
        This method shows the browse files window.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set the file name entry text to the selected file
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  "Save As",
                                                  ".",
                                                  self.fileType + \
                                                  " files (*." + \
                                                  self.fileType.lower() + \
                                                  ");;All files (*.*)")

        # If the file name is not empty
        if fileName:
            # Set the file name entry text to the selected file
            self.fileNameEntry.setText(fileName)


    def showDownloadCompletedPopUp(self):
        """
        This method shows the download completed message box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Show completed download pop-up
        self.downloadCompletedPopUp.exec_()


    def progressBarLoader(self):
        """
        This method loads the progress bar while the video is downloading.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # For each number from 0 to 100
        for i in range(101):
            # Set progress bar value
            self.progressBar.setValue(i)

            # Wait for 0.01 seconds
            time.sleep(0.01)


    def progressBarReset(self):
        """
        This method resets the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Reset the progress bar
        QProgressBar.reset(self.progressBar)


    def downloadVideo(self):
        """
        This method downloads the video.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Get the URL
        url = self.urlEntry.text()

        # Get the file type
        fileType = self.fileTypeBox.currentText()

        # Get the output path
        outputPath = self.fileNameEntry.text()

        # Download Youtube video and get the result message
        resultMessage = self.downloader.downloadYoutubeVideo(url, fileType, outputPath)

        # If the result message is download completed message
        if resultMessage is downloaderConstants.DOWNLOAD_COMPLETED_MESSAGE:
            # Load the progress bar
            self.progressBarLoader()

            # Show the download completed pop-up
            self.showDownloadCompletedPopUp()


    def changeFileType(self, changedTextString):
        """
        This method changes the file type attribute to the selected item in the file type box.

        Parameters:
            changedTextString (str): The selected item in the file type box.

        Returns:
            None
        """
        # Set the file type attribute to the selected item in the file type box
        self.fileType = changedTextString

        # Set the file name entry text to the changed file type
        self.fileNameEntry.setText(re.sub(r"\.\w+$", "." + self.fileType.lower(), self.fileNameEntry.text()))
