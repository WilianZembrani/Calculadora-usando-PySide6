from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE, MINIMUN_WIDTH, MINIMUN_HEIGHT, TEXT_MARGIN

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet (f'font-size:{BIG_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setMinimumHeight(MINIMUN_HEIGHT)
        self.setTextMargins(*margins)