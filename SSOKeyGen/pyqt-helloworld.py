import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets

from ssokeygen import Ui_MainWindow
from ssokeygendialog import Ui_Dialog


class MyApp(QMainWindow, Ui_MainWindow):
    parse_triggered = pyqtSignal()

    def __init__(self, parent=None, name=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

    def update(self):
        _translate = QtCore.QCoreApplication.translate
#         print(self.textBox.toPlainText())
        self.testLabel.setText(
            _translate("MainWindow", self.textBox.toPlainText()))

        my_dialog = Dialog(parent=self)
        my_dialog.show()


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, name=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

# class MyApp2(QMainWindow, Ui_Dialog):
#     parse_triggered = pyqtSignal()
#
#     def __init__(self, parent=None, name=None):
#         super(MyApp2, self).__init__(parent)
#         self.setupUi(self)
#
#     def accept(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.testLabel.setText(_translate("Dialog", "Accept Pushed!"))
#
#     def reject(self):
#         _translate = QtCore.QCoreApplication.translate
#         self.testLabel.setText(_translate("Dialog", "Reject Pushed!"))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
