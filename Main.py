import sys
from PyQt5.QtWidgets import QApplication
from Twidget import Twidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tw = Twidget()
    tw.setFocus()
    tw.show()
    tw.update()
    app.exec_()
