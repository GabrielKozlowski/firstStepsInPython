from random import randint

class Rocket:

    def __init__(self, speed):
        self.altitude = 0

        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości " + str(self.altitude)

class RocketBoard:
    def __init__(self, amoundOfRockets=5):
        rockets = [Rocket(randint(1, 6)) for _ in range(amoundOfRockets)]

        for _ in range(10):
            numberOfRocket = randint(0, len(rockets) - 1)
            rockets[numberOfRocket].moveUp()

        for rocket in rockets:
            print(rocket)
