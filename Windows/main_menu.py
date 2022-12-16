from PyQt5 import QtWidgets
from Forms.PY import main_menu


class MainMenu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMenu()

    def showMenu(self):
        self.show()
