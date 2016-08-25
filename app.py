#!/usr/bin/env python

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow

class MainWindow(Ui_MainWindow):
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__()
		self.setupUi(self)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
		
	form = MainWindow()
	form.show()
				
	sys.exit(app.exec_())
