import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.is_clicked = False
        self.pushButton.clicked.connect(self.click)
        self.qp = QPainter()
        print(self.size())

    def click(self):
        self.is_clicked = True
        self.update()

    def paintEvent(self, event):
        if self.is_clicked:
            self.qp.begin(self)
            self.qp.setBrush(QColor(*(255, 204, 0)))
            x = random.randint(1, 563)
            y = random.randint(1, 530)
            r = random.randint(5, 500)
            self.qp.drawEllipse(x, y, r, r)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
