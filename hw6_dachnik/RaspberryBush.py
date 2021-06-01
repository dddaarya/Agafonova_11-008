from classes.Raspberry import Raspberry


class RaspberryBush(object):

    def __init__(self, num_of_raspberries):
        self.raspberries = []
        for index in range(num_of_raspberries):
            self.raspberries.append(Raspberry(index))

    def grow_all(self):
        for raspberry in self.raspberries:
            raspberry.grow()

    def all_are_ripe(self):
        result = True
        for raspberry in self.raspberries:
            result &= raspberry.is_ripe()
        return result

    def give_away_all(self):
        return self.raspberries.clear()