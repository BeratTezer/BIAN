# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modernUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 488)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setStyleSheet("background-color: rgb(36, 55, 76);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_left_frame = QtWidgets.QFrame(self.header_frame)
        self.header_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_left_frame.setObjectName("header_left_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_header_button = QtWidgets.QPushButton(self.header_left_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.menu_header_button.setFont(font)
        self.menu_header_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_header_button.setAutoFillBackground(False)
        self.menu_header_button.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/whiteIcons/align-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_header_button.setIcon(icon)
        self.menu_header_button.setIconSize(QtCore.QSize(40, 40))
        self.menu_header_button.setObjectName("menu_header_button")
        self.horizontalLayout_4.addWidget(self.menu_header_button, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.header_left_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.size_grid_header_frame1 = QtWidgets.QFrame(self.header_frame)
        self.size_grid_header_frame1.setMinimumSize(QtCore.QSize(239, 0))
        self.size_grid_header_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grid_header_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grid_header_frame1.setObjectName("size_grid_header_frame1")
        self.horizontalLayout.addWidget(self.size_grid_header_frame1)
        self.header_center_frame = QtWidgets.QFrame(self.header_frame)
        self.header_center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_center_frame.setObjectName("header_center_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.header_center_frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/whiteIcons/gitlab.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.header_center_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.header_center_frame)
        self.size_grid_header_frame2 = QtWidgets.QFrame(self.header_frame)
        self.size_grid_header_frame2.setMinimumSize(QtCore.QSize(239, 0))
        self.size_grid_header_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grid_header_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grid_header_frame2.setObjectName("size_grid_header_frame2")
        self.horizontalLayout.addWidget(self.size_grid_header_frame2)
        self.header_right_frame = QtWidgets.QFrame(self.header_frame)
        self.header_right_frame.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.header_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right_frame.setObjectName("header_right_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimize_window_button = QtWidgets.QPushButton(self.header_right_frame)
        self.minimize_window_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/whiteIcons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setObjectName("minimize_window_button")
        self.horizontalLayout_2.addWidget(self.minimize_window_button)
        self.restore_window_button = QtWidgets.QPushButton(self.header_right_frame)
        self.restore_window_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/whiteIcons/credit-card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QtCore.QSize(16, 16))
        self.restore_window_button.setObjectName("restore_window_button")
        self.horizontalLayout_2.addWidget(self.restore_window_button)
        self.close_window_button = QtWidgets.QPushButton(self.header_right_frame)
        self.close_window_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/whiteIcons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QtCore.QSize(16, 16))
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout_2.addWidget(self.close_window_button)
        self.horizontalLayout.addWidget(self.header_right_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header_frame)
        self.main_body_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setMinimumSize(QtCore.QSize(40, 0))
        self.main_body_frame.setStyleSheet("")
        self.main_body_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_frame.setObjectName("main_body_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.left_menu_cont_frame = QtWidgets.QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setMinimumSize(QtCore.QSize(37, 0))
        self.left_menu_cont_frame.setMaximumSize(QtCore.QSize(32, 16777215))
        self.left_menu_cont_frame.setStyleSheet("background-color: rgb(36, 55, 76);")
        self.left_menu_cont_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_cont_frame.setObjectName("left_menu_cont_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.menu_frame = QtWidgets.QFrame(self.left_menu_cont_frame)
        self.menu_frame.setMinimumSize(QtCore.QSize(90, 0))
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.plots_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.plots_button_label.setFont(font)
        self.plots_button_label.setObjectName("plots_button_label")
        self.gridLayout.addWidget(self.plots_button_label, 10, 1, 1, 1)
        self.connection_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.connection_button_label.setFont(font)
        self.connection_button_label.setObjectName("connection_button_label")
        self.gridLayout.addWidget(self.connection_button_label, 3, 1, 1, 1)
        self.breaks_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.breaks_button_label.setFont(font)
        self.breaks_button_label.setObjectName("breaks_button_label")
        self.gridLayout.addWidget(self.breaks_button_label, 7, 1, 1, 1)
        self.checks_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checks_button_label.setFont(font)
        self.checks_button_label.setObjectName("checks_button_label")
        self.gridLayout.addWidget(self.checks_button_label, 1, 1, 1, 1)
        self.stability_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.stability_button_label.setFont(font)
        self.stability_button_label.setObjectName("stability_button_label")
        self.gridLayout.addWidget(self.stability_button_label, 6, 1, 1, 1)
        self.menuButton_panel = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_panel.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_panel.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/whiteIcons/monitor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_panel.setIcon(icon4)
        self.menuButton_panel.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_panel.setObjectName("menuButton_panel")
        self.gridLayout.addWidget(self.menuButton_panel, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_plots = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_plots.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_plots.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/whiteIcons/map.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_plots.setIcon(icon5)
        self.menuButton_plots.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_plots.setObjectName("menuButton_plots")
        self.gridLayout.addWidget(self.menuButton_plots, 10, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_engine = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_engine.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_engine.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/whiteIcons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_engine.setIcon(icon6)
        self.menuButton_engine.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_engine.setObjectName("menuButton_engine")
        self.gridLayout.addWidget(self.menuButton_engine, 8, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_health = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_health.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_health.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/whiteIcons/heart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_health.setIcon(icon7)
        self.menuButton_health.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_health.setObjectName("menuButton_health")
        self.gridLayout.addWidget(self.menuButton_health, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.panel_button_label = QtWidgets.QLabel(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel_button_label.sizePolicy().hasHeightForWidth())
        self.panel_button_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.panel_button_label.setFont(font)
        self.panel_button_label.setObjectName("panel_button_label")
        self.gridLayout.addWidget(self.panel_button_label, 0, 1, 1, 1)
        self.telem_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.telem_button_label.setFont(font)
        self.telem_button_label.setObjectName("telem_button_label")
        self.gridLayout.addWidget(self.telem_button_label, 2, 1, 1, 1)
        self.menuButton_energy = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_energy.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_energy.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images/whiteIcons/battery-charging.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_energy.setIcon(icon8)
        self.menuButton_energy.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_energy.setObjectName("menuButton_energy")
        self.gridLayout.addWidget(self.menuButton_energy, 9, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_stability = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_stability.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_stability.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Images/whiteIcons/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_stability.setIcon(icon9)
        self.menuButton_stability.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_stability.setObjectName("menuButton_stability")
        self.gridLayout.addWidget(self.menuButton_stability, 6, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_connection = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_connection.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_connection.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Images/whiteIcons/radio.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_connection.setIcon(icon10)
        self.menuButton_connection.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_connection.setObjectName("menuButton_connection")
        self.gridLayout.addWidget(self.menuButton_connection, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.health_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.health_button_label.setFont(font)
        self.health_button_label.setObjectName("health_button_label")
        self.gridLayout.addWidget(self.health_button_label, 5, 1, 1, 1)
        self.menuButton_breaks = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_breaks.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_breaks.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Images/whiteIcons/tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_breaks.setIcon(icon11)
        self.menuButton_breaks.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_breaks.setObjectName("menuButton_breaks")
        self.gridLayout.addWidget(self.menuButton_breaks, 7, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.energy_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.energy_button_label.setFont(font)
        self.energy_button_label.setObjectName("energy_button_label")
        self.gridLayout.addWidget(self.energy_button_label, 9, 1, 1, 1)
        self.test_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.test_button_label.setFont(font)
        self.test_button_label.setObjectName("test_button_label")
        self.gridLayout.addWidget(self.test_button_label, 4, 1, 1, 1)
        self.menuButton_telem = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_telem.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_telem.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Images/whiteIcons/link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_telem.setIcon(icon12)
        self.menuButton_telem.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_telem.setObjectName("menuButton_telem")
        self.gridLayout.addWidget(self.menuButton_telem, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.engine_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.engine_button_label.setFont(font)
        self.engine_button_label.setObjectName("engine_button_label")
        self.gridLayout.addWidget(self.engine_button_label, 8, 1, 1, 1)
        self.configs_button_label = QtWidgets.QLabel(self.menu_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.configs_button_label.setFont(font)
        self.configs_button_label.setObjectName("configs_button_label")
        self.gridLayout.addWidget(self.configs_button_label, 11, 1, 1, 1)
        self.menuButton_checks = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_checks.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_checks.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("Images/whiteIcons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_checks.setIcon(icon13)
        self.menuButton_checks.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_checks.setObjectName("menuButton_checks")
        self.gridLayout.addWidget(self.menuButton_checks, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_test = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_test.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_test.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("Images/whiteIcons/filter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_test.setIcon(icon14)
        self.menuButton_test.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_test.setObjectName("menuButton_test")
        self.gridLayout.addWidget(self.menuButton_test, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.menuButton_configs = QtWidgets.QPushButton(self.menu_frame)
        self.menuButton_configs.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.menuButton_configs.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("Images/whiteIcons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton_configs.setIcon(icon15)
        self.menuButton_configs.setIconSize(QtCore.QSize(32, 32))
        self.menuButton_configs.setObjectName("menuButton_configs")
        self.gridLayout.addWidget(self.menuButton_configs, 11, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_9.addWidget(self.menu_frame)
        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)
        self.main_body_contents = QtWidgets.QFrame(self.main_body_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.main_body_contents.setFont(font)
        self.main_body_contents.setStyleSheet("background-color: rgb(31, 37, 48);")
        self.main_body_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_contents.setObjectName("main_body_contents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_body_contents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.panel = QtWidgets.QWidget()
        self.panel.setObjectName("panel")
        self.label_18 = QtWidgets.QLabel(self.panel)
        self.label_18.setGeometry(QtCore.QRect(9, 6, 1071, 750))
        self.label_18.setStyleSheet("background-image: url(Images/panelWide.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.widget = NeedleWidget(self.panel)
        self.widget.setGeometry(QtCore.QRect(317, 205, 201, 211))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.widget.setObjectName("widget")
        self.widget_3 = SpeedWidget(self.panel)
        self.widget_3.setGeometry(QtCore.QRect(330, 120, 181, 61))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.widget_2 = BatteryWidget(self.panel)
        self.widget_2.setGeometry(QtCore.QRect(180, 200, 71, 101))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.widget_4 = HeatWidget(self.panel)
        self.widget_4.setGeometry(QtCore.QRect(570, 190, 81, 121))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.stackedWidget.addWidget(self.panel)
        self.checks = QtWidgets.QWidget()
        self.checks.setObjectName("checks")
        self.label_28 = QtWidgets.QLabel(self.checks)
        self.label_28.setGeometry(QtCore.QRect(110, 90, 461, 161))
        self.label_28.setObjectName("label_28")
        self.stackedWidget.addWidget(self.checks)
        self.telem = QtWidgets.QWidget()
        self.telem.setObjectName("telem")
        self.label_21 = QtWidgets.QLabel(self.telem)
        self.label_21.setGeometry(QtCore.QRect(100, 120, 361, 161))
        self.label_21.setObjectName("label_21")
        self.stackedWidget.addWidget(self.telem)
        self.connection = QtWidgets.QWidget()
        self.connection.setObjectName("connection")
        self.label_26 = QtWidgets.QLabel(self.connection)
        self.label_26.setGeometry(QtCore.QRect(70, 100, 431, 201))
        self.label_26.setObjectName("label_26")
        self.stackedWidget.addWidget(self.connection)
        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.label_20 = QtWidgets.QLabel(self.test)
        self.label_20.setGeometry(QtCore.QRect(70, 80, 511, 231))
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.test)
        self.health = QtWidgets.QWidget()
        self.health.setObjectName("health")
        self.label_19 = QtWidgets.QLabel(self.health)
        self.label_19.setGeometry(QtCore.QRect(110, 110, 421, 181))
        self.label_19.setObjectName("label_19")
        self.stackedWidget.addWidget(self.health)
        self.stability = QtWidgets.QWidget()
        self.stability.setObjectName("stability")
        self.label_22 = QtWidgets.QLabel(self.stability)
        self.label_22.setGeometry(QtCore.QRect(100, 100, 371, 171))
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.stability)
        self.breaks = QtWidgets.QWidget()
        self.breaks.setObjectName("breaks")
        self.label_29 = QtWidgets.QLabel(self.breaks)
        self.label_29.setGeometry(QtCore.QRect(100, 150, 541, 151))
        self.label_29.setObjectName("label_29")
        self.stackedWidget.addWidget(self.breaks)
        self.engine = QtWidgets.QWidget()
        self.engine.setObjectName("engine")
        self.label_24 = QtWidgets.QLabel(self.engine)
        self.label_24.setGeometry(QtCore.QRect(80, 120, 401, 191))
        self.label_24.setObjectName("label_24")
        self.stackedWidget.addWidget(self.engine)
        self.energy = QtWidgets.QWidget()
        self.energy.setObjectName("energy")
        self.label_25 = QtWidgets.QLabel(self.energy)
        self.label_25.setGeometry(QtCore.QRect(90, 80, 421, 181))
        self.label_25.setObjectName("label_25")
        self.stackedWidget.addWidget(self.energy)
        self.plots = QtWidgets.QWidget()
        self.plots.setObjectName("plots")
        self.label_23 = QtWidgets.QLabel(self.plots)
        self.label_23.setGeometry(QtCore.QRect(90, 110, 451, 181))
        self.label_23.setObjectName("label_23")
        self.stackedWidget.addWidget(self.plots)
        self.configs = QtWidgets.QWidget()
        self.configs.setObjectName("configs")
        self.label_27 = QtWidgets.QLabel(self.configs)
        self.label_27.setGeometry(QtCore.QRect(110, 130, 421, 161))
        self.label_27.setObjectName("label_27")
        self.stackedWidget.addWidget(self.configs)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_8.addWidget(self.main_body_contents)
        self.right_frame = QtWidgets.QFrame(self.main_body_frame)
        self.right_frame.setStyleSheet("background-color: rgb(36, 55, 76);")
        self.right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setObjectName("right_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.right_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.frame = QtWidgets.QFrame(self.right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(220, 160))
        self.frame.setMaximumSize(QtCore.QSize(220, 160))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.label_17 = QtWidgets.QLabel(self.right_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.frame_2 = QtWidgets.QFrame(self.right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(220, 160))
        self.frame_2.setMaximumSize(QtCore.QSize(220, 160))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_8.addWidget(self.right_frame)
        self.verticalLayout.addWidget(self.main_body_frame)
        self.footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.footer_frame.setStyleSheet("background-color: rgb(31, 37, 48);")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.footer_right_frame = QtWidgets.QFrame(self.footer_frame)
        self.footer_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_right_frame.setObjectName("footer_right_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.footer_right_frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.horizontalLayout_5.addWidget(self.footer_right_frame)
        self.footer_left_frame = QtWidgets.QFrame(self.footer_frame)
        self.footer_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_left_frame.setObjectName("footer_left_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.footer_info_button = QtWidgets.QPushButton(self.footer_left_frame)
        self.footer_info_button.setStyleSheet("* {\n"
"    border: none;\n"
"}")
        self.footer_info_button.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("Images/whiteIcons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.footer_info_button.setIcon(icon16)
        self.footer_info_button.setIconSize(QtCore.QSize(32, 32))
        self.footer_info_button.setObjectName("footer_info_button")
        self.horizontalLayout_7.addWidget(self.footer_info_button, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.footer_left_frame)
        self.size_grip = QtWidgets.QFrame(self.footer_frame)
        self.size_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_5.addWidget(self.size_grip, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer_frame, 0, QtCore.Qt.AlignBottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_header_button.setText(_translate("MainWindow", "Menu"))
        self.label_2.setText(_translate("MainWindow", "Atmo Sapphire Hyperloop"))
        self.plots_button_label.setText(_translate("MainWindow", "Plots"))
        self.connection_button_label.setText(_translate("MainWindow", "Connection"))
        self.breaks_button_label.setText(_translate("MainWindow", "Breaks"))
        self.checks_button_label.setText(_translate("MainWindow", "Checks"))
        self.stability_button_label.setText(_translate("MainWindow", "Stability"))
        self.menuButton_panel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Panel sayfasını açar</span></p></body></html>"))
        self.menuButton_plots.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Ortam sayfasını açar</span></p></body></html>"))
        self.menuButton_engine.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Motor sayfasını açar</span></p></body></html>"))
        self.menuButton_health.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Sağlık sayfasını açar</span></p></body></html>"))
        self.panel_button_label.setText(_translate("MainWindow", "Panel"))
        self.telem_button_label.setText(_translate("MainWindow", "Telem"))
        self.menuButton_energy.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Batarya sayfasını açar</span></p></body></html>"))
        self.menuButton_stability.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">İstikrar sayfasını açar</span></p></body></html>"))
        self.menuButton_connection.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Bağlantılar sayfasını açar</span></p></body></html>"))
        self.health_button_label.setText(_translate("MainWindow", "Health"))
        self.menuButton_breaks.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Fren sayfasını açar</span></p></body></html>"))
        self.energy_button_label.setText(_translate("MainWindow", "Energy"))
        self.test_button_label.setText(_translate("MainWindow", "Test"))
        self.menuButton_telem.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Değerler sayfasını açar</span></p></body></html>"))
        self.engine_button_label.setText(_translate("MainWindow", "Engines"))
        self.configs_button_label.setText(_translate("MainWindow", "Configs"))
        self.menuButton_checks.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Kontroller sayfasını açar</span></p></body></html>"))
        self.menuButton_test.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Test sayfasını açar</span></p></body></html>"))
        self.menuButton_configs.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Yapılandırma sayfasını açar</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">GENEL KONTROLLER</span></p><p><br/></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">İLETİŞİM (?)</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">BAĞLANTILAR</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">TEST / YAZMA</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">GENEL SAĞLIK</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">İSTİKRAR</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">FRENLER EKRANI</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">MOTORLAR</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">ENERJİ</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">ZEMİN / ORTAM</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">YAPILANDIRMALAR</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Görüntü"))
        self.label_17.setText(_translate("MainWindow", "Video"))
        self.label_3.setText(_translate("MainWindow", "Version: 1.0 | Developed by Berat Tezer"))
from batteryWidget import BatteryWidget
from heatWidget import HeatWidget
from needleWidget import NeedleWidget
from speedWidget import SpeedWidget