# Инкапсуляция, абстракция. (Магические, статичные, классновые методы в классах, множественное наследование.)


from abc import ABC, abstractmethod
import random

class Hero(ABC):

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #Защищенный атрибут
        self._luck = random.randint(0, 100)
        #приватный атрибут
        self.__crit_dmg = random.randint(0, 100)

    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f'Привет, {self.name}! \n Мой уровень: {self.lvl}')

    def status(self):
        return print(f'LVL: {self.lvl} \n HP: {self.hp}')

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} критический удар!')
        else:
            return print(f"{self.name} базовый удар!")

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} успешно защищается!")
        else:
            return print(f"{self.name} не смог защититься!")

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f'{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.hp}')

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass


"""""
hero = Hero("Боруто", 100, 1)
hero(hero._Hero__heal_hp()) 

hero.rest()
hero.protection()
hero.attack()
"""""

"""""
class ShieldHero(Hero):

    def __init__(self, name, hp, lvl, aura=0):
        super().__init__(name, hp, lvl)
        self.aura = aura

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} успешно защищается")
        else:
            self.aura +=100
            return print(f"{self.name}не смог защититься")

    def unique_attack(self):
        if self.aura >= 10:
            return print(f"{self.name} выполняет уникальную атаку!")
        else:
            return print(f"не хватает ауры")

    def unique_scream(self):
        if self.aura >= 1:
            return print(f"Датэбаё!!")

naofumi = ShieldHero("naofumi", 100, 1)
naofumi.rest()
"""""


#множественное наследование
# Python решает проблемы с помощью механизма порядка
#разрешения методов (Method Resolution Order, MRO)

#Животные
class Animal:
    def make_sound(self):
        return "Издает звук"
#Летающие
class Flyable:
    def move(self):
        return "Летит"
#Плавающие
class Swimmable:
    def move(self):
        return "Плавает"
#Утка
class Duck(Animal, Flyable, Swimmable):
    def make_sound(self):
        return "Кря-кря!"
print(Duck().make_sound())
print(Duck.__mro__)

#Алмазная проблема ()

class A:
    def speak(self):
        print(f"Я класс А")

class B(A):
    def speak(self):
        super().speak()
        print(f"Я класс B")

class C(A, B):
    def speak(self):
        super().speak()
        print(f"Я класс C")

class D(B, C): #D наследует от B и C
    def speak(self):
        super().speak()
        print(f"Я класс D")

d = D
d.speak()
print(D.__mro__)