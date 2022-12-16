from PyQt5 import QtWidgets
from Forms.PY import expenses_form
from DB import money_manager_db


class ExpensesForm(QtWidgets.QMainWindow, expenses_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.infoLbl.hide()
        self.addBtn.clicked.connect(self.add_record)
        self.clearFormBtn.clicked.connect(self.clear_forms)

    def add_record(self):
        self.infoLbl.show()

    def clear_forms(self):
        pass
