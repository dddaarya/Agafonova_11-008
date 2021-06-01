from classes.Human import Human


class Light(Human):
    def __init__(self, gender, name="No name"):
        super().__init__(max_hp=200, evasion=0.3, name=name, gender=gender, race="Light")
        self.attack_damage = [30, 50]
