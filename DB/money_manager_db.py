from DB.conn_db import Database
from Windows.Utils import checks as ch
from datetime import datetime

class MoneyManagerDb():
    def __init__(self):
        self.conn, self.cursor = Database().connect_money_manager_db()

    def getCategories(self):
        self.cursor.execute("SELECT category_name from categories")
        list = self.cursor.fetchall()

        categories_list = []
        for tuple in list:
            categories_list.append(tuple[0])

        return categories_list

    def add_record(self, name, sum, date, category, flag):
        self.cursor.execute("SELECT id from categories where category_name = '{}'".format(category))
        category_id = int(self.cursor.fetchone()[0])
        data_tuple = (name, sum, date, category_id)

        if flag == 0:
            insert_expenses = """INSERT INTO expenses
                                (expense_name, expense_sum, expense_date, expense_category_id)
                                VALUES (?, ?, ?, ?);"""
            self.cursor.execute(insert_expenses, data_tuple)
        else:
            insert_profit = """INSERT INTO profits
                                (profit_name, profit_sum, profit_date, profit_category_id)
                                VALUES (?, ?, ?, ?);"""
            self.cursor.execute(insert_profit, data_tuple)

        self.conn.commit()

    def getAllRecords(self):
        self.cursor.execute("SELECT * from expenses")
        all_expenses = self.cursor.fetchall()

        self.cursor.execute("SELECT * from profits")
        all_profits = self.cursor.fetchall()

        all_profits = ch.tupleArr_ArrArr(all_profits)
        for profit in all_profits:
            profit[0] = str(profit[0]) + "p"

        all_records = all_expenses + all_profits

        result_array = ch.tupleArr_ArrArr(all_records)

        for record in result_array:
            record[2] = self.getCategoryName(record[2])

        result_array = sorted(result_array, reverse=True, key=lambda x:datetime.strptime(x[4],"%d.%m.%Y"))

        return result_array

    def getCategoryName(self, category_id):
        self.cursor.execute("SELECT category_name from categories where id = '{}'".format(category_id))
        return self.cursor.fetchone()[0]

    def getCostsAndCategories(self):
        self.cursor.execute("SELECT expense_sum, expense_category_id from expenses")
        result_array = self.cursor.fetchall()

        records = ch.tupleArr_ArrArr(result_array)

        categories_dict = {}

        for record in records:
            record[1] = self.getCategoryName(record[1])

            if record[1] in categories_dict:
                categories_dict[record[1]] += record[0]
            else:
                categories_dict[record[1]] = record[0]
        
        return categories_dict

    def getMonthReport(self):
        self.currentMonth = datetime.today().month
        result_sum = 0
        self.cursor.execute("SELECT expense_date, expense_sum from expenses")
        expenses = self.cursor.fetchall()
        expenses_array = ch.tupleArr_ArrArr(expenses)
        
        for expense in expenses_array:
            if expense[0].split(".")[1] == str(self.currentMonth):
                result_sum -= expense[1]

        self.cursor.execute("SELECT profit_date, profit_sum from profits")
        profits = self.cursor.fetchall()
        profits_array = ch.tupleArr_ArrArr(profits)

        for profit in profits_array:
            if profit[0].split(".")[1] == str(self.currentMonth):
                result_sum += profit[1]

        return result_sum, ch.getMonthName(self.currentMonth)
        
        
