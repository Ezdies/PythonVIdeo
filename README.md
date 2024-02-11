<div align="center">

<img src="Graphics/Video-Downloader-logo.png" alt="Video Downloader Logo" width="512" height="512">

</div>

# Video Downloader

Video Downloader is a simple application built with Python and PyQt5 user interface that allows users to download videos in multiple formats from YouTube. It also features config for generating an executable application for Windows.

## Showcase

https://github.com/tukarp/Video-Downloader/assets/114019481/6e99ebe9-2353-404b-b11c-34e91f59c334

## Requirements

- `Python 3`
- `PyTube`
- `PyQt5`

## Installation

### Download repository

```commandline
https://github.com/Ezdies/PythonVIdeo
```

or

```commandline
https://github.com/tukarp/Video-Downloader
```

### Install packages

```commandline
pip install -r requirements.txt
```

or

```commandline
pip install pyqt5 pytube
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

```
MIT License

Copyright (c) 2023 Maksymilian Dudziak, Tomasz Wnuk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
