from PySide6.QtCore import (QRect)
from PySide6.QtWidgets import (QLineEdit, QGroupBox, QLabel, QPushButton, QSpinBox, QWidget,
                                QVBoxLayout, QFormLayout, QListWidget, QFrame, QMainWindow,
                                QListWidgetItem)

from lineWidget import LineWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #General
        self.setWindowTitle("Main Window")
        self.setFixedSize(600, 700)

        # Layout
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.VLayout = QVBoxLayout()
        self.VLayoutOutput = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.groupBox_input = QGroupBox(self.centralwidget)
        self.groupBox_input.setGeometry(QRect(10, 10, 580, 150))
        self.groupBox_output = QGroupBox(self.centralwidget)
        self.groupBox_output.setGeometry(QRect(10, 200, 580, 450))

        # Widgets
        self.label_input_url = QLabel("ENTER YOUTUBE URL AND NUMBER OF SONGS SEARCHED")
        self.VLayout.addWidget(self.label_input_url)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.VLayout.addWidget(self.line)
        self.formLayout.addRow("URL:", QLineEdit())
        self.spinboxNumber = QSpinBox()
        self.spinboxNumber.setValue(10)
        self.formLayout.addRow("NUMBER:", self.spinboxNumber)
        self.VLayout.addLayout(self.formLayout)
        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.onStartPressed)
        self.VLayout.addWidget(self.startButton)
        self.groupBox_input.setLayout(self.VLayout)

        self.label_output = QLabel("SIMILAR SONGS")
        self.VLayoutOutput.addWidget(self.label_output)
        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.VLayoutOutput.addWidget(self.line2)
        self.listOutput = QListWidget()

        self.VLayoutOutput.addWidget(self.listOutput)
        self.groupBox_output.setLayout(self.VLayoutOutput)

    def addItemToList(self, url):
        item = QListWidgetItem(self.listOutput)
        self.listOutput.addItem(item)
        row = LineWidget(url)
        item.setSizeHint(row.minimumSizeHint())
        self.listOutput.setItemWidget(item, row)

    def onStartPressed(self):
        num = self.spinboxNumber.value()
        for i in range(num):
            s = "https://www.youtube.com/watch?v=nfs8NYg7yQM&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&index=54 #{test}".format(test = i)
            self.addItemToList(s)

    