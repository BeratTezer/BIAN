from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from untitled import Ui_MainWindow
import sys

class HyperloopUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(HyperloopUI, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.ui.win0 = Panel.py

def HyperloopUIWindow():
    HyperloopUIWindow = QtWidgets.QApplication(sys.argv)
    win = HyperloopUI()
    win.showMaximized()
    sys.exit(HyperloopUIWindow.exec_())
    
HyperloopUIWindow()