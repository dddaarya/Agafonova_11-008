import random

from classes.Warrior import Warrior


class Orc(Warrior):
    def __init__(self, name="No name", max_hp=100,
                 gender="не указано", evasion=0.0, race="Орк"):
        super().__init__(race=race, buff_scale=1.1, name=name, max_hp=max_hp, evasion=evasion,
                         gender=gender)
        self.orcs.append(self)

    def attack(self):
        rand = random.randint(0, len(self.humans) - 1)
        damage = random.randint(self.attack_damage[0], self.attack_damage[1])
        if not self.humans[rand].is_evaded():
            self.humans[rand].curr_hp -= damage * self.buff_scale
            print("Орки : " + self.race + " " + self.name + "  ударил Человеки: " + self.humans[rand].race + " " +
                  self.humans[rand].name + " с силой " + str(damage * self.buff_scale))
            if self.humans[rand].is_dead:

                self.humans.remove(self.humans[rand])

        else:
            print(
                "Орки: " + self.race + " " + self.name + "  промахнулся по Человеки: " + self.humans[
                    rand].race + " " +
                self.humans[rand].name)

    def is_dead(self):
        print("Орки: " + self.race + " " + self.name + "  умер")
        return self.curr_hp <= 0
