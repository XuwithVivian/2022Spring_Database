# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 961, 711))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab{width:240};")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.label_1 = QtWidgets.QLabel(self.tab_1)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_1.setGeometry(QtCore.QRect(190, 10, 201, 41))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 60, 201, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 110, 201, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 160, 201, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(530, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_5.setGeometry(QtCore.QRect(670, 10, 201, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(530, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_6.setGeometry(QtCore.QRect(670, 60, 201, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(530, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_7.setGeometry(QtCore.QRect(670, 110, 201, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setGeometry(QtCore.QRect(530, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_8.setGeometry(QtCore.QRect(670, 160, 201, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(10, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 210, 201, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_1 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 260, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 260, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 260, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 260, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setGeometry(QtCore.QRect(830, 260, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.treeWidget_1 = QtWidgets.QTreeWidget(self.tab_1)
        self.treeWidget_1.setGeometry(QtCore.QRect(10, 350, 941, 341))
        self.treeWidget_1.setStyleSheet("")
        self.treeWidget_1.setObjectName("treeWidget_1")
        self.label_0 = QtWidgets.QLabel(self.tab_1)
        self.label_0.setGeometry(QtCore.QRect(530, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.lineEdit_0 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_0.setGeometry(QtCore.QRect(670, 210, 201, 41))
        self.lineEdit_0.setObjectName("lineEdit_0")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(190, 10, 201, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(190, 60, 201, 41))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox_1 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_1.setGeometry(QtCore.QRect(190, 110, 67, 31))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit_1.setGeometry(QtCore.QRect(280, 110, 110, 31))
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(190, 150, 201, 41))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(10, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(190, 200, 201, 41))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(550, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(720, 20, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(550, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(720, 70, 181, 41))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(550, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(720, 120, 181, 41))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(550, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(720, 170, 181, 41))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 250, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 250, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 250, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(600, 250, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(820, 250, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.tab_2)
        self.treeWidget_2.setGeometry(QtCore.QRect(10, 330, 941, 351))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(160, 10, 201, 41))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(10, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(160, 60, 201, 41))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(10, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(310, 110, 191, 41))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(580, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_20.setGeometry(QtCore.QRect(730, 80, 181, 41))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(580, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(730, 20, 181, 41))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 110, 101, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 170, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(220, 170, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(410, 170, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(610, 170, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(804, 170, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWidget_3.setGeometry(QtCore.QRect(10, 250, 941, 431))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.treeWidget_3.setFont(font)
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(20, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit_2.setGeometry(QtCore.QRect(170, 40, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(530, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit_3.setGeometry(QtCore.QRect(650, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_16.setGeometry(QtCore.QRect(20, 170, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("\n"
"background-color: rgb(0, 255, 127);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setGeometry(QtCore.QRect(410, 170, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_18.setGeometry(QtCore.QRect(814, 170, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.treeWidget_4 = QtWidgets.QTreeWidget(self.tab_4)
        self.treeWidget_4.setGeometry(QtCore.QRect(10, 270, 941, 411))
        self.treeWidget_4.setObjectName("treeWidget_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "姓名"))
        self.label_2.setText(_translate("MainWindow", "身份证号"))
        self.label_3.setText(_translate("MainWindow", "家庭住址"))
        self.label_4.setText(_translate("MainWindow", "客户电话"))
        self.label_5.setText(_translate("MainWindow", "联系人姓名"))
        self.label_6.setText(_translate("MainWindow", "联系人Email"))
        self.label_7.setText(_translate("MainWindow", "联系人关系"))
        self.label_8.setText(_translate("MainWindow", "联系人电话"))
        self.label_9.setText(_translate("MainWindow", "负责人身份证号"))
        self.pushButton_1.setText(_translate("MainWindow", "增加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.pushButton_4.setText(_translate("MainWindow", "查询"))
        self.pushButton_5.setText(_translate("MainWindow", "清空"))
        self.treeWidget_1.headerItem().setText(0, _translate("MainWindow", "姓名"))
        self.treeWidget_1.headerItem().setText(1, _translate("MainWindow", "身份证号"))
        self.treeWidget_1.headerItem().setText(2, _translate("MainWindow", "家庭住址"))
        self.treeWidget_1.headerItem().setText(3, _translate("MainWindow", "客户电话"))
        self.treeWidget_1.headerItem().setText(4, _translate("MainWindow", "联系人姓名"))
        self.treeWidget_1.headerItem().setText(5, _translate("MainWindow", "联系人Email"))
        self.treeWidget_1.headerItem().setText(6, _translate("MainWindow", "联系人关系"))
        self.treeWidget_1.headerItem().setText(7, _translate("MainWindow", "联系人电话"))
        self.treeWidget_1.headerItem().setText(8, _translate("MainWindow", "负责人身份证号"))
        self.treeWidget_1.headerItem().setText(9, _translate("MainWindow", "负责人类型"))
        self.label_0.setText(_translate("MainWindow", "负责人类型"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "客户管理"))
        self.label_10.setText(_translate("MainWindow", "账户号"))
        self.label_11.setText(_translate("MainWindow", "余额"))
        self.label_12.setText(_translate("MainWindow", "开户日期"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "="))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "!="))
        self.comboBox_1.setItemText(2, _translate("MainWindow", ">"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "<"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", ">="))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "<="))
        self.label_13.setText(_translate("MainWindow", "开户支行"))
        self.label_14.setText(_translate("MainWindow", "身份证号"))
        self.label_15.setText(_translate("MainWindow", "账户类型"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "储蓄"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "支票"))
        self.label_16.setText(_translate("MainWindow", "利率"))
        self.label_17.setText(_translate("MainWindow", "货币类型"))
        self.label_18.setText(_translate("MainWindow", "透支额"))
        self.pushButton_6.setText(_translate("MainWindow", "开户"))
        self.pushButton_7.setText(_translate("MainWindow", "销户"))
        self.pushButton_8.setText(_translate("MainWindow", "修改"))
        self.pushButton_9.setText(_translate("MainWindow", "查询"))
        self.pushButton_10.setText(_translate("MainWindow", "清空"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "待查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "账户管理"))
        self.label_19.setText(_translate("MainWindow", "贷款号"))
        self.label_20.setText(_translate("MainWindow", "贷款支行"))
        self.label_21.setText(_translate("MainWindow", "总金额"))
        self.label_22.setText(_translate("MainWindow", "贷款金额"))
        self.label_23.setText(_translate("MainWindow", "身份证号"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "="))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "!="))
        self.comboBox_3.setItemText(2, _translate("MainWindow", ">"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "<"))
        self.pushButton_11.setText(_translate("MainWindow", "增加"))
        self.pushButton_12.setText(_translate("MainWindow", "删除"))
        self.pushButton_13.setText(_translate("MainWindow", "查询"))
        self.pushButton_14.setText(_translate("MainWindow", "发放"))
        self.pushButton_15.setText(_translate("MainWindow", "清空"))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "贷款号"))
        self.treeWidget_3.headerItem().setText(1, _translate("MainWindow", "贷款支行"))
        self.treeWidget_3.headerItem().setText(2, _translate("MainWindow", "总金额"))
        self.treeWidget_3.headerItem().setText(3, _translate("MainWindow", "贷款状态"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "贷款管理"))
        self.label_24.setText(_translate("MainWindow", "统计时间"))
        self.label_25.setText(_translate("MainWindow", "至"))
        self.pushButton_16.setText(_translate("MainWindow", "储蓄统计"))
        self.pushButton_17.setText(_translate("MainWindow", "贷款统计"))
        self.pushButton_18.setText(_translate("MainWindow", "清空"))
        self.treeWidget_4.headerItem().setText(0, _translate("MainWindow", "支行名字"))
        self.treeWidget_4.headerItem().setText(1, _translate("MainWindow", "业务总金额"))
        self.treeWidget_4.headerItem().setText(2, _translate("MainWindow", "用户数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "业务统计"))

