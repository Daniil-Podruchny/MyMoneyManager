from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate
from Forms.PY import redact_form
from .Utils import checks as ch
from DB import money_manager_db


class RedactForm(QtWidgets.QMainWindow, redact_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.infoLbl.hide()
        self.currentDate = QDate.currentDate()
        self.aimChgDateEdit.setDate(self.currentDate)
