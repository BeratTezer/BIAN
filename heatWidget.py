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
        img1 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'basinc1.png'))
        img2 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'basinc2.png'))
        img3 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'basinc3.png'))
        img4 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'basinc4.png'))
        img5 = QtGui.QPixmap(os.path.join(r'C:\Users\tezer\Masaüstü\ForTF2\Images', 'basinc5.png'))

        # Bu değer sıcaklık yüzdeliğini gösterecek görseli seçmek için kullanılır
        heatLevel = 55
        
        if heatLevel >= 95:
            label.set_pixmap(img5)
        elif heatLevel < 95 and heatLevel >= 80:
            label.set_pixmap(img4)
        elif heatLevel < 80 and heatLevel >= 60:
            label.set_pixmap(img3)
        elif heatLevel < 60 and heatLevel >= 40:
            label.set_pixmap(img2)
        elif heatLevel < 40 and heatLevel >= 20:
            label.set_pixmap(img1)
        
        label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        QtWidgets.QVBoxLayout(self).addWidget(label)