from item import*

class Weapon(Item):
    def __init__(self,name,rarity,item_type,value,description,gains,weaponType,upgrade_tier,enchantment):
        super().__init__(name,rarity,item_type,value,description)
        self.gains = gains
        self.armorType = armorType

    def getGain(self):
        return self.gains
    def getTier(self):
        return self.upgrade_tier
    def Upgrade(self):
        pass
    def getEnchantment(self):
        return self.enchantment
    def setEnchantment(self,element):
        self.enchantment = element
    def getArmorType(self):
        return self.armorType
    def setGain(self,gains):
        self.gain = gains
    def setTier(self)


fist = Weapon("Fists",1,"Weapon",0,"Steel knucks for melee fighting.",{"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0},"melee",1,None)
