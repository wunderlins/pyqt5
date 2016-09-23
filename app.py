#!/usr/bin/env python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from AuthWindow import Ui_AuthWindow as UI

class main(UI):
	def __init__(self, parent=None):
		super(UI, self).__init__()
		self.setupUi(win)
		
	# TODO: add your custom code, event handlers, etc. here.
	def handleReturn(self):
		print "ouch"

	def handleTextChange(self, text):
		self.lineEdit_2.setText(text)
		print text

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    ui = main(win)
    #ui.setupUi(MainWindow)
    win.show()
    sys.exit(app.exec_())

