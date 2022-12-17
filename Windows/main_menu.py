from PyQt5 import QtWidgets
from Forms.PY import main_menu
from DB import money_manager_db
from .Utils import mplwidget
from . import expenses, statistic


class MainMenu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.expenses_form = expenses.ExpensesForm()
        self.statistic_form = statistic.StatisticForm()
        self.diagram = mplwidget.MplWidget()
        self.showMenu()
        self.showExpensesFormBtn.clicked.connect(self.showExpensesForm)
        self.showStatisticFormBtn.clicked.connect(self.showStatisticForm)
        self.expenses_form.backMenuBtn.clicked.connect(self.showMenu)
        self.statistic_form.backMenuBtn.clicked.connect(self.showMenu)

    def showMenu(self):
        self.expenses_form.hide()
        self.statistic_form.hide()
        self.show()

    def showExpensesForm(self):
        self.expenses_form.show()
        self.hide()

    def showStatisticForm(self):
        self.hide()
        self.statistic_form.show()

        self.refresh_diagram()
        self.statistic_form.fill_statistic_table()

    def refresh_diagram(self):
        self.statistic_form.MplWidget.canvas.ax.clear()

        categories_dict = self.money_manager_db.getCostsAndCategories()
        self.statistic_form.MplWidget.canvas.ax.pie(list(categories_dict.values()), labels=list(categories_dict))

        self.statistic_form.MplWidget.canvas.draw()

