
class Fighter:
    def __str__(self):
        return 'Unit: ' + '{:9}'.format(self.__class__.__name__) + ' > life: ' \
               + str(self.life) + '   > exp: ' + str(self.experience)

    def isAlive(self):
        return self.life > 0

    def loseLife(self, lostLife):
        self.life -= lostLife
        if self.life < 0:
            self.life = 0

    def gainExperience(self, gainedExperience):
        self.experience += gainedExperience

class Soldier(Fighter):
    cost = 1

    def __init__(self):
        self.life = 3
        self.experience = 0
        self.speed = 1 + self.experience
        self.damage = 1 + self.experience



    def getSpeed(self):
        return 1 + self.experience

    def attack(self):
        return 1 + self.experience

    def defend(self, damage):
        if damage > self.experience:
            self.life -= 1

class Archer(Fighter):
    cost = 2

    def __init__(self):
        self.life = 3
        self.experience = 0

    def getSpeed(self):
        return 3

    def attack(self):
        return 1 + self.experience

    def defend(self, damage):
        self.life -= 1

class Cavalry(Fighter):
    cost = 3

    def __init__(self):
        self.life = 4
        self.experience = 0

    def getSpeed(self):
        return 3

    def attack(self):
        return 2*self.experience + 1

    def defend(self, damage):
        if damage > (self.experience / 2):
            self.life -= 1




