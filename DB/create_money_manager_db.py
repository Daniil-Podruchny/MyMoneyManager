import sqlite3


def create_db():
    conn = sqlite3.connect('C:\\Users\\79680\\OneDrive\\Рабочий стол\\CourseWork\\MyMoneyManager\\DB\\money_manager_db.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE expenses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT 
                            , expense_name TEXT NOT NULL							
                            , expense_category_id INTEGER NOT NULL
                            , expense_sum INTEGER NOT NULL
                            , expense_date TEXT NOT NULL
                            , FOREIGN KEY (expense_category_id) REFERENCES categories(category_id)				
                            )''')

    cursor.execute('''CREATE TABLE profits (
                            id INTEGER PRIMARY KEY AUTOINCREMENT 
                            , profit_name TEXT NOT NULL							
                            , profit_category_id INTEGER NOT NULL
                            , profit_sum INTEGER NOT NULL
                            , profit_date TEXT NOT NULL
                            , FOREIGN KEY (profit_category_id) REFERENCES categories(category_id)					
                            )''')

    cursor.execute('''CREATE TABLE categories (
                            id INTEGER PRIMARY KEY AUTOINCREMENT 
                            , category_id INTEGER NOT NULL								
                            , category_name TEXT								
                            )''')
    
    return conn, cursor