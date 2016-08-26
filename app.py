#!/usr/bin/env python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow

class main(Ui_MainWindow):
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__()
		self.setupUi(MainWindow)
	
	# TODO: add your custom code, event handlers, etc. here.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    ui = main(MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

