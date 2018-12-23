class PriorityNode:
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    def getValue(self):
        return self.value
    def getPriority(self):
        return self.priority
    def setValue(self,value):
        self.value = value
    def setPriority(self,priority):
        self.priority = priority

class PriorityQ:
    def __init__(self):
        self.queue = []
    def insert(self,priority,value):

        if len(self.queue) == 0:
            self.queue.append(PriorityNode(priority,value))

        else:
            if priority > self.queue[len(self.queue)-1].getPriority():
                self.queue.append(PriorityNode(priority,value))

            else:
                for i in range(len(self.queue)):
                    if self.queue[i].getPriority() > priority:
                        newNode = PriorityNode(priority,value)
                        self.queue = self.queue[:i] + [newNode] + self.queue[i:]
                        break

    def getMax(self):
        if len(self.queue) == 0 :
            raise AttributeError("The PriorityQ is empty ... terminated run")
        return self.queue[len(self.queue)-1].getValue()
    def getMaxPriority(self):
        if len(self.queue) == 0 :
            raise AttributeError("The PriorityQ is empty ... terminated run")
        return self.queue[len(self.queue)-1].getPriority()
    def removeMax(self):
        if len(self.queue) == 0 :
            raise AttributeError("The PriorityQ is empty ... terminated run")
        maxQ = self.queue.pop()
        return maxQ.getValue()
    def getSize(self):
        return len(self.queue)
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False



def main():
    

main()
