# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.solutio_clc = QtGui.QPushButton(self.centralwidget)
        self.solutio_clc.setGeometry(QtCore.QRect(110, 132, 180, 30))
        self.solutio_clc.setObjectName(_fromUtf8("solutio_clc"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 80, 360, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.number = QtGui.QLineEdit(self.splitter)
        self.number.setObjectName(_fromUtf8("number"))
        self.degree = QtGui.QLineEdit(self.splitter)
        self.degree.setObjectName(_fromUtf8("degree"))
        self.equals = QtGui.QLabel(self.splitter)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.result = QtGui.QLabel(self.splitter)
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.solutio_clc.setText(_translate("MainWindow", "solution", None))
        self.equals.setText(_translate("MainWindow", "=", None))

