# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssokeygen.ui'
#
# Created: Sun Feb  1 21:30:51 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(80, 150, 269, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.textBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBox.setGeometry(QtCore.QRect(90, 43, 256, 41))
        self.textBox.setObjectName("textBox")
        self.testLabel = QtWidgets.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(90, 90, 251, 21))
        self.testLabel.setObjectName("testLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 29))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuTest.addAction(self.actionClose)
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hello World"))
        self.testLabel.setText(_translate("MainWindow", "TextLabel"))
        self.menuTest.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))

