class Ability:
    def __init__(self,name,style,info,myDict,cost):
        self.name = name
        self.style = style
        self.info = info
        self.dict = myDict
        self.cost = cost
        self.status = "LOCKED"

    def toString(self):
        print("Skill Name:",self.name)
        print("Style:",self.style)
        print("Info:",self.info)
        print("Furor Cost:",self.cost)
        print("Status:",self.status)

    #getters
    def getName(self):
        return self.name
    def getStyle(self):
        return self.style
    def getInfo(self):
        return self.info
    def getDict(self):
        return self.dict
    def getCost(self):
        return self.cost
    def getStatus(self):
        return se;f.status

    #setters
    def setStlye(self,value):
        self.style = value
    def setCost(self,value):
        self.cost = value
    def setDict(self,value):
        self.dict = value
    def Unlock(self,value):
        self.status = "UNLOCKED"
