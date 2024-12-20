#  Домашняя работа по уроку "Перегрузка операторов"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")
                break
            else:
                print(i)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if not isinstance(other,House):
            raise TypeError("other не является объектом класса House")
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise TypeError("other должно быть типом House")
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            print('вызов __add__')
            return House(self.name, self.number_of_floors + value)
        raise TypeError("value должно быть типом int")
    def __radd__(self, value):
            return self + value

    def __iadd__(self, value):
        if isinstance(value, int):
            print('вызов __iadd__')
            self.number_of_floors += value
            return self

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

h1 = House("ЖК Эверест", 10)
h2 = House("ЖК Новый Океан", 20)

print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
