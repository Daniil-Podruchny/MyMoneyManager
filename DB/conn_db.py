from DB import create_money_manager_db

import os
import sqlite3

def conn_money_manager_db():
    db_path = 'C:\\Users\\79680\\OneDrive\\Рабочий стол\\CourseWork\\MyMoneyManager\\DB\\money_manager_db.db'
    if not db_path:
        raise Exception('Path money_manager_db is empty. See config')	

    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))
    
    conn = None
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

    else:
        conn, cursor = create_money_manager_db.create_db()
    
    return conn, cursor


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    money_manager_conn = None
    
    def connect_money_manager_db(self):
        if self.money_manager_conn is None:
            self.money_manager_conn, self.money_manager_cursor = conn_money_manager_db()
        return self.money_manager_conn, self.money_manager_cursor
