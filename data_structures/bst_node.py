def insertInSubtree(origin,key,value):
    if origin == None:
        return BSTNode(key,value)
    elif key > origin.getKey():
        origin.setRight(insertInSubtree(origin.getRight(),key,value))
        return origin
    elif key < origin.getKey():
        origin.setLeft(insertInSubtree(origin.getLeft(),key,value))
        return origin
    else:
        raise AttributeError("Repeated Key In Tree... run terminated")
def removeInSubtree(origin,key):
    if origin == None:
        raise AttributeError("Key not found")
    elif key > origin.getKey():
        origin.setRight(removeInSubtree(origin.getRight(),key))
        return origin
    elif key <origin.getKey():
        origin.setLeft(removeInSubtree(origin.getLeft(),key))
        return origin
    else:
        if origin.getRight() == None and origin.getLeft() == None:
            del origin
            return None
        elif origin.getRight() == None:
            temp = origin.getLeft()
            del origin
            return temp
        elif origin.getLeft() == None:
            temp = origin.getRight()
            del origin
            return temp
        else:
            ancestor = getMaxInTree(origin.getLeft())
            origin.setKey(ancestor.getKey())
            origin.setValue(ancestor.getValue())
            origin.setLeft(removeInSubtree(origin.getLeft(),origin.getKey()))
            return origin
def findInSubtree(origin,key):
    if origin == None:
        raise AttributeError("Key Not Found")
    elif key > origin.getKey():
        return findInSubtree(origin.getRight(),key)
    elif key <origin.getKey():
        return findInSubtree(origin.getLeft(),key)
    else:
        return orgin.getValue();
def updateInSubtree(origin,key,value):
    if origin == None:
        raise AttributeError("Key Not Found")
    elif key > origin.getKey():
        updateInSubtree(origin.getRight(),key,value)
    elif key < origin.getKey():
        updateInSubtree(origin.getLeft(),key,value)
    else:
        orgin.setValue(value)
def inSubtree(origin,key):
    if origin == None:
        return False
    elif key > origin.getKey():
        return inSubtree(origin.getRight(),key)
    elif key <origin.getKey():
        return inSubtree(origin.getLeft(),key)
    else:
        return True
def getMinInTree(origin):
    if origin.getLeft() == None:
        return origin
    else:
        return getMinInTree(origin.getLeft())
def getMaxInTree(origin):
    if origin.getRight() == None:
        return origin
    else:
        return getMaxInTree(origin.getRight())


class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setLeft(self,node):
        self.left = node
    def setRight(self,node):
        self.right = node
    def setValue(self,value):
        self.value = value
    def setKey(self,key):
        self.key = key

class BSTTree:
    def __init__(self):
        self.size = 0
        self.root = None

    def getSize(self):
        return self.size
    def get(self,key):
        if self.size == 0:
            raise AttributeError("Tree Empty")
        else:
            return findInSubtree(self.root,key)
    def insert(self,key,value):
        if self.size == 0:
            self.root = BSTNode(key,value)
        else:
            insertInSubtree(self.root,key,value)
        self.size+=1

    def remove(self,key):
        if self.size == 0:
            raise AttributeError("Tree is empty can not prefrom remove operation")
        else:
            removeInSubtree(self.root,key)
        self.size-=1

    def update(self,key,value):
        if self.size == 0:
            self.root = BSTNode(key,value)
        else:
             updateInSubtree(self.root,key,value)

    def contains(self,key):
        if self.size==0:
            raise AttributeError("Tree is empty")
        else:
            return inSubtree(self.root,key)
    def getMinKey(self):
        if self.size == 0 :
            raise AttributeError("The tree is empty ")
        return getMinInTree(self.root).getKey()
    def getMaxKey(self):
        if self.size == 0 :
            raise AttributeError("The tree is empty ")
        return getMaxInTree(self.root).getKey()





def main():
    myTree = BSTTree();
    myTree.insert("Richmond",1)
    myTree.insert("Kobina",2)
    myTree.insert("Mensah",3)
    myTree.insert("Bensah",3)
    myTree.insert("Censah",3)

    myTree.remove("Richmond")
    myTree.remove("Kobina")
    myTree.remove("Mensah")
    myTree.remove("Bensah")
    myTree.remove("Censah")
    #myTree.remove("Censah")


    print(myTree.getSize())
    print(myTree.getMinKey())

main()
