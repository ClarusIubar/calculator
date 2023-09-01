<<<<<<< HEAD
# ch 6.3.3 ui.py
=======
# ch 6.3.1 ui.py
>>>>>>> 3ae35502755bf18aed12d509825d61851ca3667f

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

<<<<<<< HEAD
        self.btn1 = QPushButton('Calc', self)
=======
        self.btn1 = QPushButton('Calc', self) # button name changed
>>>>>>> 3ae35502755bf18aed12d509825d61851ca3667f
        self.btn2 = QPushButton('Clear', self)

        self.le1 = QLineEdit('0', self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
<<<<<<< HEAD
        self.le1.setFocus(True)
=======
        self.le1.setFocus(True) # focus setting
>>>>>>> 3ae35502755bf18aed12d509825d61851ca3667f
        self.le1.selectAll()

        self.le2 = QLineEdit('0', self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb = QComboBox(self)
        self.cb.addItems(['+','-','*','/'])

        hbox_formuler = QHBoxLayout()
        hbox_formuler.addWidget(self.le1)
        hbox_formuler.addWidget(self.cb)
        hbox_formuler.addWidget(self.le2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formuler)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

<<<<<<< HEAD
    def setDisplay(self, text):
        self.te1.appendPlainText(text)
=======
    def setDisplay(self): # change method name
        self.te1.appendPlainText("Button clicked!")
>>>>>>> 3ae35502755bf18aed12d509825d61851ca3667f

    def clearMessage(self):
        self.te1.clear()    
