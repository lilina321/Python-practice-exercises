import random

class Rocket:
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed


rockets = [Rocket(random.randint(1, 5)) for _ in range(5)]
print(rockets)

for i in range(10):
    x = random.randint(0,4)
    rockets[x].moveUp()

for rocket in rockets:
    print(rocket.altitude)