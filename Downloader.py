import DownloaderConstants as constants

from pytube import YouTube

import os

class Downloader:
    """
    This class downloads the youtube video.

    Attributes:
        None

    Methods:
        downloadYoutubeVideo: This method downloads the youtube video.
    """
    def downloadYoutubeVideo(url, filetype, outputPath):
        """
        This method downloads the youtube video.

        Parameters:
            self (Downloader): The Downloader object.
            url (str): The URL of the youtube video.
            outputPath (str): The downloaded file output path.

        Returns:
            resultMessage (str): The result message. If the video is downloaded, the result message is download completed message. If the video is not downloaded, the result message is an exception.
        """
        # Try to download the video
        try:
            # If the output path is not a directory
            if not os.path.isdir(os.path.dirname(outputPath)):
                # Raise an ValueError exception
                raise ValueError(constants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_DIRECTORY)
            # If the output path is not writable
            if not os.access(os.path.dirname(outputPath), os.W_OK):
                # Raise an ValueError exception
                raise ValueError(constants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_ACCESS)

            # Set YouTube video to the YouTube object
            youtubeVideo = YouTube(url)

            # If the filetype is MP4 or AVI
            if filetype in [constants.FILETYPE_MP4, constants.FILETYPE_AVI]:
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
            # If the stream is not available
            else:
                # Raise an stream not available exception
                return constants.EXCEPTION_MESSAGE_STREAM_NOT_AVAILABLE
        # If an exception occurs
        except Exception as exception:
            # Raise an exception
            return exception
