from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import QtCore, QtWidgets
from modernUI import Ui_MainWindow
from PyQt5.QtCore import QTimer

class Speed(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(Speed, self).__init__(*args, **kwargs)

class SpeedWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SpeedWidget, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.label = Speed(alignment=QtCore.Qt.AlignCenter)
        QFontDatabase.addApplicationFont("Images\Hyperspeed.ttf")
        self.label.setFont(QFont("Hyperspeed"))
        
        ####################
        self.currentSpeed = 986
        ####################
        
        self.label.setText("{}".format(self.currentSpeed))
        self.label.setStyleSheet('font-size: 50pt; color: #70F8BA; background-color: rgba(0, 0, 0, 0);')
        
        QtWidgets.QVBoxLayout(self).addWidget(self.label)
        
        self.updateLabel()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateLabel)
        self.timer.start(1000)
        
    # Döngüler denemeler için değerlerin değişmesi gerektiğinden kullanılmıştır
    def updateLabel(self):
        self.label.setText("{}".format(self.currentSpeed))
        if self.currentSpeed >= 120:
            for i in range(1,5):
                self.currentSpeed-=1
        elif self.currentSpeed > 50 and self.currentSpeed < 120:
            for i in range(1,10):
                self.currentSpeed-=1
        else:
            for i in range(1,20):
                self.currentSpeed+=4