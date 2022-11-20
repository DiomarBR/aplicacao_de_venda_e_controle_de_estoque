from file import Ui_Mercearia_do_Ziron
from produtos import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



a = int(input("didite algo:"))


if a == 1:
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
else:
    print("nao e isso")