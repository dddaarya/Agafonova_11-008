import random

from classes.Orc import Orc


class Shaman(Orc):
    def __init__(self, gender, name="No name"):
        super().__init__(max_hp=120, evasion=0.7, name=name, gender=gender, race="Shaman")

    def attack(self):
        rand = random.random()
        if rand < 0.5:
            rand = random.randint(0, len(self.humans) - 1)
            if self.humans[rand].race == "Druid":
                self.attack()
            else:
                self.humans[rand].curr_hp = 10
                print(
                    "Орки: " + self.race + " " + self.name + " заразил Человеки: " + self.humans[rand].race + " " +
                    self.humans[rand].name)
        else:
            rand = random.randint(0, len(self.orcs) - 1)
            if self.orcs[rand].race == "Shaman":
                self.attack()
            else:
                self.orcs[rand].curr_hp = self.orcs[rand].max_hp
                print(
                    "Орки: " + self.race + " " + self.name + " вылечил Орки: " + self.orcs[rand].race + " " +
                    self.orcs[rand].name)
