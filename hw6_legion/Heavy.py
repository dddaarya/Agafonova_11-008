from classes.Human import Human


class Heavy(Human):
    def __init__(self, gender, name="No name"):
        super().__init__(max_hp=500, evasion=0.0, name=name, gender=gender, race="Heavy")
        self.attack_damage = [50, 70]
