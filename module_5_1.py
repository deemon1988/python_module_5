#  Домашняя работа по уроку "Атрибуты и методы объекта"

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


h1 = House('ЖК Новый', 30)
h2 = House("Загородный Дом", 2)

h1.go_to(8)
h2.go_to(5)
