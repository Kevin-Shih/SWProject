# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TitelTableUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 220, 900, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 320, 900, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 420, 900, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 520, 900, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 620, 900, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 720, 900, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_prePage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prePage.setGeometry(QtCore.QRect(660, 100, 121, 61))
        self.pushButton_prePage.setObjectName("pushButton_prePage")
        self.pushButton_nextPage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nextPage.setGeometry(QtCore.QRect(780, 100, 141, 61))
        self.pushButton_nextPage.setObjectName("pushButton_nextPage")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 80, 171, 101))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(370, 30, 221, 121))
        self.pushButton_update.setObjectName("pushButton_update")
        self.label_loading = QtWidgets.QLabel(self.centralwidget)
        self.label_loading.setGeometry(QtCore.QRect(450, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_loading.setFont(font)
        self.label_loading.setObjectName("label_loading")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_prePage.setText(_translate("MainWindow", "上頁"))
        self.pushButton_nextPage.setText(_translate("MainWindow", "下頁"))
        self.pushButton_9.setText(_translate("MainWindow", "回首頁"))
        self.pushButton_update.setText(_translate("MainWindow", "更新內容"))
        self.label_loading.setText(_translate("MainWindow", "loading"))
