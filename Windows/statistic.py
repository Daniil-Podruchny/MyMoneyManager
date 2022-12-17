from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QPushButton
from Forms.PY import statistic_form
from DB import money_manager_db


class StatisticForm(QtWidgets.QMainWindow, statistic_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.all_records = self.money_manager_db.getAllRecords()
        self.records_id = []

    def fill_statistic_table(self):
        current_records = self.money_manager_db.getAllRecords()

        statistic_table = self.statisticTable
        statistic_table.setColumnCount(6)

        statistic_table.setHorizontalHeaderLabels(["Название", "Категория", "Сумма", "Дата", "", ""])
        statistic_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        statistic_table.verticalHeader().setVisible(False)
        statistic_table.setShowGrid(False)

        for record in current_records:
            if record[0] not in self.records_id:
                self.records_id.append(record[0])

                flag = False if str(record[0]).isdigit() else True

                record = record[1:]
                self.addTableRow(statistic_table, record, flag)
            else:
                continue

    def addTableRow(self, table, row_data, flag):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0

        del_btn = QPushButton(table)
        del_btn.setText("Удалить")
        del_btn.setStyleSheet("QPushButton {background-color: rgb(170, 0, 0); border: 1px solid #094065; border-radius: 15px; padding: 5px; font-size: 15px; color: rgb(255,255,255)} QPushButton::hover {background-color: rgb(150, 0, 0)}")
        red_btn = QPushButton(table)
        red_btn.setText("Редактировать")
        red_btn.setStyleSheet("QPushButton {background-color: rgb(223, 152, 52); border: 1px solid #094065; border-radius: 15px; padding: 5px; font-size: 15px; color: rgb(255,255,255)} QPushButton::hover {	background-color: rgb(198, 141, 8);}")

        for item in row_data:
            cell = QTableWidgetItem(f"+{item}₽") if (col == 2 and flag) else QTableWidgetItem(f"-{item}₽") if (col == 2 and not flag) else QTableWidgetItem(str(item))

            cell.setFlags(QtCore.Qt.ItemIsEnabled)
            table.setItem(row, col, cell)
            col += 1

        table.setCellWidget(row, col, del_btn)
        table.setCellWidget(row, col + 1, red_btn)

