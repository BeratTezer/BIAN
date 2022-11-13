from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from variableResource import Variables
from modernUI import Ui_MainWindow


class Speed(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(Speed, self).__init__(*args, **kwargs)

class SpeedWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SpeedWidget, self).__init__(parent)
        
        self.ui = Ui_MainWindow()
        
        self.label = Speed(alignment=QtCore.Qt.AlignCenter)
        
        ####################
        self.currentSpeed = 100
        ####################
        
        self.label.setText("{}kmh".format(self.currentSpeed))
        self.label.setStyleSheet('font-size: 30pt; color: #1838a1; background-color: rgba(0, 0, 0, 0);')
        
        QtWidgets.QVBoxLayout(self).addWidget(self.label)
        
        
        self.updateLabel()
        Variables.speedUpdater(self)
        

    def updateLabel(self):
        self.label.setText("{}kmh".format(self.currentSpeed))
        if self.currentSpeed >= 120:
            for i in range(1,5):
                self.currentSpeed-=1
        elif self.currentSpeed > 50 and self.currentSpeed < 120:
            for i in range(1,10):
                self.currentSpeed-=1
        else:
            for i in range(1,20):
                self.currentSpeed+=4