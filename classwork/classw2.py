#Наследование и полиморфизм
# Базовый\Супер\Родительский

"""""
class Hero:
    def __init__(self, name="John Doe", hp=100):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp += 10
        return f"{self.name}, восстанавливает здоровье на +10 HP^{self.hp}"

    def action(self):
        return  f"{self.name} делает базовое действие"

hero = Hero("Kirtito")

print(hero.action())
#print(hero.)

#наследование
class Warrior(Hero):

    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 10
            return f"{self.name} Превращается в Алмаза"
        else:
            return f"{self.name} стамина меньше 10"

 hero_warrior = Warrior("Ben-10", 1000, 100)

#print(hero_warrior.rest())
print(hero_warrior.action())

class Mege(Hero):

    def __init__(self, name, hp, mp):
        super().__init__(name,hp)
        self.mp = mp

    def rest(self):
        return f"{self.name}, восстанавливает ману на +10 MP^{self.mp}"

    def attack(self):
        if self.mp >= 10:
            self.mp -=10
            return f"{self.name} Колдует огненный шар"
        else:
            return f"{self.name} Мана меньше 10"


    def action(self):
        old_action = super().action()
        attack = self.attack()

        return f"{old_action} {attack}"
"""""

"""""
hero_mage = Mege("Гендальф", 100, 1000)
print(hero_mage.rest())
print(hero_mage.action())
"""""



