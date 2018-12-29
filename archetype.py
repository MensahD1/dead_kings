class Archetype:
    def __init__(self,name,StatInterface,dialouge,classType,skillTree):
        super().__init__(name,StatInterface,dialouge)
        #self.milestoneDash = milestoneInterface()
        self.classType = classType
        self.skillTree = skillTree
        self.bag = []

    def unlockAbility(self):
        #set offerings value to the return value of the unlock method of skill
        #the skill tree called on the current number of offerings
        offerings = self.stats.getOfferings()
        self.stats.setOfferings(self.skillTree.Unlock(offerings))  


    def getClass(self):
        return self.classType
    def getSupers(self):
        pass
