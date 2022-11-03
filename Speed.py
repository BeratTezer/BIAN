from PyQt5 import QtCore, QtGui, QtWidgets


#################################
# DOESNT WORK
#################################

class Speed(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(Speed, self).__init__(*args, **kwargs)

class SpeedWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SpeedWidget, self).__init__(parent)
        
        def medal_update(self):
            label.setText("{}kmh".format(currentSpeed))
            self.update()
            
        self.my_timer = QtCore.QTimer(self, timeout=medal_update, interval=15 * 100)
        
        label = Speed(alignment=QtCore.Qt.AlignCenter)
        
        ####################
        currentSpeed = 100
        ####################
        
        label.setText("{}kmh".format(currentSpeed))
        label.setStyleSheet('font-size: 30pt; color: #1838a1;')
        
        QtWidgets.QVBoxLayout(self).addWidget(label)
        
        currentSpeed += 50
        
        