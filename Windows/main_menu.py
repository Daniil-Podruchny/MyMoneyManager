from PyQt5 import QtWidgets
from Forms.PY import main_menu
from DB import money_manager_db
from . import expenses


class MainMenu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.expenses_form = expenses.ExpensesForm()
        self.showMenu()
        self.showExpensesFormBtn.clicked.connect(self.showExpensesForm)
        self.expenses_form.backMenuBtn.clicked.connect(self.showMenu)

    def showMenu(self):
        self.expenses_form.hide()
        self.show()

    def showExpensesForm(self):
        self.expenses_form.show()
        self.hide()
