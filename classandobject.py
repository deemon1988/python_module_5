class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_info(self):
        print(f'Привет, меня завут {self.name}, мне {self.age} лет')
    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')
    def __del__(self):
        print(f'{self.name} ушел')
    def __len__(self):
        return self.age

dim = Human('Дмитрий', 35)
den = Human('Денис', 35)
dim.say_info()
den.say_info()

del dim
den.birthday()
input()
print(len(den))