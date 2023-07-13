from PySide6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton)
from PySide6.QtCore import QRect

class LineWidget(QWidget):
    def __init__(self, url, parent=None):
        super(LineWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.copyButton = QPushButton("COPY")
        self.copyButton.setGeometry(QRect(0, 0, 100, 50))
        self.row.addWidget(QPushButton("COPY"))
        self.row.addWidget(QLabel(url))

        self.setLayout(self.row)