import random

class Attack:
    var = 0  # attribute, for example attribute of car is model, year made, engine power, etc

    def __init__(self, name, the_level):  # method
        """

        :rtype: object
        """
        self.name = name  # name, level r attributes, init is initializing them for objects
        self.level = the_level  # assigning parameters to arguments

    # dragonslayer = Attack(dragonslayer, 100)
    # print(dragonslayer.name)
    # the object is dragonslayer & it's level is 100
    # dragonslayer.get_defensive_roll()
    # def printWeaponName(self):
    # print("this is" + self.name) #when object is made self will be replaced with it

    def __repr__(self):  # self refers to the object that is using this method, for car it is drive, stop, etc
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def power(self):
        return self.level


class Monster:

    def __init__(self, name, the_level):
        """

        :rtype: object
        """
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def health(self):
        return self.level

    def attack_power(self):
        return random.randint(0, 150)
