from typing import TYPE_CHECKING
import math

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import BIG_FONT_SIZE
from display import Display
from utils import isValidNumber, isEmpty, isNumOrDot


if TYPE_CHECKING:
   from display import Display
   from main_window import MainWindow
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
         self, display: 'Display', memory: 'Memory', window: 'MainWindow',
         *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)

      self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
            ]
      self.display = display
      self.memory = memory
      self.window = window
      self._equation = ''
      self._equationInitialValue = 'Sua conta'
      self._left = None
      self._right = None
      self._op = None

      self.equation = self._equationInitialValue
      self._makeGrid()

   @property
   def equation(self):
      return self._equation

   @equation.setter
   def equation(self, value):
      self._equation = value
      self.memory.setText(value)

   def _makeGrid(self):
      self.display.eqPressed.connect(self._eq)
      self.display.delPressed.connect(self.display.backspace)
      self.display.clearPressed.connect(self._clear)
      self.display.inputPressed.connect(self._insertToDisplay)
      self.display.operatorPressed.connect(self._configLeftOp)

      for i, row in enumerate(self._gridMask):
         for j, buttonText in enumerate(row):
            button = Button(buttonText)

            if not isNumOrDot(buttonText) and not isEmpty(buttonText):
               self._configSpecialButton(button)

            self.addWidget(button, i, j)
            slot = self._makeSlot(self._insertToDisplay, buttonText)
            self._connectButtonClicked(button, slot)

   def _connectButtonClicked(self, button, slot):
      button.clicked.connect(slot)

   def _configSpecialButton(self, button):
      text = button.text()
      
      if text == 'C':
         self._connectButtonClicked(button, self._clear)

      if text in '+-/*^':
         self._connectButtonClicked(
            button,
            self._makeSlot(self._configLeftOp, text)
            )
      
      if text == '=':
         self._connectButtonClicked(button, self._eq)
      
      if text == '◀':
         self._connectButtonClicked(button, self.display.backspace)

   def _makeSlot(self, func, *args, **kwargs):
      @Slot(bool)
      def realSlot(_):
         func(*args, **kwargs)
      return realSlot

   @Slot()
   def _insertToDisplay(self, text):
      newDisplayValue = self.display.text() + text
      
      if not isValidNumber(newDisplayValue):
         return

      self.display.insert(text)

   @Slot()
   def _clear(self):
      self._left = None
      self._right = None
      self._op = None
      self.equation = self._equationInitialValue
      self.display.clear()

   @Slot()
   def _configLeftOp(self, text):
      displayText = self.display.text()  
      self.display.clear() 

      if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

      if self._left is None:
            self._left = float(displayText)

      self._op = text
      self.equation = f'{self._left} {self._op} ??'


   @Slot()
   def _eq(self):
      displayText = self.display.text()

      if not isValidNumber(displayText):
         self._showError('Conta incompleta')
         return
      
      self._right = float(displayText)
      self.equation = f'{self._left} {self._op} {self._right}'
      result = 'error'
      
      try:
         if '^' in self.equation and isinstance(self._left, float):
            result = math.pow(self._left, self._right)
         else:  
            result = eval(self.equation)      
      except ZeroDivisionError:
                     self._showError('Divisão por ZERO')
      except OverflowError:
                     self._showError('Resultado muito extenso')

      self.display.clear()
      self.memory.setText(f'{self.equation} = {result}')
      self._left = result
      self._right = None

      if result == 'error':
         self._left = None

   def _showError(self, text):
      msgBox = self.window.makeMsgBox()
      msgBox.setText(text)
      msgBox.setIcon(msgBox.Icon.Critical)

      msgBox.setStandardButtons(
         msgBox.StandardButton.Ok
      )

      msgBox.exec() 