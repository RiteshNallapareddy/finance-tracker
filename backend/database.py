import sqlite3
import os

# This gives us the absolute path to database.py's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Then we build the full path to finance.db
DB_PATH = os.path.join(BASE_DIR, 'finance.db')

# Function 1: Creates and returns a database connection
def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

# Function 2: Builds the database structure
def init_db():
    connection = get_db_connection()
    connection.execute (""" CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL,
                        category TEXT,
                        type TEXT, 
                        date TEXT,
                        description TEXT ) """)
    connection.execute(""" CREATE TABLE IF NOT EXISTS portfolio (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       stock_name TEXT,
                       symbol TEXT,
                       shares REAL,
                       purchase_price REAL,
                       purchase_date TEXT ) """)
    connection.commit()
    connection.close()