from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import os

class Battery(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(Battery, self).__init__(*args, **kwargs)
        
    def set_pixmap(self, pixmap):
            self._pixmap = pixmap
            self.setPixmap(self._pixmap)

class BatteryWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BatteryWidget, self).__init__(parent)
        
        self.label = Battery(alignment=QtCore.Qt.AlignCenter)
        self.img1 = QtGui.QPixmap(os.path.join(r'\Images', 'enerji1.png'))
        self.img2 = QtGui.QPixmap(os.path.join(r'\Images', 'enerji2.png'))
        self.img3 = QtGui.QPixmap(os.path.join(r'\Images', 'enerji3.png'))
        self.img4 = QtGui.QPixmap(os.path.join(r'\Images', 'enerji4.png'))
        self.img5 = QtGui.QPixmap(os.path.join(r'\Images', 'enerji5.png'))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        
        ############################
        self.batteryPercentage = 100
        ############################
        
        self.updateBatteryWidget()
        QtWidgets.QVBoxLayout(self).addWidget(self.label)
        
        # 10sn'de bir ker güncellemeyi çalıştırır        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateBatteryWidget)
        # self.timer.start(10000) # kullanılacak yenileme hızı
        self.timer.start(1000) 


    def updateBatteryWidget(self):
        if self.batteryPercentage >= 95:
            self.label.set_pixmap(self.img5)
        elif self.batteryPercentage < 95 and self.batteryPercentage >= 80:
            self.label.set_pixmap(self.img4)
        elif self.batteryPercentage < 80 and self.batteryPercentage >= 60:
            self.label.set_pixmap(self.img3)
        elif self.batteryPercentage < 60 and self.batteryPercentage >= 40:
            self.label.set_pixmap(self.img2)
        elif self.batteryPercentage < 40 and self.batteryPercentage >= 20:
            self.label.set_pixmap(self.img1)
        if self.batteryPercentage == 100 or self.batteryPercentage > 100:
            for i in range(1,10):
                self.batteryPercentage-=15
        else:
            for i in range(1,5):
                self.batteryPercentage+=4