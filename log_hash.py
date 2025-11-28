import bcrypt
import sqlite3
import pandas as pd
from pathlib import Path

USER_FILE = Path(__file__).parent / 'user.txt'


def hash_password(password: str) -> str:
    """Hash a plaintext password and return the decoded hash string."""
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    pw_hash = bcrypt.hashpw(binary_password, salt)
    return pw_hash.decode('utf-8')


def validate_hash(password: str, password_hash: str) -> bool:
    """Validate a plaintext password against the stored hash."""
    bin_pwd = password.encode('utf-8')
    bin_hash = password_hash.encode('utf-8')
    return bcrypt.checkpw(bin_pwd, bin_hash)


def register_user():
    user_name = input("Enter username: ")
    user_pwd = input("Enter password: ")
    password_hash = hash_password(user_pwd)
    USER_FILE.write_text(USER_FILE.read_text() + f"{user_name},{password_hash}\n") if USER_FILE.exists() else USER_FILE.write_text(f"{user_name},{password_hash}\n")


def login_user() -> bool:
    user_name = input("Enter username: ")
    user_pwd = input("Enter password: ")
    if not USER_FILE.exists():
        return False

    with open(USER_FILE, "r") as f:
        users = f.readlines()

    for user in users:
        try:
            name, password_hash = user.strip().split(",")
        except ValueError:
            continue

        if user_name == name:
            return validate_hash(user_pwd, password_hash)
    return False






conn = sqlite3.connect('DATA/intelligent_platform.db')
#migrating_it_tickets(conn)
#migrating_datasets_metadata(conn)
#migrating_cyber_incidents(conn)
conn.close()