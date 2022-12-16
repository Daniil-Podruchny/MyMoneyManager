from . import create_money_manager_db
from DB.conn_db import Database
import os
import sqlite3

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
        
