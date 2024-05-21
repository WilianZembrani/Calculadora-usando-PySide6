from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        #Configurando o Layout Básico 
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        #Título
        self.setWindowTitle('Calculadora')

    def adjustFizedSize(self):
        #ultima coisa a ser feita 
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())