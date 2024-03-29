"""
This module contains the downloader class for the downloader application.
"""

import Source.Constants.DownloaderConstants as downloaderConstants

from pytube import YouTube

import os

class Downloader:
    """
    Downloads videos from different sources.

    Attributes:
        None

    Methods:
        downloadYoutubeVideo: This method downloads the youtube video.
    """


    @staticmethod
    def downloadYoutubeVideo(url, filetype, outputPath):
        """
        Downloads the youtube video.

        Parameters:
            url (str): The url of the youtube video.
            filetype (str): The file type of the downloaded youtube video.
            outputPath (str): The output path of the downloaded youtube video.

        Returns:
            resultMessage (str): The result message. If the video is downloaded, the result message is download completed message. If the video is not downloaded, the result message is an exception.
        """
        try:
            if not os.path.isdir(os.path.dirname(outputPath)):
                return downloaderConstants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_DIRECTORY

            if not os.access(os.path.dirname(outputPath), os.W_OK):
                return downloaderConstants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_WRITABLE

            youtubeVideo = YouTube(url)

            if filetype in [downloaderConstants.FILE_TYPE_MP4, downloaderConstants.FILE_TYPE_AVI]:
                youtubeStream = youtubeVideo.streams.get_highest_resolution()
            else:
                youtubeStream = youtubeVideo.streams.filter(only_audio=True).first()

            if youtubeStream:
                youtubeStream.download(filename=outputPath)

                return downloaderConstants.DOWNLOAD_COMPLETED_MESSAGE
            else:
                return downloaderConstants.EXCEPTION_MESSAGE_STREAM_NOT_AVAILABLE
        except Exception as exception:
            return str(exception)
