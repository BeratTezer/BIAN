from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5 import QtGui, QtCore, QtWidgets
from qt_material import *
from modernUI import *
import sys 
import os

class Hyperloop(QtWidgets.QMainWindow):
    def __init__(self):
        super(Hyperloop, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # apply_stylesheet(app, theme="dark_cyan.xml")
        
        # Pencere çerçevesini siler
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Gölgelendirme ile ilgili
        # self.shadow = QGraphicsDropShadowEffect()
        # self.shadow.setBlurRadius(50)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 92, 157, 550))
        # self.ui.centralwidget.setGraphicsEffect(self.shadow)
        
        # Pencere ikonunu belirler
        self.setWindowIcon(QtGui.QIcon("Images/whiteIcons/airplay.svg"))
        self.setWindowTitle("Atmo Sapphire Hyperloop")
        
        # Pencerenin sağ altında bulunan ölçeklendirme köşesini oluşturur
        QtWidgets.QSizeGrip(self.ui.size_grip), 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight
        
        # Uygulamada bulunan pencere tuşlarına işlev bağlantılarını atar
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximized())
        
        # Başlangıçta panel butonunu tıklanmış olarak gösterir
        self.ui.menuButton_panel.setStyleSheet("background-color: rgb(31, 37, 48);\nborder-radius: 50;")
        
        # Sol tarafta yer alan sembollere işlev kazandırır
        self.ui.menuButton_panel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.panel))
        self.ui.menuButton_panel.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_panel))
        
        self.ui.menuButton_checks.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.checks))
        self.ui.menuButton_checks.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_checks))
        
        self.ui.menuButton_telem.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.telem))
        self.ui.menuButton_telem.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_telem))
        
        self.ui.menuButton_connection.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.connection))
        self.ui.menuButton_connection.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_connection))
        
        self.ui.menuButton_test.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.test))
        self.ui.menuButton_test.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_test))
        
        self.ui.menuButton_health.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.health))
        self.ui.menuButton_health.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_health))
        
        self.ui.menuButton_stability.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.stability))
        self.ui.menuButton_stability.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_stability))
        
        self.ui.menuButton_breaks.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.breaks))
        self.ui.menuButton_breaks.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_breaks))
        
        self.ui.menuButton_engine.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.engine))
        self.ui.menuButton_engine.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_engine))
        
        self.ui.menuButton_energy.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.energy))
        self.ui.menuButton_energy.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_energy))
        
        self.ui.menuButton_plots.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.plots))
        self.ui.menuButton_plots.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_plots))
        
        self.ui.menuButton_configs.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.configs))
        self.ui.menuButton_configs.clicked.connect(lambda: self.defaultBackground(self.ui.menuButton_configs))
        
        # Pencereyi hareket ettirme işlevi sağlayan fonksiyon
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.pos() - self.clickPosition)
                    self.clickPosition = e.pos()
                    e.accept()

        # İlgili frame'in fonksiyon ile bağlantısı
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        # Solda yer alan menünün üzerindeki butonun fonksiyon ile bağlantısı
        self.ui.menu_header_button.clicked.connect(lambda: self.slideLeftMenu())
        
    # Seçili pencerenin ait olduğu sembol butonunu belirtmeye yarayan fonksiyon
    def defaultBackground(self, widget):
        self.ui.menuButton_panel.setStyleSheet("border: none;")
        self.ui.menuButton_checks.setStyleSheet("border: none;")
        self.ui.menuButton_telem.setStyleSheet("border: none;")
        self.ui.menuButton_connection.setStyleSheet("border: none;")
        self.ui.menuButton_test.setStyleSheet("border: none;")
        self.ui.menuButton_health.setStyleSheet("border: none;")
        self.ui.menuButton_stability.setStyleSheet("border: none;")
        self.ui.menuButton_breaks.setStyleSheet("border: none;")
        self.ui.menuButton_engine.setStyleSheet("border: none;")
        self.ui.menuButton_energy.setStyleSheet("border: none;")
        self.ui.menuButton_plots.setStyleSheet("border: none;")
        self.ui.menuButton_configs.setStyleSheet("border: none;")
        
        widget.setStyleSheet("background-color: rgb(31, 37, 48);\nborder-radius: 50;")
        
        
    # Solda yer alan menünün açılıp kapanma işlevini sağlayan fonksiyon
    def slideLeftMenu(self):
        width = self.ui.left_menu_cont_frame.width()
        object = self.ui.left_menu_cont_frame
        
        if width == 37:
            newWidth = 120
        else:
            newWidth = 37
        
        self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(750)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # Pencereyi hareket ettirme işlevi sağlayan fonksiyon 2
    def mousePressEvent(self, event):
        self.clickPosition = event.pos()
        
    # Uygulamada bulunan pencere tuşlarına işlev oluşturur
    def restore_or_maximized(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon("Images/whiteIcons/maximize.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon("Images/whiteIcons/credit-card.svg"))
        
def HyperloopWindow():
    HyperloopWindow = QtWidgets.QApplication(sys.argv)
    win = Hyperloop()
    win.showNormal()
    sys.exit(HyperloopWindow.exec_())
    
HyperloopWindow()