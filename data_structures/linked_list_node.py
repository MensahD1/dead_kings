class LinkedListNode:
    def __init__(self,value):
        self.value = value
        self.after = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.after
    def setValue(self,value):
        self.value = value
    def setNext(self,after):
        self.after = after
