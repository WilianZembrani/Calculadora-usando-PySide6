from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        #Configurando o Layout Básico 
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        #Título da janela 
        self.setWindowTitle('Calculadora')


    def adjustFizedSize(self):
        #ultima coisa a ser feita 
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def AddWidgetToVlayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
    
    def makeMsgBox(self):
        return QMessageBox(self)