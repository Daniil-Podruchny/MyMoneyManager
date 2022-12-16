from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate
from Forms.PY import expenses_form
from DB import money_manager_db
from .Utils import checks as ch


class ExpensesForm(QtWidgets.QMainWindow, expenses_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        categories = self.money_manager_db.getCategories()
        self.expenseCategoryComboBox.addItems(categories[:9])
        self.profitCategoryEdit.addItems(categories[9:])
        self.currentDate = QDate.currentDate()
        self.expenseDateEdit.setDate(self.currentDate)
        self.profitDateEdit.setDate(self.currentDate)
        self.infoLbl.hide()
        self.addBtn.clicked.connect(self.add_record)
        self.clearFormBtn.clicked.connect(self.clear_forms)

    def add_record(self):
        if self.ControllMoneyTab.currentIndex() == 0:
            expenseName = self.expenseNameEdit.text()
            expenseSum = self.ExpenseSumEdit.text()
            expenseDate = self.expenseDateEdit.text()
            expenseCategory = self.expenseCategoryComboBox.currentText()
            if not ch.isEmpty(self, expenseName, expenseSum, expenseDate) and ch.isCorrectSum(self, expenseSum):
                    self.money_manager_db.add_record(expenseName, expenseSum, expenseDate, expenseCategory, 0)
                    self.infoLbl.show()
                    self.clear_forms()
                    QtCore.QTimer.singleShot(2000, lambda: self.infoLbl.hide())
        else:
            profitName = self.profitNameEdit.text()
            profitSum = self.profitSumEdit.text()
            profitDate = self.profitDateEdit.text()
            profitCategory = self.profitCategoryEdit.currentText()
            if not ch.isEmpty(self, profitName, profitSum, profitDate) and ch.isCorrectSum(self, profitSum):
                self.money_manager_db.add_record(profitName, profitSum, profitDate, profitCategory, 1)
                self.infoLbl.show()
                self.clear_forms()
                QtCore.QTimer.singleShot(2000, lambda: self.infoLbl.hide())

    def clear_forms(self):
        if self.ControllMoneyTab.currentIndex() == 0:
            self.expenseNameEdit.clear()
            self.ExpenseSumEdit.clear()
            self.expenseDateEdit.setDate(self.currentDate)
        else:
            self.profitNameEdit.clear()
            self.profitSumEdit.clear()
            self.profitDateEdit.setDate(self.currentDate)
