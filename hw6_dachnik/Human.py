from classes.RaspberryBush import RaspberryBush


class Human(object):

    @staticmethod
    def knowledge_base():
        print("В средней полосе России малину сажают с начала сентября до 20 октября\n"
              "В южных регионах посадку осуществляют с середины сентября до последних чисел октября\n"
              "В северных регионах нужно успеть высадить малину в первых числах сентября или перенести посадку "
              "на весеннее время.")

    def __init__(self, name: str, raspberry_bush: RaspberryBush):
        self.name = name
        self._plant = raspberry_bush

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print("Too early")
