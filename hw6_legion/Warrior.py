import random
from abc import ABC, abstractmethod


class Warrior(ABC):
    orcs = []
    humans = []

    def __init__(self, name="No name", max_hp=100, race="не указано",
                 gender="не указано", evasion=0.0, buff_scale=1.0):
        self.name = name
        self.max_hp = max_hp
        self.curr_hp = self.max_hp
        self.race = race
        self.gender = gender
        self.evasion = evasion
        self.buff_scale = buff_scale
        self.attack_damage = [0, 0]

    def is_evaded(self):
        return random.random() <= self.evasion

    def bio(self):
        print("Name: " + self.name)
        print("Race: " + self.race)
        print("Gender: " + self.gender)
        print("Current HP: " + str(self.curr_hp))

    def __str__(self):
        result = ""
        result += "Name: " + self.name + "\n"
        result += "Race: " + self.race + "\n"
        result += "Gender: " + self.gender + "\n"
        result += "Current HP: " + str(self.curr_hp) + "\n"
        return result

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def is_dead(self):
        pass
