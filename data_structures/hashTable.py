import random
def Hash(key,capacity):
    if type(key) is str:
        index = 0
        for char in key:
            index+=ord(char)
        index = (index * ord(key[0])) %capacity
    else:
        index = key %capacity
        if index < 0:
            index+=capacity


    return index

class LinearDictionary:
    def __init__(self):
        self.array = []

    def get(self,key):
        for x in range(len(self.array)):
            if self.array[x][0] == key:
                return self.array[x][1]
        raise AttributeError("Key not found")

    def update(self,key,value):
        for x in range(len(self.array)):
            if self.array[x][0] == key:
                self.array[x] = (key,value)
                return 0
        raise AttributeError("Key not found")

    def contains(self,key):
        for x in range(len(self.array)):
            if self.array[x][0] == key:
                return True
        return False

    def insert(self,key,value):
        for x in range(len(self.array)):
            if self.array[x][0] == key:
                raise AttributeError("Not a unique key")
        self.array.append((key,value))
    def remove(self,key):
        for x in range(len(self.array)):
            if self.array[x][0] == key:
                self.array = self.array[0:x] + self.array[x+1:]
                return
        raise AttributeError("Key not found")

    def getSize(self):
        return len(self.array)
    def isEmpty(self):
        if len(self.array) == 0:
            return True
        return False
    def getKeys(self):
        my_keys = []
        for i in range(len(self.array)):
            my_keys.append(self.array[i][0])
        return my_keys

    def getItems(self):
        return self.array


class HashTable:
    def __init__(self):
        self.size = 0
        self.capacity = 1000
        self.table = [None] * self.capacity
    def getCapacity(self):
        return self.capacity
    def getSize(self):
        return self.size
    def insert(self,key,value):

        index = Hash(key,self.capacity)

        if self.table[index] == None:
            self.table[index] = LinearDictionary()

        self.table[index].insert(key,value)
        self.size+=1

        if self.size/self.capacity > .50:
            self.ensureCapacity()
    def remove(self,key):
        index = Hash(key,self.capacity)
        self.table[index].remove(key)

    def get(self,key):
        index = Hash(key,self.capacity)
        return self.table[index].get(key)
    def contains(self,key):
        index = Hash(key,self.capacity)
        if self.table[index] != None:
            return self.table[index].contains(key)

        return False



    def getKeys(self):
        all_keys = []
        for i in range(self.capacity):
            if self.table[i]!= None:
                all_keys+=self.table[i].getKeys()
        return all_keys

    def ensureCapacity(self):
        newCapactiy = self.capacity * 2
        newTable = [None]*newCapactiy

        #go thorugh each index of hash table, a linear dictionary

        for dictionary in self.table:
            if dictionary!=None:
                for item in dictionary.getItems():
                    index = Hash(item[0],newCapactiy)
                    if newTable[index] == None:
                        newTable[index] = LinearDictionary()
                    newTable[index].insert(item[0],item[1])


        self.table = newTable
        self.capacity = newCapactiy
