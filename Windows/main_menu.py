from PyQt5 import QtWidgets
from Forms.PY import main_menu
from DB import money_manager_db
from .Utils import mplwidget
from . import expenses, statistic, aims, recommendation


class MainMenu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(798, 600)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.expenses_form = expenses.ExpensesForm()
        self.statistic_form = statistic.StatisticForm()
        self.aims_form = aims.AimsForm()
        self.recomendation_form = recommendation.RecomendationForm()
        self.diagram = mplwidget.MplWidget()
        self.showMenu()
        self.showExpensesFormBtn.clicked.connect(self.showExpensesForm)
        self.showStatisticFormBtn.clicked.connect(self.showStatisticForm)
        self.showAimsFormBtn.clicked.connect(self.showAimsForm)
        self.showRecommendationFormBtn.clicked.connect(self.showRecomendationForm)
        self.expenses_form.backMenuBtn.clicked.connect(self.showMenu)
        self.statistic_form.backMenuBtn.clicked.connect(self.showMenu)
        self.aims_form.backMenuBtn.clicked.connect(self.showMenu)
        self.recomendation_form.backMenuBtn.clicked.connect(self.showMenu)

    def showMenu(self):
        self.expenses_form.hide()
        self.statistic_form.hide()
        self.aims_form.hide()
        self.show()

    def showExpensesForm(self):
        self.expenses_form.show()
        self.hide()

    def showStatisticForm(self):
        self.hide()
        self.statistic_form.show()

        self.refresh_diagram()
        self.statistic_form.fill_statistic_table()
        self.setMonthReport()
    
    def showAimsForm(self):
        self.hide()
        self.aims_form.show()

    def showRecomendationForm(self):
        self.hide()
        self.recomendation_form.show()

    def refresh_diagram(self):
        self.statistic_form.MplWidget.canvas.ax.clear()

        categories_dict = self.money_manager_db.getCostsAndCategories()
        self.statistic_form.MplWidget.canvas.ax.pie(list(categories_dict.values()), labels=list(categories_dict))

        self.statistic_form.MplWidget.canvas.draw()

    def setMonthReport(self):
        sum, month = self.money_manager_db.getMonthReport()
        if sum > 0: 
            sum = f"+{sum}"
            self.statistic_form.resultLbl.setStyleSheet("background-color: rgb(0, 179, 255); color: rgb(255, 255, 255); border: 1px solid #094065; border-radius: 19px; padding: 10px; font-size: 20px;")
            self.statistic_form.resultLbl.setText(f"Итог за {month}: {sum}₽")
        else:
            self.statistic_form.resultLbl.setStyleSheet("background-color: rgb(150, 0, 0); color: rgb(255, 255, 255); border: 1px solid #094065; border-radius: 19px; padding: 10px; font-size: 20px;")
            self.statistic_form.resultLbl.setText(f"Итог за {month}: {sum}₽")


