import sys

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QImage, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from UI import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img = QImage(500, 500, QImage.Format_ARGB32)
        self.img.fill(QColor(0, 0, 0, 0))
        self.pushButton.clicked.connect(self.button_handler)

    def button_handler(self):
        self.img = QImage(500, 500, QImage.Format_ARGB32)
        self.img.fill(QColor(0, 0, 0, 0))
        qp = QPainter(self.img)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(50, 250)
        qp.drawEllipse(QPointF(250, 250), r, r)
        qp.end()
        self.repaint()

    def paintEvent(self, a0):
        qp = QPainter(self)
        qp.drawImage(125, 0, self.img)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
