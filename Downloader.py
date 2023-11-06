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
                # Return the invalid output path exception message
                return downloaderConstants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_DIRECTORY
            # If the output path is not writable
            if not os.access(os.path.dirname(outputPath), os.W_OK):
                # Return the output path is not writable exception message
                return downloaderConstants.EXCEPTION_MESSAGE_OPERATING_SYSTEM_PATH_IS_NOT_WRITABLE

            # Set YouTube video to the YouTube object
            youtubeVideo = YouTube(url)

            # If the filetype is MP4 or AVI
            if filetype in [downloaderConstants.FILE_TYPE_MP4, downloaderConstants.FILE_TYPE_AVI]:
                # Get the highest resolution stream
                youtubeStream = youtubeVideo.streams.get_highest_resolution()
            # If the filetype is MP3
            else:
                # Get the audio only stream
                youtubeStream = youtubeVideo.streams.filter(only_audio=True).first()

            # If the stream is available
            if youtubeStream:
                # Download the video
                youtubeStream.download(filename=outputPath)

                # Return the download completed message
                return downloaderConstants.DOWNLOAD_COMPLETED_MESSAGE
            # If the stream is not available
            else:
                # Return the stream not available exception message
                return downloaderConstants.EXCEPTION_MESSAGE_STREAM_NOT_AVAILABLE
        # If an exception occurs
        except Exception as exception:
            # Return the exception message as a string
            return str(exception)
