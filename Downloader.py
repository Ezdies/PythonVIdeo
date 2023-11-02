import DownloaderConstants as downloaderConstants

from pytube import YouTube

import os

class Downloader:
    """
    This class downloads videos from different sources.

    Attributes:
        None

    Methods:
        downloadYoutubeVideo: This method downloads the youtube video.
    """
    @staticmethod
    def downloadYoutubeVideo(url, filetype, outputPath):
        """
        This method downloads the youtube video.

        Parameters:
            url (str): The URL of the youtube video.
            filetype (str): The file type of the downloaded youtube video.
            outputPath (str): The output path of the downloaded youtube video.

        Returns:
            resultMessage (str): The result message. If the video is downloaded, the result message is download completed message. If the video is not downloaded, the result message is an exception.
        """
        # Try to download the video
        try:
            # If the output path is not a directory
            if not os.path.isdir(os.path.dirname(outputPath)):
                # Show an invalid output path exception message in the status bar
                return downloaderConstants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_DIRECTORY
            # If the output path is not writable
            if not os.access(os.path.dirname(outputPath), os.W_OK):
                # Show an output path is not writable exception message in the status bar
                return downloaderConstants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_WRITABLE

            # Set YouTube video to the YouTube object
            youtubeVideo = YouTube(url)

            # If the filetype is MP4 or AVI
            if filetype in [downloaderConstants.FILETYPE_MP4, downloaderConstants.FILETYPE_AVI]:
                # Get the highest resolution stream
                youtubeStream = youtubeVideo.streams.get_highest_resolution()
            # If the filetype is MP3
            else:
                # Get the audio stream
                youtubeStream = youtubeVideo.streams.filter(only_audio=True).first()

            # If the stream is available
            if youtubeStream:
                # Download the video
                youtubeStream.download(filename=outputPath)

                # Show the download completed message in the status bar
                return downloaderConstants.MESSAGE_DOWNLOAD_COMPLETED
            # If the stream is not available
            else:
                # Show a stream not available exception message in the status bar
                return downloaderConstants.EXCEPTION_MESSAGE_STREAM_NOT_AVAILABLE
        # If an exception occurs
        except Exception as exception:
            # Show the exception message in the status bar
            return str(exception)
