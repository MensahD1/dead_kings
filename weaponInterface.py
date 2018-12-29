from weapon import *

class WeaponInterface:
    def __init__(self):
        self.primary = None
        self.secondary = None
        self.armory = []

    #Getters--------------
    def getPrimary(self):
        return self.primary
    def getSecondary(self):
        return self.secondary
    def getWeaponSet(self):
        return [self.primary,self.secondary]
    def getArmory(self):
        return self.armory
    def getName(self,weapon):
        return weapon.getName()
    def getGain(self,armorPiece):
        return weapon.getGain()

    #Setters-------------
    def setPrimary(self,weapon):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.primary,weapon)

        #add current armor back to armory
        storeInArmory(self.primary)

        #wear the armor
        self.primary = weapon

        return netStat
    def setSecondary(self,weapon):
        #find the difference in stat benefits to apply later
        netStat = getNetStat(self.secondary,weapon)

        #add current armor back to armory
        storeInArmory(self.secondary)

        #wear the armor
        self.secondary = weapon

        return netStat

    #Other Methods------------

    def storeInArmory(self,weapon):
        #store item in the armory array
        print(weapon.getName(),"stored in your armory.")
        self.armory.append(weapon)
    def printWeapon(self):
        print("Weapon Loadout")
        print("-------------")
        print("Primary:",self.primary)
        print("Secondary:"self.secondary)
        print("-------------")
    def getNetStat(self,oldWeapon,newWeapon):
        #returns a list of stat gain difference after armor change
        netGain = {"H":0,"F":0,"P":0,"D":0,"S":0,"X":0,"A":0,"C":0}

        for i in range(len(armorOne)):
            netGain[i] = newWeapon.getGain()[i]-oldWeapon.getGain()[i]

        return netGain
