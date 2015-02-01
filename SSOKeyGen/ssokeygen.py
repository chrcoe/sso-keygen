# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssokeygen.ui'
#
# Created: Sun Feb  1 12:54:41 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(550, 550, 230, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.buttonUpdate = QtWidgets.QPushButton(self.splitter)
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.buttonClear = QtWidgets.QPushButton(self.splitter)
        self.buttonClear.setObjectName("buttonClear")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(280, 120, 256, 213))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.textBox = QtWidgets.QPlainTextEdit(self.splitter_2)
        self.textBox.setObjectName("textBox")
        self.testLabel = QtWidgets.QLabel(self.splitter_2)
        self.testLabel.setObjectName("testLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 29))
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
        self.buttonUpdate.clicked.connect(MainWindow.update)
        self.buttonClear.clicked.connect(self.testLabel.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hello World"))
        self.buttonUpdate.setText(_translate("MainWindow", "Update"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.testLabel.setText(_translate("MainWindow", "TextLabel"))
        self.menuTest.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))

