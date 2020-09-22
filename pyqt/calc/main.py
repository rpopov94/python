import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.solutio_clc = QtWidgets.QPushButton(self.centralwidget)
        self.solutio_clc.setGeometry(QtCore.QRect(110, 132, 180, 30))
        self.solutio_clc.setObjectName("solutio_clc")
        self.number = QtWidgets.QLineEdit(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(50, 80, 142, 25))
        self.number.setObjectName("number")
        self.degree = QtWidgets.QLineEdit(self.centralwidget)
        self.degree.setGeometry(QtCore.QRect(218, 80, 142, 25))
        self.degree.setObjectName("degree")
        self.equals = QtWidgets.QLabel(self.centralwidget)
        self.equals.setGeometry(QtCore.QRect(385, 80, 16, 17))
        self.equals.setObjectName("equals")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(400, 80, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setItalic(True)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.solutio_clc.setText(_translate("MainWindow", "solution"))
        self.equals.setText(_translate("MainWindow", "="))


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QtWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.solutio_clc.clicked.connect(self.result)
    def result(self):
        try:
            n1 = self.ui.number.text()
            n2 = int(self.ui.degree.text())
            s = int(n1, n2)
            self.ui.lblSum.setText(str(s))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTititle("Input error")
            msg.setText("Input corret data!")
            msg.SetIcon(msg.Warning)
            msg.exec()


if __name__=="main":
    app = QtWidgets.QApplacation(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
