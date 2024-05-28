from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import BIG_FONT_SIZE
from display import Display
from utils import isValidNumber

class Button(QPushButton):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.configStyle()

   def configStyle(self):
      font = self.font()
      font.setPixelSize(BIG_FONT_SIZE)
      self.setFont(font)
      self.setMinimumSize(100, 75)

class ButtonsGrid(QGridLayout):
   def __init__(self, display: Display, *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)

      self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
            ]
      self.display = display
      self._makeGrid()

   def _makeGrid(self):
      for i ,row in enumerate(self._gridMask):
         for j, buttonText in enumerate(row):
            button = Button(buttonText)
            self.addWidget(button, i, j)
            buttonSlot = self._makeButtonDisplaySlot(self._insetButtonTextToDisplay, button)

            button.clicked.connect(buttonSlot)

   def _makeButtonDisplaySlot(self, func, *args, **kwargs):
      @Slot(bool)
      def realSlot(_):
         func(*args, **kwargs)
      return realSlot

   def _insetButtonTextToDisplay(self,button):
      buttonText = button.text()
      newDisplayValue = self.display.text() + buttonText
      if not isValidNumber(newDisplayValue):
         return

      self.display.insert(buttonText)
      
