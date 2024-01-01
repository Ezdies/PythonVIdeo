<img src="Video-Downloader-logo.png" alt="Video Downloader Logo" width="512" height="512">

# Video Downloader

Video Downloader is a simple application built with Python and PyQt5 user interface that allows users to download videos in multiple formats from YouTube. It also features config for generating an executable application for Windows.

## Requirements

- `Python 3`
- `PyQt5`
- `PyTube`

## Installation

### Download repository

```
https://github.com/Ezdies/PythonVIdeo
```

or

```commandline
https://github.com/tukarp/Video-Downloader
```

### Install packages

```commandline
pip install pyqt5 pytube
```

or

```commandline
pip install -r requirements.txt
```

## Generate an executable file

### Install PyInstaller

```commandline
pip install pyinstaller
```

### Generate the executable file

```commandline
pyinstaller --windowed --name "Video Downloader" main.py
```

## Run the application

### Run the script

```commandline
python main.py
```

### Run the executable file

```commandline
Video Downloader.exe
```

## How to use

- Open the program and enter a valid YouTube video URL in the input field.

- Choose a destination folder by either typing the path or clicking the `Browse files` button to select a path.

- Click the `Download` button to start the download process. The program will display the download status in the progress bar.

- Once the download is complete, a `Pop-Up` message will appear confirming the download.

## Acknowledgements

- [PyTube](https://github.com/pytube/pytube)
- [PyQt5](https://pypi.org/project/PyQt5/)

## License

This project is licensed under the MIT License.
