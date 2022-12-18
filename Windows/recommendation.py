from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from Forms.PY import recomendation_form
from .Utils import checks as ch
from DB import money_manager_db


class RecomendationForm(QtWidgets.QMainWindow, recomendation_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        