from PyQt5 import QtWidgets
from Forms.PY import statistic_form
from DB import money_manager_db


class StatisticForm(QtWidgets.QMainWindow, statistic_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
