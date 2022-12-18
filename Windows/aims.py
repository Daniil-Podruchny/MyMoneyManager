from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate
from Forms.PY import aims_form
from .Utils import checks as ch
from DB import money_manager_db


class AimsForm(QtWidgets.QMainWindow, aims_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 744)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.infoLbl.hide()
        self.currentDate = QDate.currentDate()
        self.array_of_ids = []
        self.aimDateEdit.setDate(self.currentDate)
        self.fill_aim_table()
        self.clearFormBtn.clicked.connect(self.clear_forms)
        self.addAimBtn.clicked.connect(self.add_aim_record)
        self.deleteAimBtn.clicked.connect(self.delete_aim_record)
        self.redactAimBtn.clicked.connect(self.redact_aim_record)

    def add_aim_record(self):
        aimName = self.aimNameEdit.text()
        aimSum = self.aimSumEdit.text()
        aimDate = self.aimDateEdit.text()
        if not ch.isEmpty(self, aimName, aimSum, aimDate) and ch.isCorrectSum(self, aimSum):
                self.money_manager_db.add_aim_record(aimName, aimSum, aimDate)
                self.infoLbl.show()
                self.fill_aim_table()
                self.clear_forms()
                QtCore.QTimer.singleShot(2000, lambda: self.infoLbl.hide())

    def fill_aim_table(self):
        aims = self.money_manager_db.getAims()

        for aim in aims:
            if aim[0] not in self.array_of_ids:
                self.array_of_ids.append(aim[0])
                self.aimList.addItem(f"Id: {aim[0]}\tНазвание: {aim[1]}\tсумма: {aim[2]}\tдо {aim[3]}")

    def clear_forms(self):
        self.aimNameEdit.clear()
        self.aimSumEdit.clear()
        self.aimDateEdit.setDate(self.currentDate)

    def delete_aim_record(self):
        listItems=self.aimList.selectedItems()
        if ch.isSelected(self, listItems):
            return
        else:        
            for item in listItems:
                id = int(self.aimList.currentItem().text().split("\t")[0].split(" ")[1])
                self.money_manager_db.delete_aim_record(id)
                self.aimList.takeItem(self.aimList.row(item))

    def redact_aim_record(self):
        pass
        