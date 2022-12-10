from PyQt5 import QtCore, QtGui, QtWidgets
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
        img1 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'enerji1.png'))
        img2 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'enerji2.png'))
        img3 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'enerji3.png'))
        img4 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'enerji4.png'))
        img5 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'enerji5.png'))
        
        # Bu değer batarya yüzdeliğini gösterecek görseli seçmek için kullanılır
        batteryPercentage = 35
        
        if batteryPercentage >= 95:
            label.set_pixmap(img5)
        elif batteryPercentage < 95 and batteryPercentage >= 80:
            label.set_pixmap(img4)
        elif batteryPercentage < 80 and batteryPercentage >= 60:
            label.set_pixmap(img3)
        elif batteryPercentage < 60 and batteryPercentage >= 40:
            label.set_pixmap(img2)
        elif batteryPercentage < 40 and batteryPercentage >= 20:
            label.set_pixmap(img1)
                
        label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        QtWidgets.QVBoxLayout(self).addWidget(label)