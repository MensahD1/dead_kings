from armorInterface import *
from weaponInterface import *
from effectInterface import *
from StatInterface import *
from battleNode import *
from dialouge import *
class Persona:
    def __init__(self,StatInterface,dialouge):
        self.stats = StatInterface
        self.armorSet = ArmorInterface()
        self.weaponSet = WeaponInterface()
        self.activeEffects = EffectInterface()
        self.dialouge = dialouge
    def Reset(self):
        self.stats.resetBoosts()
        self.activeEffects.resetCondition()
    def Heal(self,heal):
        self.stats.setHealth(heal)
    def Damage(self,damage):
        self.stats.setHealth(-damage)
    def Attack(self):
        pass
    def Super(self):
        pass
    def Dodge(self):
        pass
    def Finisher(self):
        pass
    def Transform(self):
        pass
