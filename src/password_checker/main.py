"""
main.py
"""

from lib import is_strong_password, generate_random_password, hash_password


def main():
    test_passwords = ["12345678", "password", "Str0ng!Pass"]

    print("=== Перевірка паролів на надійність ===")
    for pwd in test_passwords:
        result = "надійний" if is_strong_password(pwd) else "ненадійний"
        print(f'Пароль "{pwd}" -> {result}')

    print("\n=== Генерація нового пароля ===")
    new_password = generate_random_password(12)
    print(f"Згенерований пароль: {new_password}")
    print(f"Перевірка сили: {'надійний' if is_strong_password(new_password) else 'ненадійний'}")

    print("\n=== Хешування пароля ===")
    hashed = hash_password(new_password)
    print(f"SHA-256 хеш: {hashed}")


if __name__ == "__main__":
    main()