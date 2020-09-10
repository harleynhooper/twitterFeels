from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QTextEdit
from GetFeels import Feels


class Twidget(QWidget):
    def __init__(self):
        super(Twidget, self).__init__()
        self.text = QLabel()
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("How's the internet currently feel about ...")
        self.img = QLabel()
        self.pixmap = QPixmap(f"img/thinking.png")
        self.img.setPixmap(self.pixmap)
        self.logOutput = QTextEdit()
        self.vbox = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.user_input.setFont(QFont('FiraSans', 24, QFont.Bold))
        self.user_input.setAlignment(Qt.AlignCenter)
        self.text.setFont(QFont('FiraSans', 18))
        self.text.setAlignment(Qt.AlignCenter)
        self.logOutput.setReadOnly(True)
        self.logOutput.setFont(QFont('FiraCode', 11))
        self.logOutput.setLineWrapMode(True)
        self.logOutput.setMinimumHeight(self.pixmap.height()/2)
        self.logOutput.setAutoFillBackground(True)
        self.logOutput.setStyleSheet("color: #ffd700; background-color: #4a4a4a;")
        self.resize(self.pixmap.width(), self.pixmap.height())
        self.vbox.addWidget(self.text)
        self.vbox.addStretch()
        self.vbox.addWidget(self.img)
        self.vbox.addStretch()
        self.vbox.addWidget(self.user_input)
        self.vbox.addStretch()
        self.vbox.addWidget(self.logOutput)
        self.vbox.addStretch()
        self.setLayout(self.vbox)

    def data(self):
        feels = Feels.get_feels(self.user_input.text())
        self.text.setText(f"The internet currently feels {feels[0].upper()} about {self.user_input.text().title()}. \n\nScore: {feels[1]}\n")
        self.user_input.selectAll()
        self.pixmap = QPixmap(f"img/{feels[0]}.png")
        self.img.setPixmap(self.pixmap)
        self.logOutput.setText(feels[2])

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            if self.user_input.text() == "":
                self.logOutput.setText("Error: You're doing it wrong! Please enter a search query.")
            else:
                self.data()
        elif e.key() == Qt.Key_Escape:
            self.close()
