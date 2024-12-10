

class Hero:

    def __init__(self, name ="Djahen", hp = 1000):
        self.name = name
        self.hp = hp

    def status(self):
        return f"Имя:{self.name}, Здоровье:{self.hp}"

    def rest(self):
        self.hp += 10
        return f"{self.name} отдыхает, восстанавливает здоровье. Теперь здоровье {self.hp}"

    def action(self):
        return f"{self.name} выполняет действие"

hero = Hero("Djahen")
print(hero.status())
print(hero.action())
print(hero.rest())


#наследование
class Warrior(Hero):

    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st

    def status(self):
        base_status = super().status()
        return f"{base_status} Стамина:{self.st}"

    def charge(self):
        if self.st >= 20:
            self.st -= 20
            self.hp += 40
            print(f"{self.name} совершает заряд, восстанавливает +40. Новое здоровье: {self.hp}")
        else:
            print(f"{self.name} Не хватает стамина для заряда.")

warrior = Warrior("Levi", 100, 100)
print(warrior.status())
print(warrior.charge())


class Mage(Hero):
    def __init__(self, name, hp, mn):
        super().__init__(name, hp)
        self.mn = mn

    def status(self):
        base_status = super().status()
        return f"{base_status}, Мана:{self.mn}"

    def teleport(self):
        if self.mn >= 35:
            self.mn -= 35
            print(f"{self.name} телепортируется. Осталось маны: {self.mn}")
        else:
            print(f"{self.name} не хватает маны для телепортации")

mage = Mage("Han Nam", 1000, 120)
print(mage.status())
print(mage.teleport())


class Archer(Hero):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def status(self):
        base_status = super().status()
        return f"{base_status}, Стрелы: {self.arrows}, Точность: {self.precision}"

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision > 50:
                print(f"{self.name} атакует стрелой. Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} промахнулся при атаке. Осталось стрел{self.arrows}")
        else:
            print(f"{self.name} не осталось стрел для атаки")
    def rest(self):
        self.arrows += 5
        return f"{self.name} отдыхает, восстанавливает +5 стрел. Всего стрел: {self.arrows}"

archer = Archer("Shelli", 100, 50, 110)
print(archer.status())
print(archer.attack())
print(archer.rest())
