import random
import string

# Генерация уникального email
def generate_email():
    digits = random.randint(100, 999)
    return f"stanislavgaiduked46{digits}@yandex.ru"

# Генерация пароля длиной не менее 6 символов
def generate_password(length=8):
    if length < 6:
        length = 6

    characters = string.ascii_letters + string.digits

    return "".join(
        random.choice(characters)
        for _ in range(length)
    )

# Генерация данных пользователя
def generate_user():
    return {
        "name": "Stanislav",
        "email": generate_email(),
        "password": generate_password(),
    }
