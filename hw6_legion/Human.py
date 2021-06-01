from classes.Warrior import Warrior
import random


class Human(Warrior):
    def __init__(self, name="No name", max_hp=100,
                 gender="не указано", evasion=0.0, race="Человек"):
        super().__init__(race=race, buff_scale=1.1, name=name, max_hp=max_hp, evasion=evasion,
                         gender=gender)
        self.humans.append(self)

    def is_evaded(self):
        return random.random() <= self.evasion * self.buff_scale

    def attack(self):
        rand = random.randint(0, len(self.orcs) - 1)
        damage = random.randint(self.attack_damage[0], self.attack_damage[1])
        if not self.orcs[rand].is_evaded():
            self.orcs[rand].curr_hp -= damage
            print("Человеки: " + self.race + " " + self.name + "  ударил Орки: " + self.orcs[rand].race + " " +
                  self.orcs[rand].name + " с силой " + str(damage))
            if self.orcs[rand].is_dead:

                self.orcs.remove(self.orcs[rand])

        else:
            print("Человеки: " + self.race + " " + self.name + "  промахнулся по  Орки: " + self.orcs[rand].race + " " +
                  self.orcs[rand].name)

    def is_dead(self):
        print("Человеки: " + self.race + " " + self.name + "  умер")
        return self.curr_hp <= 0
