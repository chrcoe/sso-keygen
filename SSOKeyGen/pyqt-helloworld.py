import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets

from SSOKeyGen.ssokeygen import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    parse_triggered = pyqtSignal()

    def __init__(self, parent=None, name=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

#         _translate = QtCore.QCoreApplication.translate
#         self.menuTest.setTitle(_translate("MainWindow", "Test_NEW"))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
