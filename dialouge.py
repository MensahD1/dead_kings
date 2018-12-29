import random
class Dialouge:
    def __init__(self,basic,miss):
        self.basic = basic
    def getPhrase(self):
        return random.randchoice(basic)
    def getMissPhrase(self):
        return random.randchoice(basic)


test = Dialouge(["%s rushes foward and strikes the %s. Damage Done: %d"],"%s rushes forward to strike but completely misses their attack")
