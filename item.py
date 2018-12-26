class Item:
    def __init__(self,name,rarity,item_type,value,info):
        self.name = name
        self.rarity = rarity
        self.type = item_type
        self.value = value
        self.info = info
    def getName(self):
        return self.name
    def getRarity(self):
        return self.rarity
    def getType(self):
        return self.item_type
    def getValue(self):
        return self.value
    def getInfo(self):
        return self.info

    def setName(self,newName):
        self.name = newName
    def setRarity(self,rarity):
        self.rarity = rarity
    def setValue(self,value):
        self.value = value
