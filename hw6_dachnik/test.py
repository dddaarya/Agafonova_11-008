from classes.Human import Human
from classes.RaspberryBush import RaspberryBush

if __name__ == '__main__':
    Human.knowledge_base()

    raspberry_bush = RaspberryBush(6)

    human = Human("Oleg", raspberry_bush)

    human.work()
    human.work()
    human.harvest()
    human.work()
    human.harvest()
    human.work()
    human.harvest()
