from . import create_money_manager_db
from DB.conn_db import Database
import os
import sqlite3

class MoneyManagerDb():
    def __init__(self):
        self.conn, self.cursor = Database().connect_money_manager_db()
        
