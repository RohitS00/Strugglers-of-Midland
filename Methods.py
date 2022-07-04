import random


class Attack:
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

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Sword(Attack):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2
