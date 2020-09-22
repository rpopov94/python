import sys
from calc import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QtWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# logic
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
    