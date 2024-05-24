from PySide6.QtWidgets import QPushButton
from variables import MED_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.configStyle()

    def configStyle(self):
       font = self.font()
       font.setPixelSize(MED_FONT_SIZE)
       self.setFont(font)
       self.setMinimumSize(75, 75)

