import sys
from calc import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QtWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# logic
        self.ui.solutio_clc.clicked.connect(self.result)


if __name__=="main":
    app = QtWidgets.QApplacation(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
    