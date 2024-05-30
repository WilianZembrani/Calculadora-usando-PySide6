from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MINIMUN_WIDTH, MINIMUN_HEIGHT, TEXT_MARGIN

class Display(QLineEdit):
    eqRequested = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet (f'font-size:{BIG_FONT_SIZE}px; color: white;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setMinimumHeight(MINIMUN_HEIGHT)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        KEYS= Qt.Key

        isEnter = key in [KEYS.Key_Enter or key == KEYS.Key_Return]

        if isEnter:
            print('Enter precionado sinal emitido', type(self).__name__)
            self.eqRequested.emit()
            return event.ignore()
