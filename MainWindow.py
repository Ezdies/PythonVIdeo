import Constants as downloaderConstants

from PopUpWindow import DownloadCompletedPopUp
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
    Creates the main window of the downloader application and all of its components.

    Attributes:
        Main window (QMainWindow): The parent class.

    Methods:
        __init__: The constructor for DownloaderMainWindow class.
        initializeMainWindowComponents: Initializes the main window components.
        initializeUrlLabel: Initializes the url label.
        initializeUrlEntry: Initializes the url entry.
        initializeFileNameLabel: Initializes the file name label.
        initializeFileNameEntry: Initializes the file name entry.
        initializeFileTypeBox: Initializes the file type box.
        initializeBrowseFilesButton: Initializes the browse files button.
        initializeProgressBar: Initializes the progress bar.
        initializeDownloadButton: Initializes the download video button.
        initializeDownloadCompletedPopup: Initializes the download completed popup.
        changeFileType: Changes the file type attribute to the selected item in the file type box.
        getDefaultFileName: Gets the default file name.
        getDefaultDownloadPath: Gets the default download path.
        setDefaultDownloadPath: Sets the default download path.
        showBrowseFilesWindow: Shows the browse files window.
        progressBarLoader: Loads the progress bar while the video is downloading.
        progressBarReset: Resets the progress bar.
        setDownloadCompletedPopUpProperties: Sets the download completed popup properties.
        showDownloadCompletedPopUp: Shows download completed popup.
        downloadVideo: Downloads the video from the url and saves it to the output path.
    """


    def __init__(self):
        """
        The constructor for DownloaderMainWindow class.

        Parameters:
            self (DownloaderMainWindow): The DownloaderMainWindow object.

        Returns:
            None
        """
        super().__init__()
        self.setWindowTitle(downloaderConstants.DOWNLOADER_WINDOW_TITLE)
        self.setFixedSize(downloaderConstants.MAIN_WINDOW_WIDTH, downloaderConstants.MAIN_WINDOW_HEIGHT)
        self.setStyleSheet(downloaderConstants.DOWNLOADER_COLOR_LIGHT)
        self.setFont(QFont(downloaderConstants.FONT, downloaderConstants.FONT_SIZE, QFont.Bold))
        self.setWindowIcon(QIcon(downloaderConstants.DOWNLOADER_ICON_PATH))

        self.urlLabel = None
        self.urlEntry = None
        self.fileNameLabel = None
        self.fileNameEntry = None
        self.fileTypeBox = None
        self.browseFilesButton = None
        self.progressBar = None
        self.downloadButton = None
        self.fileType = downloaderConstants.DEFAULT_FILE_TYPE

        self.downloader = Downloader()
        self.downloadCompletedPopUp = DownloadCompletedPopUp(self)
        self.initializeMainWindowComponents()


    def initializeMainWindowComponents(self):
        """
        Initializes the main window components.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.initializeUrlLabel()
        self.initializeUrlEntry()
        self.initializeFileNameLabel()
        self.initializeFileNameEntry()
        self.initializeFileTypeBox()
        self.initializeBrowseFilesButton()
        self.initializeProgressBar()
        self.initializeDownloadButton()
        self.initializeDownloadCompletedPopup()
        self.setDefaultDownloadPath()


    def initializeUrlLabel(self):
        """
        Initializes the url label.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.urlLabel = QLabel(downloaderConstants.URL_LABEL_TEXT, self)
        self.urlLabel.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.urlLabel.setGeometry(downloaderConstants.URL_LABEL_X_AXIS,
                                  downloaderConstants.URL_LABEL_Y_AXIS,
                                  downloaderConstants.URL_LABEL_WIDTH,
                                  downloaderConstants.URL_LABEL_HEIGHT)


    def initializeUrlEntry(self):
        """
        Initializes the url entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.urlEntry = QLineEdit(self)
        self.urlEntry.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.urlEntry.setGeometry(downloaderConstants.URL_ENTRY_X_AXIS,
                                  downloaderConstants.URL_ENTRY_Y_AXIS,
                                  downloaderConstants.URL_ENTRY_WIDTH,
                                  downloaderConstants.URL_ENTRY_HEIGHT)


    def initializeFileNameLabel(self):
        """
        Initializes the file name label.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.fileNameLabel = QLabel(downloaderConstants.FILE_NAME_LABEL_TEXT, self)
        self.fileNameLabel.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.fileNameLabel.setGeometry(downloaderConstants.FILE_NAME_LABEL_X_AXIS,
                                       downloaderConstants.FILE_NAME_LABEL_Y_AXIS,
                                       downloaderConstants.FILE_NAME_LABEL_WIDTH,
                                       downloaderConstants.FILE_NAME_LABEL_HEIGHT)


    def initializeFileNameEntry(self):
        """
        Initializes the file name entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.fileNameEntry = QLineEdit(self)
        self.fileNameEntry.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.fileNameEntry.setGeometry(downloaderConstants.FILE_NAME_ENTRY_X_AXIS,
                                       downloaderConstants.FILE_NAME_ENTRY_Y_AXIS,
                                       downloaderConstants.FILE_NAME_ENTRY_WIDTH,
                                       downloaderConstants.FILE_NAME_ENTRY_HEIGHT)


    def initializeFileTypeBox(self):
        """
        Initializes the file type box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.fileTypeBox = QComboBox(self)
        self.fileTypeBox.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.fileTypeBox.currentTextChanged.connect(self.changeFileType)
        self.fileTypeBox.setGeometry(downloaderConstants.FILE_TYPE_BOX_X_AXIS,
                                     downloaderConstants.FILE_TYPE_BOX_Y_AXIS,
                                     downloaderConstants.FILE_TYPE_BOX_WIDTH,
                                     downloaderConstants.FILE_TYPE_BOX_HEIGHT)
        self.fileTypeBox.addItems([downloaderConstants.FILE_TYPE_MP3,
                                   downloaderConstants.FILE_TYPE_MP4,
                                   downloaderConstants.FILE_TYPE_AVI])


    def initializeBrowseFilesButton(self):
        """
        Initializes the browse files button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.browseFilesButton = QPushButton(downloaderConstants.BROWSE_FILES_BUTTON_TEXT, self)
        self.browseFilesButton.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.browseFilesButton.clicked.connect(self.showBrowseFilesWindow)
        self.browseFilesButton.setGeometry(downloaderConstants.BROWSE_FILES_BUTTON_X_AXIS,
                                           downloaderConstants.BROWSE_FILES_BUTTON_Y_AXIS,
                                           downloaderConstants.BROWSE_FILES_BUTTON_WIDTH,
                                           downloaderConstants.BROWSE_FILES_BUTTON_HEIGHT)


    def initializeProgressBar(self):
        """
        Initializes the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.progressBar = QProgressBar(self)
        self.progressBar.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.progressBar.setGeometry(downloaderConstants.PROGRESS_BAR_X_AXIS,
                                     downloaderConstants.PROGRESS_BAR_Y_AXIS,
                                     downloaderConstants.PROGRESS_BAR_WIDTH,
                                     downloaderConstants.PROGRESS_BAR_HEIGHT)


    def initializeDownloadButton(self):
        """
        Initializes the download video button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.downloadButton = QPushButton(downloaderConstants.DOWNLOAD_BUTTON_TEXT, self)
        self.downloadButton.setStyleSheet(downloaderConstants.FONT_COLOR_DARK)
        self.downloadButton.clicked.connect(self.downloadVideo)
        self.downloadButton.setGeometry(downloaderConstants.DOWNLOAD_BUTTON_X_AXIS,
                                        downloaderConstants.DOWNLOAD_BUTTON_Y_AXIS,
                                        downloaderConstants.DOWNLOAD_BUTTON_WIDTH,
                                        downloaderConstants.DOWNLOAD_BUTTON_HEIGHT)


    def initializeDownloadCompletedPopup(self):
        """
        Initializes the download completed popup.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.downloadCompletedPopUp.finished.connect(self.progressBarReset)


    def changeFileType(self, changedTextString):
        """
        Changes the file type attribute to the selected item in the file type box.

        Parameters:
            changedTextString (str): The selected item in the file type box.

        Returns:
            None
        """
        self.fileType = changedTextString

        self.fileNameEntry.setText(re.sub(r"\.\w+$", "." + self.fileType.lower(), self.fileNameEntry.text()))


    def getDefaultFileName(self):
        """
        Gets the default file name.

        Parameters:

        Returns:
            defaultFileName (str): The default file name.
        """
        defaultFileName = {
            downloaderConstants.FILE_TYPE_MP4: downloaderConstants.DEFAULT_VIDEO_FILE_NAME,
            downloaderConstants.FILE_TYPE_AVI: downloaderConstants.DEFAULT_VIDEO_FILE_NAME,
        }.get(self.fileType, downloaderConstants.DEFAULT_AUDIO_FILE_NAME)

        return defaultFileName


    @staticmethod
    def getDefaultDownloadPath():
        """
        Gets the default download path.

        Parameters:

        Returns:
            defaultDownloadPath (str): The default download path (User's Downloads folder).
        """
        homeDirectory = os.path.expanduser("~")

        defaultDownloadPath = os.path.join(homeDirectory, "Downloads")

        return defaultDownloadPath


    def setDefaultDownloadPath(self):
        """
        Sets the default download path.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        defaultDownloadPath = self.getDefaultDownloadPath() + "\\" + self.getDefaultFileName() + "." + self.fileType.lower()

        self.fileNameEntry.setText(defaultDownloadPath)


    def showBrowseFilesWindow(self):
        """
        Shows the browse files window.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        filePath = self.getDefaultDownloadPath() + "\\" + self.getDefaultFileName()

        fileTypeFilter = f"{self.fileType} files (*.{self.fileType.lower()});;All files (*.*)"

        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  downloaderConstants.SAVE_FILE_TEXT,
                                                  filePath,
                                                  fileTypeFilter)

        if fileName:
            self.fileNameEntry.setText(fileName)


    def progressBarLoader(self):
        """
        Loads the progress bar while the video is downloading.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        for i in range(101):
            self.progressBar.setValue(i)

            time.sleep(0.01)


    def progressBarReset(self):
        """
        Resets the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        QProgressBar.reset(self.progressBar)


    def setDownloadCompletedPopUpProperties(self, isDownloadSuccessful):
        """
        Sets the download completed popup properties.

        Parameters:
            self (Downloader): The Downloader object.
            isDownloadSuccessful (bool): The download status (True if the download is successful, False if the download is not successful).

        Returns:
            None
        """
        if isDownloadSuccessful:
            self.downloadCompletedPopUp.setPopUpPropertiesToSuccess()
        else:
            self.downloadCompletedPopUp.setPopUpPropertiesToFailure()


    def showDownloadCompletedPopUp(self):
        """
        Shows download completed popup.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        self.downloadCompletedPopUp.exec_()


    def downloadVideo(self):
        """
        Downloads the video from the url and saves it to the output path.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        url = self.urlEntry.text()
        fileType = self.fileTypeBox.currentText()
        outputPath = self.fileNameEntry.text()

        downloadResultMessage = self.downloader.downloadYoutubeVideo(url, fileType, outputPath)

        if downloadResultMessage is downloaderConstants.DOWNLOAD_COMPLETED_MESSAGE:
            self.progressBarLoader()

            self.downloadCompletedPopUp.setPopUpPropertiesToSuccess()
        else:
            self.downloadCompletedPopUp.setPopUpPropertiesToFailure()

        self.showDownloadCompletedPopUp()
