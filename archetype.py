from persona import *
from helpfulFunctions import *
from skillTree import*
class Archetype(Persona):
    def __init__(self,name,StatInterface,dialouge,classType,skillTree):
        super().__init__(name,StatInterface,dialouge)
        #self.milestoneDash = milestoneInterface()
        self.classType = classType
        self.skillTree = skillTree
        self.bag = []

    def browseTree(self):
        self.skillTree.Browse()
    def unlockAbility(self):
        #set offerings value to the return value of the unlock method of skill
        #the skill tree called on the current number of offerings
        offerings = self.stats.getOfferings()
        self.stats.setOfferings(self.skillTree.Unlock(offerings))

    def getClass(self):
        return self.classType
    def getSupers(self):
        self.skillTree.getUnlockedSupers()
    def getFinishers(self):
        self.skillTree.getUnlockedFinishers()

    def Super(self):
        supers = self.getSuper()
        formatted_supers = []
        canUse = False

        for ability in supers:
            formatted_supers.append(ability.getName()+ " [%d]"%(ability.getCost()))
        print("Choose a super to use!")

        while canUse == False:
            action = Select(supers+"Quit",False)
            if self.enoughFuror(supers[action].getCost) == True:
             canUse = True

        return supers[action]

    def Finisher(self):

        finishers = self.getFinishers()
        formatted_finishers = []
        canUse = False

        for ability in finishers:
            formatted_finishers.append(ability.getName()+ " [%d]"%(ability.getCost()))
        print("Choose a finisher to use!")

        while canUse == False:
            action = Select(supers+"Quit",False)
            if self.enoughFuror(finishers[action].getCost) == True:
             canUse = True

        return finishers[action]

    #PROTOTYPE IDEA 
    #def Transform(self):
