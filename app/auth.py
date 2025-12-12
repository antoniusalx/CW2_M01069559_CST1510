from pathlib import Path
from typing import Tuple

from log_hash import validate_hash, hash_password


USER_FILE = Path(__file__).resolve().parents[1] / 'user.txt'


def authenticate(username: str, password: str) -> bool:
    """Return True if username/password are valid."""
    if not USER_FILE.exists():
        return False
    with USER_FILE.open('r') as f:
        for line in f:
            try:
                name, password_hash = line.strip().split(',', 1)
            except ValueError:
                continue
            if name == username:
                return validate_hash(password, password_hash)
    return False


def register(username: str, password: str) -> bool:
    """Register a new user. Returns False if user already exists, True on success."""
    if USER_FILE.exists():
        with USER_FILE.open('r') as f:
            for line in f:
                if not line.strip():
                    continue
                name = line.strip().split(',', 1)[0]
                if name == username:
                    return False

    hashed = hash_password(password)
    USER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with USER_FILE.open('a') as f:
        f.write(f"{username},{hashed}\n")
    return True
