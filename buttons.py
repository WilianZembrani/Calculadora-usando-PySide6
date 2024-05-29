from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import BIG_FONT_SIZE
from display import Display
from utils import isValidNumber, isEmpty, isNumOrDot

from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from display import Display
   from memory import Memory


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
   def __init__(
         self, display: 'Display', Memory: 'Memory', *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)

      self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
            ]
      self.display = display
      self.memory = Memory
      self._equation = ''
      self._makeGrid()

      @property
      def equation(self):
         return self._equation
      
      @equation.setter
      def equation(self, value):
         self._equation
         self.memory.setText(value)

   def _makeGrid(self):
      for i ,row in enumerate(self._gridMask):
         for j, buttonText in enumerate(row):
            button = Button(buttonText)

            if not isNumOrDot(buttonText) and not isEmpty(buttonText):
               self._configSpecialButton(button)

            self.addWidget(button, i, j)
            slot = self._makeSlot(self._insetButtonTextToDisplay, button)
            self._connectbuttonClicked(button, slot)

   def _connectbuttonClicked(self, button, slot):
      button.clicked.connect(slot)

   def _configSpecialButton(self, button):
      text = button.text()
      
      if text == 'C':
         self._connectbuttonClicked(button, self._clear)

   def _makeSlot(self, func, *args, **kwargs):
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

   def _clear(self):
      self.display.clear()
      
