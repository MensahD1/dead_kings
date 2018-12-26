class StatInterface:
    def __init__(self,health,furor,defense,shred,speed,accuracy):
        self.health = health
        self.furor = furor
        self.defense = defense
        self.shred = shred
        self.speed = speed
        self.accuracy = accuracy
        self.crit = 0
        self.shredBoost = 0
        self.defenseBoost = 0
        self.powerBoost = 0
        self.critBoost = 0
        self.level = 1
        self.experience = 0
        self.offerings = 0
        self.gold = 0
        self.maxHealth = self.health
        self.maxFuror = self.furor

    def resetBoosts():
        self.shredBoost = 0
        self.critBoost = 0
        self.powerBoost = 0
        self.defenseBoost = 0
    def printGeneral(self,name):
        print(name,"Stats Overview-------")
        print("Level:",self.level)
        print("Gold:",self.gold)
        print("Health:",self.health)
        print("---------------")
    def printDetailed(self,name):
        print(name,"Stats Detailed--------")
        print("Level:",self.level)
        print("EXP:",self.experience)
        print("Gold:",self.gold)
        print("Offerings:",self.offerings)
        print("Health:",self.health)
        print("Furor:",self.furor)
        print("Defense:",self.defense)
        print("Shred:",self.shred)
        print("Speed:",self.speed)
        print("Accuracy:",self.accuracy)
        print("---------------")

    #Getters------------------------
    def getHealth(self):
        return self.health
    def getFuror(self):
        return self.furor
    def getDefense(self):
        return self.defense
    def getShred(self):
        return self.shred
    def getSpeed(self):
        return self.speed
    def getAccuracy(self):
        return self.accuracy
    def getCrit(self):
        return self.crit
    def getShredBoost(self):
        return self.shredBoost
    def getDefenseBoost(self):
        return self.defenseBoost
    def getPowerBoost(self):
        return self.powerBoost
    def getCritBoost(self):
        return self.critBoost
    def getLevel(self):
        return self.level
    def getExp(self):
        return self.experience
    def getOfferings(self):
        return self.offerings
    def getGold(self):
        return self.gold
    def getMaxHealth(self):
        return self.maxHealth
    def getMaxFuror(self):
        return self.maxFuror

    def setHealth(self,value):
         self.health += value
    def setFuror(self,value):
         self.furor += value
    def setDefense(self,value):
         self.defense += value
    def setShred(self,value):
         self.shred += value
    def setSpeed(self,value):
         self.speed += value
    def setAccuracy(self,value):
         self.accuracy += value
    def setCrit(self,value):
         self.crit += value
    def setShredBoost(self,value):
         self.shredBoost += value
    def setDefenseBoost(self,value):
         self.defenseBoost += value
    def setPowerBoost(self,value):
         self.powerBoost += value
    def setCritBoost(self,value):
         self.critBoost += value
    def setLevel(self,value):
         self.level += value
    def setExp(self,value):
         self.experience += value
    def setOfferings(self,value):
         self.offerings += value
    def setGold(self,value):
         self.gold += value
    def setMaxHealth(self,value):
         self.maxHealth +=value
    def setMaxFuror(self,value):
         self.maxFuror+=value
