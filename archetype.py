class Archetype:
    def __init__(self,name,StatInterface,dialouge,classType,skillTree):
        super().__init__(name,StatInterface,dialouge)
        self.classType = classType
        self.skillTree = skillTree
        self.bag = []

    def getClass(self):
        return self.classType
    def getSupers(self):
        pass
