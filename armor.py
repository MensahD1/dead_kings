from item import*

class Armor(Item):
    def __init__(self,name,rarity,item_type,value,description,gains,armorType,upgrade_tier):
        super().__init__(name,rarity,item_type,value,description)
        self.gains = gains
        self.armorType = armorType

    def getGain(self):
        return self.gains
    def getTier(self):
        return self.upgrade_tier
    def Upgrade(self):
        self.upgrade_tier+=1
        #TODO:
        #self.setGain()
    def getArmorType(self):
        return self.armorType
    def setGain(self,gains):
        self.gain = gains


ragged_hood = Armor("Ragged Hood",1,"Armor",200,"A tatered cloth hood.",{"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0},"head",1)
ragged_cloth = Armor("Ragged Cloth",1,"Armor",200,"A tatered cloth hood.",{"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0},"chest",1)
ragged_bracer = Armor("Ragged Bracers",1,"Armor",200,"A tatered cloth hood.",{"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0},"arm",1)
ragged_leg = Armor("Ragged Leggings",1,"Armor",200,"A tatered cloth hood.",{"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0},"leg",1)
ragged_boot = Armor("Ragged Boots",1,"Armor",200,"A tatered cloth hood.",{"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0},"feet",1)
