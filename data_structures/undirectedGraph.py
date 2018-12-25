from directedGraph import*
class undirectedGraph:
    def __init__(self):
        self.directedGraph = directedGraph()
    def insertVertex(self,vertexName):
        self.directedGraph.insertVertex(vertexName)
    def removeVertex(self,vertexName):
        self.directedGraph.removeVertex(vertexName)
    def containsVertex(self,vertexName):
        return self.directedGraph.containsVertex(vertexName)
    def getVertices(self):
        return self.directedGraph.getVertices()
    def insertEdge(self,src,dest,label,weight):
        self.directedGraph.insertEdge(src,dest,label,weight)
        self.directedGraph.insertEdge(dest,src,label,weight)
    def removeEdge(self,src,dest):
        self.directedGraph.removeEdge(src,dest)
        self.directedGraph.removeEdge(dest,src)
    def containsEdge(self,src,dest):
        return self.directedGraph.containsEdge(src,dest)
    def getEdge(self,src,dest):
        return self.directedGraph.getEdge(src,dest)
    def getEdges(self):
        toReturn = []
        myEdges = self.directedGraph.getEdges()
        foundDouble = False

        for x in range(len(myEdges)):
            foundDouble = False
            for y in range(len(toReturn)):
                if (toReturn[y].getSource() == myEdges[x].getDestination()) and (toReturn[y].getDestination() == myEdges[x].getSource()):
                    foundDouble = True
                    break
            if foundDouble == False:
                toReturn.append(myEdges[x])
        return toReturn

    def getOutgoingEdges(self,vertexName):

        return self.directedGraph.getOutgoingEdges(vertexName)

    def getIncomingEdges(self,destination):
        return self.directedGraph.getIncomingEdges(destination)


def main():
    myG = undirectedGraph()
    myG.insertVertex("A")
    myG.insertVertex("B")
    myG.insertVertex("C")
    myG.insertVertex("D")
    print(myG.getVertices())
    myG.insertEdge("A","B","low",12)
    myG.insertEdge("A","C","low",12)
    myG.insertEdge("A","D","low",12)
    print(myG.getEdge("B","A"))
    print(myG.getEdges())
    print(myG.getIncomingEdges("A"))


main()
