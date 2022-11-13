from modernUI import Ui_MainWindow
from PyQt5.QtCore import QTimer
import speedWidget

class Variables():
    def __init__(self):
        super(Variables, self).__init__()
        
        self.ui = Ui_MainWindow()
        
        self.currentSpeed = speedWidget.currentSpeed
        
    def speedUpdater(self):
        self.updateLabel()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateLabel)
        self.timer.start(1000)