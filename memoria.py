from PySide6.QtWidgets import QLabel
from variables import SML_FONT_SIZE
from PySide6.QtCore import Qt 


class Memoria(QLabel):
    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     self.configStyle()

    def configStyle(self):
       self.setStyleSheet(f'font-size: {SML_FONT_SIZE}px;')
       self.setAlignment(Qt.AlignmentFlag.AlignRight)


       