#Задание - ( ООП - Инкапсуляция )

from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self, name = "Ю Бин", hp = 100):
        self.name = name
        self.hp = hp
        self.__random_action = random.choice([1, 2, 3]) #приватный атрибут

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}"

    def attack(self):
        self.hp -= 15
        return print(f"{self.name} атакует! Теперь здоровье: {self.hp}")

    def protection(self):
        return print(f"{self.name} защищается!")

    def rest(self):
        self.hp += 20
        return print(f"{self.name} отдыхает, восстанавливает силы. Здоровье: {self.hp}")

    def action(self):
        return  print(f"{self.name} выполняет действие.")

    @abstractmethod
    def action(self):
        pass
    def __random_action(self):
        return self.__random_action

"""""
hero = Hero("Ю Бин", 100)
print(hero.status())
print(hero.attack())
print(hero.protection())
print(hero.rest())
print(hero.action())
"""""
