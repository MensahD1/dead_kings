from armorInterface import *
from weaponInterface import *
from effectInterface import *
from StatInterface import *
from battleNode import *
from dialouge import *

class Persona:
    def __init__(self,name,StatInterface,dialouge):
        self.name = name
        self.stats = StatInterface
        self.armorSet = ArmorInterface()
        self.weaponSet = WeaponInterface()
        self.activeEffects = EffectInterface()
        self.dialouge = dialouge

    def getName(self):
        return self.name
    def printDetails(self):
        self.stats.printDetailed()

    def isDead(self):
        if self.stats.getHealth() <= 0:
            return True
        return False
        
    def Reset(self):
        self.stats.resetBoosts()
        self.activeEffects.resetCondition()

    def Heal(self,heal):
        self.stats.setHealth(heal)

    def Damage(self,damage):
        mitigatedDamage = self.applyMitigations(damage)
        self.stats.setHealth(-mitigatedDamage)

    def willMiss(self):
        if random.randrange(100) < self.stats.getAccuracy():
            return True
        return False

    def Attack(self,source,target):
        #assign values to variables
        message = self.dialouge.getPhrase()
        power = self.stats.getPower()
        boost = self.stats.getPowerBoost()
        #check to see if attack will miss
        if self.willMiss() == True:
            message = self.dialouge.getMissPhrase()
            power = 0
            boost = 0
        #return node instance
        return BattleNode(source,target,message,power + boost,"Attack")


    def Dodge(self):
        pass
    def Finisher(self):
        pass
    def Super(self):
        pass
    def Transform(self):
        pass
