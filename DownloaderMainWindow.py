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
import os

class DownloaderMainWindow(QMainWindow):
    """
    Class that creates the main window of the downloader application and all of its components.

    Attributes:
        Main window (QMainWindow): The parent class.

    Methods:
        __init__: The constructor for DownloaderMainWindow class.
        initializeMainWindowComponents: This method initializes the main window components.
        initializeUrlLabel: This method initializes the url label.
        initializeUrlEntry: This method initializes the url entry.
        initializeFileNameLabel: This method initializes the file name label.
        initializeFileNameEntry: This method initializes the file name entry.
        initializeFileTypeBox: This method initializes the file type box.
        initializeBrowseFilesButton: This method initializes the browse files button.
        initializeProgressBar: This method initializes the progress bar.
        initializeDownloadButton: This method initializes the download video button.
        initializeDownloadCompletedPopup: This method initializes the download completed popup.
        changeFileType: This method changes the file type attribute to the selected item in the file type box.
        getDefaultFileName: This method gets the default file name.
        getDefaultDownloadPath: This method gets the default download path.
        setDefaultDownloadPath: This method sets the default download path.
        showBrowseFilesWindow: This method shows the browse files window.
        progressBarLoader: This method loads the progress bar while the video is downloading.
        progressBarReset: This method resets the progress bar.
        setDownloadCompletedPopUpProperties: This method sets the download completed popup properties.
        showDownloadCompletedPopUp: This method shows download completed popup.
        downloadVideo: This method downloads the video from the url and saves it to the output path.
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

        # Set the window color
        self.setStyleSheet(downloaderConstants.DOWNLOADER_COLOR_LIGHT)

        # Set the window font
        self.setFont(QFont(downloaderConstants.FONT, downloaderConstants.FONT_SIZE, QFont.Bold))

        # Set the window icon
        self.setWindowIcon(QIcon(downloaderConstants.DOWNLOADER_ICON_PATH))

        # Initialize the main window components and attributes
        self.urlLabel = None                                    # Url label
        self.urlEntry = None                                    # Url entry
        self.fileNameLabel = None                               # File name label
        self.fileNameEntry = None                               # File name entry
        self.fileTypeBox = None                                 # File type box
        self.browseFilesButton = None                           # Browse files button
        self.progressBar = None                                 # Progress bar
        self.downloadButton = None                              # Download button
        self.fileType = downloaderConstants.DEFAULT_FILE_TYPE   # File type

        # Initialize the downloader object
        self.downloader = Downloader()

        # Initialize the download completed pop-up object
        self.downloadCompletedPopUp = DownloadCompletedPopUp(self)

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
        self.initializeUrlLabel()                               # Url label
        self.initializeUrlEntry()                               # Url entry
        self.initializeFileNameLabel()                          # File name label
        self.initializeFileNameEntry()                          # File name entry
        self.initializeFileTypeBox()                            # File type box
        self.initializeBrowseFilesButton()                      # Browse files button
        self.initializeProgressBar()                            # Progress bar
        self.initializeDownloadButton()                         # Download button
        self.initializeDownloadCompletedPopup()                 # Download completed pop-up
        self.setDefaultDownloadPath()                           # Set the default download path


    def initializeUrlLabel(self):
        """
        This method initializes the Url label.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the url label
        self.urlLabel = QLabel(downloaderConstants.URL_LABEL_TEXT, self)

        # Set the url label geometry
        self.urlLabel.setGeometry(downloaderConstants.URL_LABEL_X_AXIS,
                                  downloaderConstants.URL_LABEL_Y_AXIS,
                                  downloaderConstants.URL_LABEL_WIDTH,
                                  downloaderConstants.URL_LABEL_HEIGHT)

        # Set the url label color
        self.urlLabel.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)


    def initializeUrlEntry(self):
        """
        This method initializes the url entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the url entry
        self.urlEntry = QLineEdit(self)

        # Set the url entry geometry
        self.urlEntry.setGeometry(downloaderConstants.URL_ENTRY_X_AXIS,
                                  downloaderConstants.URL_ENTRY_Y_AXIS,
                                  downloaderConstants.URL_ENTRY_WIDTH,
                                  downloaderConstants.URL_ENTRY_HEIGHT)

        # Set the url entry color
        self.urlEntry.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)


    def initializeFileNameLabel(self):
        """
        This method initializes the file name label and entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the file name label
        self.fileNameLabel = QLabel(downloaderConstants.FILE_NAME_LABEL_TEXT, self)

        # Set the file name label geometry
        self.fileNameLabel.setGeometry(downloaderConstants.FILE_NAME_LABEL_X_AXIS,
                                       downloaderConstants.FILE_NAME_LABEL_Y_AXIS,
                                       downloaderConstants.FILE_NAME_LABEL_WIDTH,
                                       downloaderConstants.FILE_NAME_LABEL_HEIGHT)

        # Set the file name label color
        self.fileNameLabel.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)


    def initializeFileNameEntry(self):
        """
        This method initializes the file name entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the file name entry
        self.fileNameEntry = QLineEdit(self)

        # Set the file name entry geometry
        self.fileNameEntry.setGeometry(downloaderConstants.FILE_NAME_ENTRY_X_AXIS,
                                       downloaderConstants.FILE_NAME_ENTRY_Y_AXIS,
                                       downloaderConstants.FILE_NAME_ENTRY_WIDTH,
                                       downloaderConstants.FILE_NAME_ENTRY_HEIGHT)

        # Set the file name entry color
        self.fileNameEntry.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)


    def initializeFileTypeBox(self):
        """
        This method initializes the file type box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the file type label
        self.fileTypeBox = QComboBox(self)

        # Set the file type label geometry
        self.fileTypeBox.setGeometry(downloaderConstants.FILE_TYPE_BOX_X_AXIS,
                                     downloaderConstants.FILE_TYPE_BOX_Y_AXIS,
                                     downloaderConstants.FILE_TYPE_BOX_WIDTH,
                                     downloaderConstants.FILE_TYPE_BOX_HEIGHT)

        # Add items to the file type box
        self.fileTypeBox.addItems([downloaderConstants.FILE_TYPE_MP3,
                                   downloaderConstants.FILE_TYPE_MP4,
                                   downloaderConstants.FILE_TYPE_AVI])

        # Set the file type box color
        self.fileTypeBox.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)

        # Connect the file type box to the changeFileType method
        self.fileTypeBox.currentTextChanged.connect(self.changeFileType)


    def initializeBrowseFilesButton(self):
        """
        This method initializes the browse files button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the browse button
        self.browseFilesButton = QPushButton(downloaderConstants.BROWSE_FILES_BUTTON_TEXT, self)

        # Set the browse button geometry
        self.browseFilesButton.setGeometry(downloaderConstants.BROWSE_FILES_BUTTON_X_AXIS,
                                           downloaderConstants.BROWSE_FILES_BUTTON_Y_AXIS,
                                           downloaderConstants.BROWSE_FILES_BUTTON_WIDTH,
                                           downloaderConstants.BROWSE_FILES_BUTTON_HEIGHT)

        # Set the browse button color
        self.browseFilesButton.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)

        # Connect the browse button to the browseFiles method
        self.browseFilesButton.clicked.connect(self.showBrowseFilesWindow)


    def initializeProgressBar(self):
        """
        This method initializes the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the progress bar
        self.progressBar = QProgressBar(self)

        # Set the progress bar geometry
        self.progressBar.setGeometry(downloaderConstants.PROGRESS_BAR_X_AXIS,
                                     downloaderConstants.PROGRESS_BAR_Y_AXIS,
                                     downloaderConstants.PROGRESS_BAR_WIDTH,
                                     downloaderConstants.PROGRESS_BAR_HEIGHT)

        # Set the progress bar color
        self.progressBar.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)


    def initializeDownloadButton(self):
        """
        This method initializes the download video button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create the download button
        self.downloadButton = QPushButton(downloaderConstants.DOWNLOAD_BUTTON_TEXT, self)

        # Set the download button geometry
        self.downloadButton.setGeometry(downloaderConstants.DOWNLOAD_BUTTON_X_AXIS,
                                        downloaderConstants.DOWNLOAD_BUTTON_Y_AXIS,
                                        downloaderConstants.DOWNLOAD_BUTTON_WIDTH,
                                        downloaderConstants.DOWNLOAD_BUTTON_HEIGHT)

        # Set the download button color
        self.downloadButton.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)

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
        # Connect the download completed popup to the resetting the progress bar
        self.downloadCompletedPopUp.finished.connect(self.progressBarReset)


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


    def getDefaultFileName(self):
        """
        This method gets the default file name.

        Parameters:

        Returns:
            defaultFileName (str): The default file name.
        """
        # Get the default file name based on the file type
        defaultFileName = {
            # Default file name for videos
            downloaderConstants.FILE_TYPE_MP4: downloaderConstants.DEFAULT_VIDEO_FILE_NAME,
            downloaderConstants.FILE_TYPE_AVI: downloaderConstants.DEFAULT_VIDEO_FILE_NAME,
        # Default file name for audio
        }.get(self.fileType, downloaderConstants.DEFAULT_AUDIO_FILE_NAME)

        # Return the default file name
        return defaultFileName


    @staticmethod
    def getDefaultDownloadPath():
        """
        This method gets the default download path.

        Parameters:

        Returns:
            defaultDownloadPath (str): The default download path (User's Downloads folder).
        """
        # Get the user's home directory
        homeDirectory = os.path.expanduser("~")

        # Set the default download path to the user's Downloads folder
        defaultDownloadPath = os.path.join(homeDirectory, "Downloads")

        # Return the default download path
        return defaultDownloadPath


    def setDefaultDownloadPath(self):
        """
        This method sets the default download path.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Get the default download path
        defaultDownloadPath = self.getDefaultDownloadPath() + "\\" + self.getDefaultFileName() + "." + self.fileType.lower()

        # Set the file name entry text to the default download path
        self.fileNameEntry.setText(defaultDownloadPath)


    def showBrowseFilesWindow(self):
        """
        This method shows the browse files window.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set the file path to the default download path
        filePath = self.getDefaultDownloadPath() + "\\" + self.getDefaultFileName()

        # Set the file type filter
        fileTypeFilter = f"{self.fileType} files (*.{self.fileType.lower()});;All files (*.*)"

        # Set the file name entry text to the selected file
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  downloaderConstants.SAVE_FILE_TEXT,
                                                  filePath,
                                                  fileTypeFilter)

        # If the file name is not empty
        if fileName:
            # Set the file name entry text to the selected file
            self.fileNameEntry.setText(fileName)


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
            # Set the progress bar value
            self.progressBar.setValue(i)

            # Sleep for 0.1 seconds
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


    def setDownloadCompletedPopUpProperties(self, isDownloadSuccessful):
        """
        This method sets the download completed popup properties.

        Parameters:
            self (Downloader): The Downloader object.
            isDownloadSuccessful (bool): The download status (True if the download is successful, False if the download is not successful).

        Returns:
            None
        """
        # Check if the download is successful
        if isDownloadSuccessful:
            # Set the download completed popup properties to success
            self.downloadCompletedPopUp.setPopUpPropertiesToSuccess()
        else:
            # Set the download completed popup properties to failure
            self.downloadCompletedPopUp.setPopUpPropertiesToFailure()


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


    def downloadVideo(self):
        """
        This method downloads the video from the url and saves it to the output path.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Get the url
        url = self.urlEntry.text()

        # Get the file type
        fileType = self.fileTypeBox.currentText()

        # Get the output path
        outputPath = self.fileNameEntry.text()

        # Download the YouTube video and get the result message
        downloadResultMessage = self.downloader.downloadYoutubeVideo(url, fileType, outputPath)

        # Check if the video downloaded successfully
        if downloadResultMessage is downloaderConstants.DOWNLOAD_COMPLETED_MESSAGE:
            # Load the progress bar
            self.progressBarLoader()

            # Set the download completed popup properties to success
            self.downloadCompletedPopUp.setPopUpPropertiesToSuccess()
        else:
            # Set the download completed popup properties to failure
            self.downloadCompletedPopUp.setPopUpPropertiesToFailure()

        # Show the download completed popup
        self.showDownloadCompletedPopUp()
