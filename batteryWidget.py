from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QSize
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
        
        label = Battery(alignment=QtCore.Qt.AlignCenter)
        img0 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery0.png')).scaled(QSize(50,88))
        img1 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery1.png')).scaled(QSize(50,88))
        img2 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery2.png')).scaled(QSize(50,88))
        img3 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery3.png')).scaled(QSize(50,88))
        img4 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery4.png')).scaled(QSize(50,88))
        img5 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery5.png')).scaled(QSize(50,88))
        img6 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery6.png')).scaled(QSize(50,88))
        img7 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery7.png')).scaled(QSize(50,88))
        img8 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery8.png')).scaled(QSize(50,88))
        img9 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF\Images', 'panelBattery9.png')).scaled(QSize(50,88))
    
        ######################
        batteryCharge = False
        batteryPercentage = 50
        ######################
        
        if batteryCharge == True:
            if batteryPercentage >= 50:
                label.set_pixmap(img6)
            else:
                label.set_pixmap(img7)
        elif batteryCharge == False:
            if batteryPercentage >= 95:
                label.set_pixmap(img0)
            elif batteryPercentage >= 80:
                label.set_pixmap(img1)
            elif batteryPercentage >= 60:
                label.set_pixmap(img2)
            elif batteryPercentage >= 50:
                label.set_pixmap(img3)
            elif batteryPercentage >= 35:
                label.set_pixmap(img4)
            elif batteryPercentage >= 15:
                label.set_pixmap(img5)
            elif batteryPercentage >= 5:
                label.set_pixmap(img8)
            else:
                label.set_pixmap(img9)
                
        label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        
        QtWidgets.QVBoxLayout(self).addWidget(label)