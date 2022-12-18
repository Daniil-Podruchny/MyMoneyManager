from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
from Forms.PY import aims_form
from .Utils import checks as ch
from DB import money_manager_db
from . import redact


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
                self.aimList.addItem(f"Id: {aim[0]}\tНазвание: {aim[1]}\tсумма: {aim[2]}\tдо: {aim[3]}")

    def clear_forms(self):
        self.aimNameEdit.clear()
        self.aimSumEdit.clear()
        self.aimDateEdit.setDate(self.currentDate)

    def delete_aim_record(self):
        listItems = self.aimList.selectedItems()
        if ch.isSelected(self, listItems):
            return
        else:        
            for item in listItems:
                button = QMessageBox.question( self, 'Подтверждение', 'Вы уверены что хотите удалить запись?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No )
                if button == QMessageBox.StandardButton.Yes:
                    id = int(self.aimList.currentItem().text().split("\t")[0].split(" ")[1])
                    self.money_manager_db.delete_aim_record(id)
                    self.aimList.takeItem(self.aimList.row(item))

    def clear_row(self):
        listItems = self.aimList.selectedItems()
        if ch.isSelected(self, listItems):
            return
        else:
            for item in listItems:
                self.aimList.takeItem(self.aimList.row(item))

    def redact_aim_record(self):
        self.redact_form = redact.RedactForm()
        self.redact_form.cancelRedactBtn.clicked.connect(self.destroyRedactWindow)
        result_redact_array = []

        listItems = self.aimList.selectedItems()
        if ch.isSelected(self, listItems):
            return
        else:
            for item in listItems:
                array_to_redact = self.aimList.currentItem().text().split("\t")

                for el in array_to_redact:
                    result_redact_array.append(el.split(": ")[1])

                self.redact_form.saveChangeBtn.clicked.connect(lambda: self.updateAimRecord(result_redact_array[0]))

                self.redact_form.aimChgNameEdit.setText(result_redact_array[1])
                self.redact_form.aimChgSumEdit.setText(result_redact_array[2])
                self.redact_form.aimChgDateEdit.setDate(QDate.fromString(result_redact_array[3], "dd.MM.yyyy"))

                self.redact_form.show()
                self.hide()
        
    def destroyRedactWindow(self):
        self.show()
        self.redact_form.close()

    def updateAimRecord(self, id):
        new_aim_name = self.redact_form.aimChgNameEdit.text()
        new_aim_sum = self.redact_form.aimChgSumEdit.text()
        new_aim_date = self.redact_form.aimChgDateEdit.text()

        if not ch.isEmpty(self, new_aim_name, new_aim_sum, new_aim_date) and ch.isCorrectSum(self, new_aim_sum):
                self.redact_form.infoLbl.show()
                self.money_manager_db.update_aim_record(id, new_aim_name, new_aim_sum, new_aim_date)
                self.clear_row()
                self.array_of_ids.remove(int(id))
                self.fill_aim_table()
                self.destroyRedactWindow()

