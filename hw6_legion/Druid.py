from classes.Human import Human

import random


class Druid(Human):
    def __init__(self, gender, name="No name"):
        super().__init__(max_hp=100, evasion=0.7, name=name, gender=gender, race="Druid")

    def attack(self):
        rand = random.random()
        if rand <= 0.3:
            rand = random.randint(0, len(self.orcs) - 1)
            if self.orcs[rand].race == "Shaman":
                self.attack()
            else:
                self.orcs[rand].curr_hp = 10
                print("Человеки: " + self.race + " " + self.name + " заразил Орки: " + self.orcs[rand].race + " " +
                      self.orcs[rand].name)
        else:
            rand = random.randint(0, len(self.humans) - 1)
            if self.humans[rand].race == "Druid":
                self.attack()
            else:
                self.humans[rand].curr_hp = self.humans[rand].max_hp
                print(
                    "Человеки: " + self.race + " " + self.name + " вылечил Человеки: " + self.humans[rand].race + " " +
                    self.humans[rand].name)
