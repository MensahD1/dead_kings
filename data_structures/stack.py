from linked_list import *

class Stack:
    def __init__(self):
        self.stack = LinkedList()
    def push(self,value):
        self.stack.insertAtHead(value)
    def pop(self):
        return self.stack.removeHead()
    def getSize():
        return self.stack.getSize()
    def isEmpty():
        return self.stack.isEmpty()
    def peek():
        return self.stack.getHead()
