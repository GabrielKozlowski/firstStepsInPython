from random import randint
from math import sqrt


class Rocket:

    def __init__(self, speed=1, altitude=0, x=0):
        self.altitude = altitude

        self.speed = speed
        self.x = x

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości " + str(self.altitude)




class RocketBoard:
    def __init__(self, amoundOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amoundOfRockets)]

        for _ in range(10):
            numberOfRocket = randint(0, len(self.rockets) - 1)
            self.rockets[numberOfRocket].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1, rocket2):
        ac = (rocket1.altitude - rocket2.altitude) ** 2
        ab = (rocket1.x - rocket2.x) ** 2
        return sqrt(ac + ab)