from hashlib import md5

from files import read_users_file, add_user_to_file
from errors import NoMoreAttempts, RefuseToCreateNewUser


def hashed(s: str) -> str:
    return md5(s.encode()).hexdigest()


def get_user(users_filename: str) -> str:
    # прочитать файл с пользователями
    # если его нет, то создать | это будет сделано после логина
    users = read_users_file(users_filename)

    # запросить имя пользователя
    user = input(f"Введите имя пользователя: ")
    if user in users:
        # если имя есть - запросить пароль
        attempts = 5
        for _ in range(attempts):
            password = input(f"Введите пароль: ")
            if hashed(password) == users[user]:
                #  если пароль верный - вернуть имя
                return user
            else:
                #  если не верный - запросить ещё и вернуть имя если будет верный
                print(f"Неверный пароль. Попробуем ещё раз.")
        else:
            #  или исчерпать количество попыток
            raise NoMoreAttempts(f"Больше нет попыток. До свидания.")

    choice = input(f"Нет такого пользователя. Создадим? [Да/Нет] ")
    if choice == 'Нет':
        raise RefuseToCreateNewUser(f"Нельзя продолжать не создав этого пользователя. До свидания.")

    # если нет такого имени - то создать - записать имя и новый пароль
    for _ in range(5):
        password = input(f"Введите пароль: ")
        password_again = input(f"Введите пароль ещё раз: ")
        if password == password_again:
            users[user] = hashed(password)
            add_user_to_file(users_filename, user, hashed(password))
            break
        print(f"Введённые пароли не совпадают, попробуйте ещё раз")
    else:
        raise NoMoreAttempts(f"Больше нет попыток. До свидания.")
