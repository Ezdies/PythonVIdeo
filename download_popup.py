from PyQt5.QtWidgets import QLabel, QVBoxLayout, QDialog, QPushButton

class DownloadCompletedPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Download completed")
        
        
        layout = QVBoxLayout()
        label = QLabel("The file has been downloaded successfully.")
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.close)
        layout.addWidget(label)
        layout.addWidget(ok_button)
        self.setLayout(layout)
        
        