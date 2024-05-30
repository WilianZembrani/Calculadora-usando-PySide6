import sys
import os

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication)
from variables import WINDOW_ICON_PATH
from display import Display
from memory import Memory
# from style import setupTheme
from buttons import Button, ButtonsGrid

os.system('cls')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    #Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    #memoria
    memory = Memory('ola')
    window.AddWidgetToVlayout(memory)
    
    #display 
    display = Display()
    window.AddWidgetToVlayout(display)


    #buttonsGrid
    buttonsGrid = ButtonsGrid(display, memory, window)
    window.vLayout.addLayout(buttonsGrid)
    
    #botões


    #executa tudo 
    window.adjustFizedSize()
    window.show()
    app.exec()
    