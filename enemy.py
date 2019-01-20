from persona import *
class Enemy(Persona):
    def __init__(self,name,StatInterface,dialouge,goldReward,expReward,itemDrops):
        super().__init__(name,StatInterface,dialouge)
        self.goldReward = goldReward
        self.expReward = expReward
        self.itemDrops = itemDrops

    def getRewards(self):
        return [self.goldReward,self.expReward,self.itemDrops]

    def printProfile(self):
        print("Enemy Profile")
        print("Name:",self.name)
        print("Health:",self.stats.getHealth())
        print("Gold Reward:",self.goldReward)
        print("EXP Reward:",self.expReward)
        print("------------------")
