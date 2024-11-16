class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

    def validate(self, username, password):
        if  username in self.data:
            print("Такой пользователь уже существует")
            return False
        is_upper = is_digit= False
        while not is_upper and not is_digit and len(password) >= 3:
            for i in password:
                if i.isupper() and not is_upper :
                    is_upper = True
                elif i.isdigit() and not is_digit:
                    is_digit = True
        return is_upper and is_digit

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choise = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n")
        if choise == '1':
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Неверный пароль.")
            else:
                print("Пользователь не найден.")

        if choise == '2':
            user = User(input("Введите имя: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте ещё раз.")
                continue
            if database.validate(user.username,password):
                database.add_user(user.username, user.password)
                print("Успешная регистрация!")
                print(database.data) # для проверки
            else:
                print("Пароль слишком простой, придумайте другой")
                # choise = '2'
                print(database.data) # для проверки
                continue