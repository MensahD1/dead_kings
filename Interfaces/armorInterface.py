from armor import *

class ArmorInterface:
    def __init__(self):
        self.head = ragged_hood
        self.chest = ragged_cloth
        self.arm = ragged_bracer
        self.leg = ragged_leg
        self.feet = ragged_boot
        self.armory = []

    #Getters--------------
    def getHead(self):
        return self.head
    def getChest(self):
        return self.chest
    def getArm(self):
        return self.arm
    def getLeg(self):
        return self.leg
    def getFeet(self):
        return self.feet
    def getArmorSet(self):
        return [self.head,self.chest,self.arm,self.leg,self.feet]
    def getArmory(self):
        return self.armory
    def getName(self,armorPiece):
        return armorPiece.getName()
    def getGain(self,armorPiece):
        retrun armorPiece.getGain()

    #Setters-------------
    def setHead(self,newArmor):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.head,newArmor)

        #add current armor back to armory
        storeInArmory(self.head)

        #wear the armor
        self.head = newArmor

        return netStat
    def setChest(self,newArmor):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.chest,newArmor)

        #add current armor back to armory
        storeInArmory(self.chest)

        #wear the armor
        self.chest = newArmor

        return netStat
    def setArm(self,newArmor):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.arm,newArmor)

        #add current armor back to armory
        storeInArmory(self.arm)

        #wear the armor
        self.arm = newArmor

        return netStat
    def setLeg(self,newArmor):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.leg,newArmor)

        #add current armor back to armory
        storeInArmory(self.leg)

        #wear the armor
        self.leg = newArmor

        return netStat
    def setFeet(self,newArmor):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.feet,newArmor)

        #add current armor back to armory
        storeInArmory(self.feet)

        #wear the armor
        self.feet = newArmor

        return netStat
    #Other Methods------------

    def storeInArmory(self,armor):
        #store item in the armory array
        print(self.armor,"stored in your armory.")
        self.armory.append(armor)
    def printArmor(self):
        print("Armor Loadout")
        print("-------------")
        print("Head:",self.head)
        print("Chest:"self.chest)
        print("Arms:",self.arm)
        print("Legs:",self.leg)
        print("Feet:",self.feet)
        print("-------------")
    def getNetStat(self,oldArmor,newArmor):
        #returns a list of stat gain difference after armor change
        netGain = {"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0}

        for i in range(len(armorOne)):
            netGain[i] = newArmor.getGain()[i]-oldArmor.getGain()[i]

        return netGain
