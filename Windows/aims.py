from PyQt5 import QtWidgets
from Forms.PY import aims_form
from DB import money_manager_db


class AimsForm(QtWidgets.QMainWindow, aims_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 744)
        self.infoLbl.hide()
        