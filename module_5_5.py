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
        while not is_upper and not is_digit and len(password) >= 8:
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
        user = User(input("Введите имя: "), password := input("Введите пароль: "),
                    password2 := input("Повторите пароль: "))
        if password != password2:
            exit()
        if database.validate(user.username,password):
            database.add_user(user.username, user.password)
            print(database.data)
        else:
            print(user.__dict__)
            print(database.data)
            continue
