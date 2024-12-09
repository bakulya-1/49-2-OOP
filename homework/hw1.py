
#Создание класса Person

class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")

Person1 = Person("Эмили", 20, "Франция")
Person1.introduce()



#Задание 2. Методы класса
class Person:

    def __int__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")

    def is_adult(self):
            if self.age >= 18:
                return True
            else:
                return False
person1 = Person("Энни", 15, "Кореи")
person2 = Person("Хан Нам", 22, "Японии")

print(person1.is_adult())
print(person2.is_adult())


#Задание 3. Модификация и использование __str__ и __init__

class Person:

    def __int__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мне {self.age}, я живу в {self.city}")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def __str__(self):
        return f"Имя: {self.name}, Возраст:{self.age}, Город:{self.city}"
person1 = Person("Эмили", 20, "Франции")

print(person1)







