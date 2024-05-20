from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel)
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)


    window = QMainWindow()

    cw = QWidget()
    v_layout = QVBoxLayout()
    cw.setLayout(v_layout)
 
    label_text = QLabel('Ola meu texto')
    v_layout.addWidget(label_text)

    window.setCentralWidget(cw)
    window.show()



    app.exec()
    