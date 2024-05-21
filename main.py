import sys
import os

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH


os.system('cls')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    label1 = QLabel('Ola meu texto')
    label1.setStyleSheet('font-size: 150px; color:red;')
    window.AddWidgetToVlayout(label1)
    window.adjustFizedSize()

    #Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)


    window.adjustFizedSize()
    window.show()
    app.exec()
    