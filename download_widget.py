from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from download_popup import DownloadCompletedPopup

class DownloadStatusWidget(QLabel):
#   TEN PLIK JEST OBECNIE NIEUZYWANY, DODALEM GO DO DOWNLOADER_WINDOW
#   BO TAK BYLO WYGODNIEJ
#   for future purposes

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(20, 250, 400, 30)
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setText("")

    def show_popup(self):
        popup = DownloadCompletedPopup(self)
        popup.exec_()
        
