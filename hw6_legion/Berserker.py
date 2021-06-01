from classes.Orc import Orc


class Berserker(Orc):
    def __init__(self, gender, name="No name"):
        super().__init__(max_hp=600, evasion=0.1, name=name, gender=gender, race="Berserker")
        self.attack_damage = [60, 90]
