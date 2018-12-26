from armorInterface import*
from weaponInterface import*
from effectInterface import*
class Persona:
    def __init__(self):
        self.stats = StatInterface()
        self.armorSet = ArmorInterface()
        self.weaponSet = WeaponInterface()
        self.activeEffects = EffectInterface()
