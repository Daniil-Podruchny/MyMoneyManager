from PyQt5 import QtWidgets
from Forms.PY import main_menu
from DB import money_manager_db


class MainMenu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.showMenu()

    def showMenu(self):
        self.show()
