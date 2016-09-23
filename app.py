#!/usr/bin/env python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon, QApplication # tray classes
from AuthWindow import Ui_AuthWindow as UI

import systray_rc

class main(UI):
	def __init__(self, parent=None):
		super(UI, self).__init__()
		self.setupUi(parent)
		self.parent = parent
		
		#print type(self).__name__
		print self.lUsername
		
		#self.minimizeAction = QAction("Mi&nimize", parent, triggered=parent.hide)
		self.createActions()
		self.createTrayIcon()
		self.setIcon(QIcon(':/images/heart.png'))
		self.trayIcon.show()
		
		# setup gui events
		self.events()
	
	def createActions(self):
		#self.minimizeAction = QAction("Mi&nimize", self.parent, triggered=self.parent.hide)
		#self.maximizeAction = QAction("Ma&ximize", self.parent, triggered=self.parent.showMaximized)
		#self.restoreAction = QAction("&Restore", self.parent, triggered=self.parent.showNormal)
		self.quitAction = QAction("&Quit", self.parent, triggered=QApplication.instance().quit)

	def createTrayIcon(self):
		self.trayIconMenu = QMenu(self.parent)
		#self.trayIconMenu.addAction(self.minimizeAction)
		#self.trayIconMenu.addAction(self.maximizeAction)
		#self.trayIconMenu.addAction(self.restoreAction)
		#self.trayIconMenu.addSeparator()
		self.trayIconMenu.addAction(self.quitAction)

		self.trayIcon = QSystemTrayIcon(self.parent)
		self.trayIcon.setContextMenu(self.trayIconMenu)

	def setIcon(self, icon):
		self.trayIcon.setIcon(icon)
		self.parent.setWindowIcon(icon)

	def events(self):
		self.bCancelOk.button(self.bCancelOk.Ok).clicked.connect(QApplication.instance().quit)
		self.bCancelOk.button(self.bCancelOk.Cancel).clicked.connect(QApplication.instance().quit)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	if not QSystemTrayIcon.isSystemTrayAvailable():
		QMessageBox.critical(None, "Systray",
			"I couldn't detect any system tray on this system.")
		sys.exit(1)

	QtWidgets.QApplication.setQuitOnLastWindowClosed(False)

	#win = QtWidgets.QMainWindow()
	win = QtWidgets.QDialog()
	#ui = Ui_MainWindow()
	ui = main(win)
	#ui.minimizeAction = QAction("Mi&nimize", win, triggered=win.hide)
	#ui.setupUi(MainWindow)
	win.show()
	sys.exit(app.exec_())

