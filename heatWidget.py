from PyQt5 import QtCore, QtGui, QtWidgets
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
        
        label = Heat(alignment=QtCore.Qt.AlignCenter)
        img = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'heatIndicatorBlue2.png')).scaled(50, 92)
    
        ######################
        # deviceOn = False
        heatLevel = 50
        ######################
        
        label.set_pixmap(img)        
        label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        
        QtWidgets.QVBoxLayout(self).addWidget(label)