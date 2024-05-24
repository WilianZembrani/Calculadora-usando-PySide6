from PySide6.QtWidgets import QLabel, QWidget
from variables import SML_FONT_SIZE
from PySide6.QtCore import Qt 


class Memoria(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SML_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


       