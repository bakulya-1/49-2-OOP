#Дочерный класс Jester наследуя класс Hero
# health (hp) - здоровье
# mana (mn)- мана
# stamina (st)- выносливость
# protection - защита
# choice - выбор


from main import Hero
import main


class Jester(Hero):
    def __init__(self, name, hp, mn):
        super().__init__(name, hp)
        self.mn = mn

    def teleport(self):
        if self.mn >= 40:
            self.mn -= 40
            print(f"{self.name} телепортируется. Осталось маны: {self.mn}")

    def action(self):
        _Jester__random_action = self.__random_action
        if _Jester__random_action == 1:
            self.attack()
        elif _Jester__random_action == 2:
            self.protection()
        elif _Jester__random_action == 3:
            self.rest()

    def unique_attack(self):
        return print(f"{self.name} выполняет уникальную атаку!!")

    def unique_scream(self):
        return print(f"Xa-xa !")

Joker = Jester("Джокер", 100, 50)
Joker.action()
Joker.unique_attack()
Joker.unique_scream()
