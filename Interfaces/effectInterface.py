import random
class EffectInterface():
    def __init__(self):
           self.poisoned = False
           self.burned = False
           self.invincible = False
           self.bleeding = False
           self.frozen = False
    def isBurned(self):
        if self.resolveEffect() == False and self.burned == True:
            self.burned = False
        return self.burned
    def isPoisoned(self):
        if self.resolveEffect() == False and self.poisoned == True:
            self.poisoned = False
        return self.poisoned
    def isInvincible(self):
        if self.resolveEffect() == False and self.invincible == True:
            self.invincible = False
        return self.invincible
    def isBleeding(self):
        if self.resolveEffect() == False and self.bleeding == True:
            self.bleeding = False
        return self.bleeding
    def isFrozen(self):
        if self.resolveEffect() == False and self.frozen == True:
            self.frozen = False
        return self.frozen

    def resolveEffect(self):
        #randomly decicdes is persona is still afflicted by status effect
        if random.randchoice([1,0,0,0,0,0,0,0,0,0]) == 1:
            return False
        return True

    def resetCondition(self):
        self.poisoned = False
        self.burned = False
        self.invincible = False
        self.bleeding = False
        self.frozen = False
