import random

from classes.Berserker import Berserker
from classes.Druid import Druid
from classes.Heavy import Heavy
from classes.Human import Human
from classes.Light import Light
from classes.Shaman import Shaman
from classes.Warrior import Warrior

if __name__ == '__main__':
    Light(name="Light1", gender="Ж")
    Light(name="Light2", gender="М")
    Light(name="Light3", gender="Ж")
    Light(name="Light4", gender="М")
    Light(name="Light5", gender="М")
    Light(name="Light6", gender="М")
    Light(name="Light7", gender="М")
    Light(name="Light8", gender="М")

    Heavy(name="Heavy1", gender="М")
    Heavy(name="Heavy2", gender="М")
    Heavy(name="Heavy3", gender="Ж")
    Heavy(name="Heavy4", gender="М")
    Heavy(name="Heavy5", gender="Ж")
    Heavy(name="Heavy6", gender="М")
    Heavy(name="Heavy7", gender="Ж")
    Heavy(name="Heavy8", gender="М")
    Heavy(name="Heavy9", gender="Ж")
    Heavy(name="Heavy10", gender="М")
    Heavy(name="Heavy11", gender="Ж")
    Heavy(name="Heavy12", gender="М")
    Heavy(name="Heavy13", gender="Ж")
    Heavy(name="Heavy14", gender="М")
    Heavy(name="Heavy15", gender="М")
    Heavy(name="Heavy16", gender="Ж")
    Heavy(name="Heavy17", gender="М")
    Heavy(name="Heavy18", gender="Ж")
    Heavy(name="Heavy19", gender="М")
    Heavy(name="Heavy20", gender="Ж")
    Heavy(name="Heavy21", gender="М")

    Druid(name="Druid1", gender="М")
    Druid(name="Druid2", gender="Ж")
    Druid(name="Druid3", gender="М")
    Druid(name="Druid4", gender="Ж")
    Druid(name="Druid5", gender="М")
    Druid(name="Druid6", gender="Ж")
    Druid(name="Druid7", gender="М")
    Druid(name="Druid8", gender="Ж")

    Berserker(name="Berserker1", gender="М")
    Berserker(name="Berserker2", gender="Ж")
    Berserker(name="Berserker3", gender="М")
    Berserker(name="Berserker4", gender="М")
    Berserker(name="Berserker5", gender="Ж")
    Berserker(name="Berserker6", gender="М")
    Berserker(name="Berserker7", gender="Ж")
    Berserker(name="Berserker8", gender="М")
    Berserker(name="Berserker9", gender="Ж")
    Berserker(name="Berserker10", gender="М")
    Berserker(name="Berserker11", gender="Ж")
    Berserker(name="Berserker12", gender="М")
    Berserker(name="Berserker13", gender="Ж")
    Berserker(name="Berserker14", gender="Ж")
    Berserker(name="Berserker15", gender="М")
    Berserker(name="Berserker16", gender="М")
    Berserker(name="Berserker17", gender="Ж")
    Berserker(name="Berserker18", gender="Ж")
    Berserker(name="Berserker19", gender="М")
    Berserker(name="Berserker20", gender="М")
    Berserker(name="Berserker21", gender="Ж")
    Berserker(name="Berserker22", gender="М")
    Berserker(name="Berserker23", gender="Ж")
    Berserker(name="Berserker25", gender="М")
    Berserker(name="Berserker26", gender="Ж")
    Berserker(name="Berserker27", gender="Ж")
    Berserker(name="Berserker28", gender="М")
    Berserker(name="Berserker29", gender="М")
    Berserker(name="Berserker30", gender="Ж")

    Shaman(name="Shaman1", gender="М")
    Shaman(name="Shaman2", gender="М")
    Shaman(name="Shaman3", gender="М")
    Shaman(name="Shaman4", gender="М")
    Shaman(name="Shaman5", gender="М")
    Shaman(name="Shaman6", gender="М")
    Shaman(name="Shaman7", gender="М")
    Shaman(name="Shaman8", gender="М")
    Shaman(name="Shaman9", gender="М")
    Shaman(name="Shaman10", gender="М")
    Shaman(name="Shaman11", gender="М")
    Shaman(name="Shaman12", gender="М")
    Shaman(name="Shaman13", gender="М")
    Shaman(name="Shaman14", gender="М")
    Shaman(name="Shaman15", gender="М")
    Shaman(name="Shaman16", gender="М")
    Shaman(name="Shaman17", gender="М")
    Shaman(name="Shaman18", gender="М")
    Shaman(name="Shaman19", gender="М")
    Shaman(name="Shaman20", gender="М")
    Shaman(name="Shaman21", gender="М")
    Shaman(name="Shaman22", gender="М")

    while True:
        print("Новый круг")

        rand = random.randint(0, len(Warrior.orcs) - 1)
        Warrior.orcs[rand].attack()
        if len(Warrior.humans) <= 0:
            print("Победили орки")
            for orc in Warrior.orcs:
                orc.bio()
                print("")
            break

        rand = random.randint(0, len(Warrior.humans) - 1)
        Warrior.humans[rand].attack()
        if len(Warrior.orcs) <= 0:
            print("Победили люди")
            for human in Warrior.humans:
                human.bio()
                print("")
            break
