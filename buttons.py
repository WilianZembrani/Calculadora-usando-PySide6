from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
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

class ButtonsGrid(QGridLayout):
   def __init__(self,*args, **kwargs) -> None:
      super().__init__(*args, **kwargs)

      self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]