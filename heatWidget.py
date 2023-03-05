from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import os

class Heat(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(Heat, self).__init__(*args, **kwargs)
        
    def set_pixmap(self, pixmap):
            self._pixmap = pixmap
            self.setPixmap(self._pixmap)

class HeatWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HeatWidget, self).__init__(parent)
        
        self.label = Heat(alignment=QtCore.Qt.AlignCenter)
        self.img1 = QtGui.QPixmap(os.path.join(r'\Images', 'basinc1.png'))
        self.img2 = QtGui.QPixmap(os.path.join(r'\Images', 'basinc2.png'))
        self.img3 = QtGui.QPixmap(os.path.join(r'\Images', 'basinc3.png'))
        self.img4 = QtGui.QPixmap(os.path.join(r'\Images', 'basinc4.png'))
        self.img5 = QtGui.QPixmap(os.path.join(r'\Images', 'basinc5.png'))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        ####################
        self.heatLevel = 100
        ####################
        
        self.updateHeatLevel()
        QtWidgets.QVBoxLayout(self).addWidget(self.label)
        
        # 10sn'de bir ker güncellemeyi çalıştırır        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateHeatLevel)
        # self.timer.start(5000) # kullanılacak yenileme hızı
        self.timer.start(1000) 
        
    def updateHeatLevel(self):
        if self.heatLevel >= 95:
            self.label.set_pixmap(self.img5)
        elif self.heatLevel < 95 and self.heatLevel >= 80:
            self.label.set_pixmap(self.img4)
        elif self.heatLevel < 80 and self.heatLevel >= 60:
            self.label.set_pixmap(self.img3)
        elif self.heatLevel < 60 and self.heatLevel >= 40:
            self.label.set_pixmap(self.img2)
        elif self.heatLevel < 40 and self.heatLevel >= 20:
            self.label.set_pixmap(self.img1)
        if self.heatLevel >= 95:
            for i in range(1,10):
                self.heatLevel-=13
        else:
            for i in range(1,10):
                self.heatLevel+=2