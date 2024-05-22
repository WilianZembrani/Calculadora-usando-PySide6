import sys
import os

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication)
from variables import WINDOW_ICON_PATH
from display import Display
from memoria import Memoria
from style import setupTheme


os.system('cls')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    
    # label1 = QLabel('Ola meu texto')
    # label1.setStyleSheet('font-size: 150px; color:red;')
    # window.AddWidgetToVlayout()
    # window.adjustFizedSize()
    # 'font_family': 'Roboto',
 
    #display 
    display = Display()
    window.AddWidgetToVlayout(display)

    #memoria
    memoria = Memoria('25 ')
    window.AddWidgetToVlayout(memoria)

    #Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #executa tudo 
    window.adjustFizedSize()
    window.show()
    app.exec()
    