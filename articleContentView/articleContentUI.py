# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'articleContentUI.ui'
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
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 160, 1000, 700))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 20, 141, 61))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(170, 10, 691, 31))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 100, 21, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_good = QtWidgets.QLabel(self.centralwidget)
        self.label_good.setGeometry(QtCore.QRect(130, 100, 41, 16))
        self.label_good.setObjectName("label_good")
        self.label_boo = QtWidgets.QLabel(self.centralwidget)
        self.label_boo.setGeometry(QtCore.QRect(260, 100, 41, 16))
        self.label_boo.setObjectName("label_boo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(150, 60, 261, 31))
        font = QtGui.QFont()
        font.setFamily("3ds Light")
        font.setPointSize(11)
        self.label_author.setFont(font)
        self.label_author.setObjectName("label_author")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 130, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(200, 130, 311, 21))
        self.label_date.setObjectName("label_date")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 90, 91, 21))
        self.label_9.setObjectName("label_9")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setGeometry(QtCore.QRect(610, 90, 481, 21))
        self.label_url.setObjectName("label_url")
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
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdsssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdsssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdsssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdsssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss fdssssssssssssssssssssssssssssssssssssssssss</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "文章列表"))
        self.label_2.setText(_translate("MainWindow", "標題:"))
        self.label_title.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "推:"))
        self.label_3.setText(_translate("MainWindow", "噓:"))
        self.label_good.setText(_translate("MainWindow", "TextLabel"))
        self.label_boo.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "作者:"))
        self.label_author.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "發表時間:"))
        self.label_date.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "原文連結:"))
        self.label_url.setText(_translate("MainWindow", "Ffdsfs"))
