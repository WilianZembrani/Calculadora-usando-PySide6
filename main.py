import sys
import os

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication)
from variables import WINDOW_ICON_PATH
from display import Display
from memory import Memoria
from style import setupTheme
from buttons import Button, ButtonsGrid

os.system('cls')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
 
    #Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    #memoria
    memory = Memoria('2.0 ^ 10.0 = 1024')
    window.AddWidgetToVlayout(memory)
    
    #display 
    display = Display()
    window.AddWidgetToVlayout(display)


    #buttonsGrid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)
    
    #botões
    buttonsGrid.addWidget(Button('0'), 0, 0)
    buttonsGrid.addWidget(Button('1'), 0, 1)
    buttonsGrid.addWidget(Button('2'), 0, 2)
    buttonsGrid.addWidget(Button('3'), 1, 0, 1, 1)


    #executa tudo 
    window.adjustFizedSize()
    window.show()
    app.exec()
    