import sqlite3

def get_db_connection():
    conn = sqlite3.connect('DATA/intelligent_platform.db')
    return conn