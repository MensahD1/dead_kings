from linked_list import *

class Queue:
    def __init__(self):
        self.queue = LinkedList()
    def enqueue(self,value):
        self.queue.insertAtTail(value)
    def dequeue(self):
        return self.queue.removeHead()
    def getSize():
        return self.queue.getSize()
    def isEmpty():
        return self.queue.isEmpty()
    def peek():
        return self.queue.getHead()
