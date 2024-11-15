class Human:
    head = True
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
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    def __bool__(self):
        return bool(self.age)
    def __str__(self):
        return f'{self.name}'

if __name__ == "__main__":
    dim = Human('Дмитрий', 35)
    den = Human('Денис', 35)
    dim.say_info()
    den.say_info()
    if den:
        den.say_info()
    print(den)
    print(dim == den)
    den.birthday()
    print(dim<den)

    #del dim

    #input()
    print(len(den))

