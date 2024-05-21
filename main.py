from PySide6.QtWidgets import (QApplication, QLabel)
import sys
from main_window import MainWindow
import os

os.system('cls')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    label1 = QLabel('Ola meu texto')
    label1.setStyleSheet('font-size: 150px;')
    window.v_layout.addWidget(label1)
    window.adjustFizedSize()

    window.show()
    app.exec()
    