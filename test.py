import sqlite3
import pandas as pd

conn = sqlite3.connect('DATA/intelligent_platform.db')

def create_table(conn):
    curr = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL) """
    curr.execute(sql)
    conn.commit()


def insert_user(conn, username, password_hash):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    curr.execute(sql, (username, password_hash))
    conn.commit()

def get_user(conn, username):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    curr.execute(sql, (username,))
    return curr.fetchone()

def delete_user(conn, username):
    curr = conn.cursor()
    sql = "DELETE FROM users WHERE username = ?"
    curr.execute(sql, (username,))
    conn.commit()

def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    return curr.fetchall()  

def migrate_users():
    with open('/Users/antoniusalx/VSCode/CW2_M01069559_CST1510/DATA/user.txt', 'r') as f:
        for line in f:
            username, password_hash = line.strip().split(',')
            insert_user(conn, username, password_hash)
    print("User data migration completed.")


def migrate_datasets_metadata(conn):
    df = pd.read_csv('/Users/antoniusalx/VSCode/CW2_M01069559_CST1510/DATA/datasets_metadata.csv')
    df.to_sql('datasets_metadata', conn, if_exists='replace', index=False)
    print("Datasets metadata migration completed.")

migrate_datasets_metadata(conn)
conn.close