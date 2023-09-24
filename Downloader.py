from DownloadPopup import DownloadCompletedPopup
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from pytube import YouTube
import time
import os


# Define the constants
WINDOW_WIDTH = 500 # The window width
WINDOW_HEIGHT = 300 # The window height
DOWNLOADER_WINDOW_TITLE = "YouTube Video Downloader" # The window title
DOWNLOADER_VIDEO_URL_LABEL = "YouTube Video URL:" # The URL label
SAVE_AS_LABEL = "Save As:" # The filename label
DEFAULT_FILETYPE = "MP4" # The default filetype
FILETYPE_MP4 = "MP4" # The MP4 filetype
FILETYPE_MP3 = "MP3" # The MP3 filetype
FILETYPE_AVI = "AVI" # The AVI filetype
BROWSE_FILES_BUTTON_TEXT = "Browse files" # The browse button text
DOWNLOAD_BUTTON_TEXT = "Download" # The download button text
MESSAGE_DOWNLOAD_COMPLETED = "Download completed" # The download completed message
MESSAGE_BOX_TEXT = "The video has been downloaded successfully." # The message box text
EXCEPTION_MESSAGE_STREAM_NOT_AVAILABLE = "Error: Stream not available" # The stream not available exception message
EXCEPTION_MESSAGE_OPERATING_SYSTEM_ACCESS = "Error: Output path is not writable" # The operating system access exception message
EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_DIRECTORY = "Error: Invalid output path" # The operating system path is not directory exception message


class Downloader(QMainWindow):
    """
    Class that creates the main window of the downloader application.

    Attributes:
        QMainWindow (QMainWindow): The parent class.

    Methods:
        __init__: The constructor for Downloader class.
        urlLabel: This method creates the URL label and entry.
        filenameLabel: This method creates the filename label and entry.
        filetypeBox: This method creates the filetype box.
        browseFilesButton: This method creates the browse button.
        browseFiles: This method opens the browse window.
        progressBar: This method creates the progress bar.
        progressBarLoading: This method creates the progress bar.
        showPopup: This method shows the popup.
        messageBox: This method shows the message box.
        downloadButton: This method downloads the video.
        downloadVideo: This method downloads the video.
    """
    def __init__(self):
        """
        The constructor for Downloader class.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Call the parent constructor
        super().__init__()

        # Set some main window's properties
        # Set the window title
        self.setWindowTitle(DOWNLOADER_WINDOW_TITLE)
        # Set the window width and height
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        # Set downloader window size
        self.setGeometry(100, 100, 500, 300)

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
        self.filetype = DEFAULT_FILETYPE

    def urlLabel(self):
        """
        This method creates the URL label and entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create URL label
        url_label = QLabel(DOWNLOADER_VIDEO_URL_LABEL, self)

        # Move URL label
        url_label.move(20, 20)

        # Resize URL label
        url_label.resize(200, 30)

        # Create URL entry
        self.url_entry = QLineEdit(self)

        # Set URL entry geometry
        self.url_entry.setGeometry(20, 60, 350, 30)


    def filenameLabel(self):
        """
        This method creates the filename label and entry.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create filename label
        filename_label = QLabel(SAVE_AS_LABEL, self)

        # Move filename label
        filename_label.move(20, 100)

        # Resize filename label
        filename_label.resize(200, 30)

        # Create filename entry
        self.filename_entry = QLineEdit(self)

        # Set filename entry geometry
        self.filename_entry.setGeometry(20, 140, 350, 30)


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
        filetype_box.addItems([FILETYPE_MP4, FILETYPE_MP3, FILETYPE_AVI])

        # Connect the filetype box to the text_changed method
        filetype_box.currentTextChanged.connect(self.text_changed)


    def text_changed(self, str):
        """
        This method sets the filetype attribute to the selected item in the filetype box.

        Parameters:
            self (Downloader): The Downloader object.
            str (str): The selected item in the filetype box.

        Returns:
            None
        """
        # Set the filetype attribute to the selected item in the filetype box
        self.filetype = str


    def browseFilesButton(self):
        """
        This method creates the browse button.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create browse button
        browse_files_button = QPushButton(BROWSE_FILES_BUTTON_TEXT, self)

        # Set browse button geometry
        browse_files_button.setGeometry(385, 140, 100, 30)

        # Connect the browse button to the browseFiles method
        browse_files_button.clicked.connect(self.browseFiles)


    def browseFiles(self):
        """
        This method opens the browse window.

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
            self.filename_entry.setText(filename)


    def progressBar(self):
        """
        This method creates the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create progress bar
        self.progressBar = QProgressBar(self)

        # Set progress bar geometry
        self.progressBar.setGeometry(20, 200, 500, 30)


    def progressBarLoading(self):
        """
        This method creates the progress bar.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set progress bar value to 0
        self.progressBar.setValue(0)

        # Loop through the progress bar values
        for i in range(101):
            # Wait 0.05 seconds
            time.sleep(0.05)

            # Set progress bar value to iteration value
            self.progressBar.setValue(i)


    def showPopup(self):
        """
        This method shows the popup.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create completed download popup
        popup = DownloadCompletedPopup(self)

        # Show completed download popup
        popup.exec_()


    def messageBox(self):
        """
        This method shows the message box.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Set status bar message
        self.statusBar().showMessage(MESSAGE_DOWNLOAD_COMPLETED)

        # Create message box
        messageBox = QMessageBox()

        # Set message box title
        messageBox.setWindowTitle(MESSAGE_DOWNLOAD_COMPLETED)

        # Set message box text
        messageBox.setText(MESSAGE_BOX_TEXT)

        # Show message box
        messageBox.exec_()


    def downloadButton(self):
        """
        This method downloads the video.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Create download button
        download_button = QPushButton(DOWNLOAD_BUTTON_TEXT, self)

        # Set download button geometry
        download_button.setGeometry(20, 250, 465, 30)

        # Connect the download button to the download_video method
        download_button.clicked.connect(self.downloadVideo)


    def downloadVideo(self):
        """
        This method downloads the video.

        Parameters:
            self (Downloader): The Downloader object.

        Returns:
            None
        """
        # Get the URL
        url = self.url_entry.text()

        # Get the output path
        output_path = self.filename_entry.text()

        # Try to download the video
        try:
            # If the output path is not a directory
            if not os.path.isdir(os.path.dirname(output_path)):
                # Raise an ValueError exception
                raise ValueError(EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_DIRECTORY)
            # If the output path is not writable
            if not os.access(os.path.dirname(output_path), os.W_OK):
                # Raise an ValueError exception
                raise ValueError(EXCEPTION_MESSAGE_OPERATING_SYSTEM_ACCESS)

            # Set YouTube video to the YouTube object
            youtubeVideo = YouTube(url)

            # If the filetype is MP4 or AVI
            if self.filetype in [FILETYPE_MP4, FILETYPE_AVI]:
                # Get the highest resolution stream
                youtubeStream = youtubeVideo.streams.get_highest_resolution()
            # If the filetype is MP3
            else:
                # Get the audio stream
                youtubeStream = youtubeVideo.streams.filter(only_audio=True).first()
            # If the stream is available
            if youtubeStream:
                # Start the progress bar
                self.progressBarLoading()

                # Download the video
                youtubeStream.download(filename=output_path + '.' + self.filetype.lower())

                # Show the popup
                self.show_popup()

                # Show the message box
                self.statusBar().showMessage(MESSAGE_DOWNLOAD_COMPLETED)

            # If the stream is not available
            else:
                # Raise an ValueError exception
                self.statusBar().showMessage(EXCEPTION_MESSAGE_STREAM_NOT_AVAILABLE)
        # If an exception occurs
        except Exception as e:
            # Show the exception message
            self.statusBar().showMessage(f"Error: {str(e)}")
