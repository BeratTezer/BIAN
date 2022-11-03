import os
from PyQt5 import QtCore, QtGui, QtWidgets

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
        img0 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery0.png')
        img1 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery1.png')
        img2 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery2.png')
        img3 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery3.png')
        img4 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery4.png')
        img5 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery5.png')
        img6 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery6.png')
        img7 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery7.png')
        img8 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery8.png')
        img9 = os.path.join(r'C:\Users\tezer\Masaüstü\ForTF', 'panelBattery9.png')
        
        ######################
        batteryCharge = False
        batteryPercentage = 50
        ######################
        
        if batteryCharge == True:
            if batteryPercentage >= 50:
                label.set_pixmap(QtGui.QPixmap(img6))
            else:
                label.set_pixmap(QtGui.QPixmap(img7))
        elif batteryCharge == False:
            if batteryPercentage >= 95:
                label.set_pixmap(QtGui.QPixmap(img0))
            elif batteryPercentage >= 80:
                label.set_pixmap(QtGui.QPixmap(img1))
            elif batteryPercentage >= 60:
                label.set_pixmap(QtGui.QPixmap(img2))
            elif batteryPercentage >= 50:
                label.set_pixmap(QtGui.QPixmap(img3))
            elif batteryPercentage >= 35:
                label.set_pixmap(QtGui.QPixmap(img4))
            elif batteryPercentage >= 15:
                label.set_pixmap(QtGui.QPixmap(img5))
            elif batteryPercentage >= 5:
                label.set_pixmap(QtGui.QPixmap(img8))
            else:
                label.set_pixmap(QtGui.QPixmap(img9))
                
        QtWidgets.QVBoxLayout(self).addWidget(label)
        