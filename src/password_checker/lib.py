"""
lib.py
"""

import random
import string
import hashlib


def is_strong_password(password: str) -> bool:
    """
      - довжина не менше 8 символів;
      - містить хоча б одну велику літеру;
      - містить хоча б одну малу літеру;
      - містить хоча б одну цифру;
      - містить хоча б один спеціальний символ.
    """
    if len(password) < 8:
        return False

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)

    return has_upper and has_lower and has_digit and has_special


def generate_random_password(length: int = 12) -> str:
    if length < 4:
        length = 4

    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password_chars)
    return "".join(password_chars)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()