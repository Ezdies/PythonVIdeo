# YouTube Video Downloader

YouTube Video Downloader is a simple application built with Python and PyQt5 user interface that allows users to download videos in multiple formats from YouTube. It also features config for generating an executable application for Windows.

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

```
https://github.com/tukarp/Youtube-Video-Downloader
```

### Install packages

```
pip install pyqt5 pytube
```

## Generate an executable file

### Install PyInstaller

```
pip install pyinstaller
```

### Generate the executable file

```
pyinstaller --windowed --name "Video Downloader" main.py
```

## Run the application

### Run the script

```
python main.py
```

### Run the executable file

```
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
