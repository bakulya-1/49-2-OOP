#Тема №1. OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов, Принцип ООП - Наследование.

class Car:

    def __init__(self, this_model, this_year, this_color):
# атрибуты класса/Field
        self.model = this_model
        self.year = this_year
        self.color = this_color

#print(car_bmw)
#print(car_bmw.model)
#str = "dasdas"

#Метод класса
def sigma(self):
    print(f"{self.model}signal!")

def max_speed(self):
    if self.model == "BMW":
        print("Супер быстрая машина")
    else:
        print("быстрая")

#Экземпляр класса
car_bmw = Car("BMW x5", 2004, 'silver')
car_honda = Car("Fit", 2004, 'Red')

car_bmw.signal()
car_bmw.max_speed()
car_honda.signal()
car_honda.max.speed()









