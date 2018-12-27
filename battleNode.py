class BattleNode:
    def __init__(self,source,target,message,value,action):
        self.source = source
        self.target = target
        self.message = message
        self.value = value
        self.action = action
    def getSource(self):
        return self.source
    def getTarget(self):
        return self.target
    def getMessage(self):
        return self.message
    def getValue(self):
        return self.value
    def getAction(self):
        return self.action
