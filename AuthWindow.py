# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ad/ad/dialog.ui'
#
# Created: Fri Sep 23 14:33:00 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon 

class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.resize(267, 100)
        self.formLayoutWidget = QtWidgets.QWidget(AuthWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lUsername = QtWidgets.QLabel(self.formLayoutWidget)
        self.lUsername.setObjectName("lUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lUsername)
        self.tUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tUsername.setObjectName("tUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tUsername)
        self.lPassword = QtWidgets.QLabel(self.formLayoutWidget)
        self.lPassword.setObjectName("lPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lPassword)
        self.tPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tPassword.setObjectName("tPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tPassword)
        self.bCancelOk = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.bCancelOk.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bCancelOk.setObjectName("bCancelOk")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bCancelOk)
        
        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Dialog"))
        self.lUsername.setText(_translate("AuthWindow", "Username"))
        self.lPassword.setText(_translate("AuthWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthWindow = QtWidgets.QDialog()
    ui = Ui_AuthWindow()
    ui.setupUi(AuthWindow)
    AuthWindow.show()
    sys.exit(app.exec_())

