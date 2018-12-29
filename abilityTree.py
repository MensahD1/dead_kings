from directedGraph import *
from ability import *
from helpfulFunctions imprt *

class AbilityTree:
    def __init__(self):
        self.tree = directedGraph()
        self.unlocked = []

    #initializing methods for tree, add ability objects as vertexes
    def insertAbility(self,ability):
        self.tree.insertVertex(value)
    def insertPath(self,abilityOne,abilityTwo):
        self.tree.insertEdge(abilityOne,abilityTwo,0,0)

    #getters
    def getAbilities(self):
        return self.tree.getVertices()
    def getPaths(self):
        return self.tree.getEdges()
    def getRequiredPaths(self,ability):
        return self.tree.getIncomingEdges()
    def getAvailablePaths(self,ability):
        return self.tree.getOutgoingEdges()

    #Naviagational Methods
    def getUnlocked(self):
        return self.unlocked
    def getLocked(self):
        #get all abilites and all unlocked abilities
        myUnlocks = self.unlocked
        myAbilities = self.getAbilities()

        #remove all unlock abilities from the list of all abilities
        for ability in myUnlocks:
            myAbilities.remove(ability)

        #return the list, which are all the locked abilities
        return myAbilities
    def getUnlockables(self):

        #define variables
        unlockables = []
        requiredPaths = []
        myUnlocks = self.unlocked
        lockedAbilities = self.getLocked()

        #for each locked ability get its incoming paths
        for ability in lockedAbilities:
            #get the incoming edges to the ability
            requiredPaths = self.getRequiredPaths(ability)

            #mark the number of paths representing how many abilities
            #are needed to unlock the ability
            requiredCount = len(requiredPaths)

            # for each incoming path get the source ability
            for path in requiredPaths:
                requiredAbility = path.getSource()

                #check if the source ability is in the unlocks, if so lower count
                if requiredAbility in myUnlocks:
                    requiredCount-=1

            if requiredCount == 0:
                unlockables.append(ability)

    def Unlock(self,offerings):

        selection = ""
        #continue to allow unlocks until user is out of offerings or quits
        while offerings > 0 and selection != "Quit":

            #define unlockable abilities and make a lst of the names for the user
            unlockables = self.getUnlockables()
            unlockables_str = []
            for ability in unlockables:
                unlockables_str.append(ability.getName())

            #Open up selection for the user
            print("Give up an offering to unlock a blessing!")
            print("What blessing do you desire? (Select a blessing to learn more.)")
            selection = Select(unlockables_str + "Quit",False)

            #make sure selection
            if selection < len(unlockables):
                unlockables[selection].toString()
                print("Give an offering for this blessing?")
                response = Select(["Yes","No"],True)

                if response == "Yes":
                    offerings-=1
                    unlockables[selection].Unlock()
                    self.unlocked.append(unlockables[selection])
            else:
                selection = "Quit"

        return offerings
