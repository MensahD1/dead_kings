from linked_list_node import *

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def getSize(self):
        return self.size
    def getHead(self):
        if self.size==0:
            raise AttributeError("Error: There is nothing in the Linked List")
        return self.head.getValue()
    def getTail(self):
        if self.size==0:
            raise AttributeError("Error: There is nothing in the Linked List")
        return self.tail.getValue()
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    def getNode(self,index):
        if self.size==0:
            raise AttributeError("Error: There is nothing in the Linked List")
        finder = self.head

        for x in range(index):
            finder.getNext()

        return finder.getValue()

    def insertAtHead(self,value):
        holder = self.head
        self.head = LinkedListNode(value)
        if self.size == 0:
            self.tail = self.head
        self.head.setNext(holder)
        self.size+=1
    def insertAtTail(self,value):
        newTail = LinkedListNode(value)
        if self.size!=0:
            self.tail.setNext(newTail)
        self.tail = newTail
        if self.size == 0:
            self.head = self.tail
        self.size+=1
    def removeHead(self):
        if self.size==0:
            raise AttributeError("Error: There is nothing in the Linked List")
        if self.size==1:
            del self.head
            self.head = None
            self.tail = None
        else:
            newHead = self.head.getNext()
            del self.head
            self.head = newHead
        self.size-=1
    def removeTail(self):
        if self.size==0:
            raise AttributeError("Error: There is nothing in the Linked List")
        if self.size==1:
            del self.tail
            self.head = None
            self.tail = None
        else:
            finder = self.head
            for node in range(self.size-2):
                finder.getNext()
            finder.setNext(None)
            del self.tail
            self.tail = finder
        self.size-=1
