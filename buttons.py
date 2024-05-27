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

      self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
            ]
      self._makeGrid()

   def _makeGrid(self):
      for i ,row in enumerate(self._gridMask):
         for j, button_text in enumerate(row):
            button = Button(button_text)
            self.addWidget(button, i, j)


