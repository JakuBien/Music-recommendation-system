from PySide6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton)
from PySide6.QtWidgets import QApplication

class LineWidget(QWidget):
    def __init__(self, url, parent=None):
        super(LineWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.copyButton = QPushButton("COPY", clicked=self.copyToClipboard)
        self.copyButton.setFixedSize(75, 25)
        self.row.addWidget(self.copyButton)
        self.labelURL = QLabel(url)
        self.row.addWidget(self.labelURL)

        self.setLayout(self.row)

    def copyToClipboard(self):
        cb = QApplication.clipboard()
        cb.clear()
        cb.setText(self.labelURL.text())

