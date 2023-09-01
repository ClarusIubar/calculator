# ch 6.2.2 ctrl.py

class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self): # calculate method
        pass 
    
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)