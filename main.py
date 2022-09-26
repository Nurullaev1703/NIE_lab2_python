import math
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('NIE_lab2')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.label_img.setPixmap(QPixmap('Main.png'))
        self.label_img.setScaledContents(True)

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x >= 5:
                answer = (5 * math.pow(x,2))/(6*math.pow(a+b,2))
            else:
                answer = math.pow(x,3) * (a+b)
            self.label_answer.setText('Ответ: ' + str(format(answer, '.2f')))
            self.label_answer.setStyleSheet("background: rgb(0, 255, 140,0.5); padding:5px;")
        except:
            self.label_answer.setText('Ошибка!')
            self.label_answer.setStyleSheet('background: rgb(255, 0, 0, 1); padding:5px; color:rgb(255,255,255);')
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')
        self.label_answer.setStyleSheet('')

app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())
