import json

login_input = input("Введите логин: ")
passwd_input = input("Введите пароль: ")


def register(login, passwd):
    with open("users.json", "r") as file:
        data_users = json.load(file)

    if login not in data_users:
        if passwd:
            data_users[login] = passwd

            with open("users.json", "w") as file:
                json.dump(data_users, file)

            print("Пользователь успешно добавлен")
        else:
            print("Надо указать пароль")
    else:
        print("Логин уже занят")


def login(login, passwd):
    with open("users.json", "r") as file:
        data_users = json.load(file)

    if login in data_users:
        if data_users[login] == passwd:
            print("Пользователь успешно авторизовался")
        else:
            print("Неправильный пароль")
    else:
        print("Такого пользователя не существует")


register(login_input, passwd_input)
login(login_input, passwd_input)
