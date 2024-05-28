#estilos do QT para Python | tema usado Dark Theme 
from PySide6 import QtWidgets
from qt_material import apply_stylesheet



def setupTheme():

   apply_stylesheet(qApp, theme='dark_blue.xml', ) #type:ignore



