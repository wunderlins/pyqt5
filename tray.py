#!/usr/bin/env python

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout)

import systray_rc

class Window(QDialog):
	def __init__(self):
		super(Window, self).__init__()

		#self.createIconGroupBox()
		#self.createMessageGroupBox()

		self.durationLabel = QLabel("Duration:")
		self.iconLabel = QLabel("Icon:")
		self.iconComboBox = QComboBox()
		self.iconComboBox.addItem(QIcon(':/images/bad.png'), "Bad")
		self.iconComboBox.addItem(QIcon(':/images/heart.png'), "Heart")
		self.iconComboBox.addItem(QIcon(':/images/trash.png'), "Trash")

		self.iconLabel.setMinimumWidth(self.durationLabel.sizeHint().width())

		self.createActions()
		self.createTrayIcon()

		"""
		self.showMessageButton.clicked.connect(self.showMessage)
		self.showIconCheckBox.toggled.connect(self.trayIcon.setVisible)
		self.iconComboBox.currentIndexChanged.connect(self.setIcon)
		"""
		self.trayIcon.messageClicked.connect(self.messageClicked)
		self.trayIcon.activated.connect(self.iconActivated)

		#mainLayout = QVBoxLayout()
		#self.setLayout(mainLayout)

		self.iconComboBox.setCurrentIndex(1)
		self.setIcon(1)
		self.trayIcon.show()

		self.setWindowTitle("Systray")
		self.resize(400, 300)

		
	def setIcon(self, index):
		icon = self.iconComboBox.itemIcon(index)
		self.trayIcon.setIcon(icon)
		self.setWindowIcon(icon)

		self.trayIcon.setToolTip(self.iconComboBox.itemText(index))

	def createActions(self):
		self.minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
		self.maximizeAction = QAction("Ma&ximize", self,
			triggered=self.showMaximized)
		self.restoreAction = QAction("&Restore", self,
			triggered=self.showNormal)
		self.quitAction = QAction("&Quit", self,
			triggered=QApplication.instance().quit)

	def createTrayIcon(self):
		self.trayIconMenu = QMenu(self)
		self.trayIconMenu.addAction(self.minimizeAction)
		self.trayIconMenu.addAction(self.maximizeAction)
		self.trayIconMenu.addAction(self.restoreAction)
		self.trayIconMenu.addSeparator()
		self.trayIconMenu.addAction(self.quitAction)

		self.trayIcon = QSystemTrayIcon(self)
		self.trayIcon.setContextMenu(self.trayIconMenu)

	def iconActivated(self, reason):
		sys.stdout.write("ouch\n")
		if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
			self.iconComboBox.setCurrentIndex(
					(self.iconComboBox.currentIndex() + 1)
					% self.iconComboBox.count())
		elif reason == QSystemTrayIcon.MiddleClick:
			self.showMessage()


	def messageClicked(self):
		QMessageBox.information(None, "Systray",
				"Sorry, I already gave what help I could.\nMaybe you should "
				"try asking a human?")
	
if __name__ == '__main__':

    app = QApplication(sys.argv)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
	# do not show window, only display tray
    #window.show()
    sys.exit(app.exec_())