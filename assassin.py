class Assassin(Archetype):
    def __init__(self,name,StatInterface,dialouge,classType,skillTree):
        super().__init__(classType,skillTree)
        self.execute_limit = .20

    def Super(self):
        super().Super()
