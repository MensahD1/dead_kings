import directedGraph.py
class undirectedGraph:
    def __init__(self):
        self.directedGraph = directedGraph()
    def insertVertex(self,vertexName):
        if self.vertices.contains(vertexName) == False:
            self.vertices.insert(vertexName,True)
            self.edges.insert(vertexName,HashTable())
    def removeVertex(self,vertexName):
        if self.vertices.contains(vertexName) == True:
            self.vertices.remove(vertexName)
    def containsVertex(self,vertexName):
        return self.vertices.contains(vertexName)
    def getVertices(self):
        return self.vertices.getKeys()
    def insertEdge(self,src,dest,label,weight):
        if self.vertices.contains(src) == False:
            raise ValueError("SRC key not found")
        if self.vertices.contains(dest) == False:
            raise ValueError("DEST key not found")
        if self.edges.get(src).contains(dest) == True:
            raise ValueError("Edge already exits from",src,"to",dest)
        else:
            self.edges.get(src).insert(Edge(src,dest,label,weight))
    def removeEdge(self,src,dest):
        if self.edges.contains(src) and self.edges.get(src).contains(dest):
            self.edges.get(src).remove(dest)
        else:
            raise ValueError("Edge does not exit from",src,"to",dest)
    def containsEdge(self,src,dest):
        return self.edges.contains(src) and self.edges.get(src).contains(dest):
    def getEdge(self,src,dest):
        if self.edges.contains(src) and self.edges.get(src).contains(dest):
            return self.edges.get(src).get(dest)
        else:
            raise ValueError("Edge does not exit from",src,"to",dest)
    def getEdges(self):
        myEdges =[]
        sources = self.edges.getKeys()
        for x in range(len(sources)):
            destinations = self.edges.get(sources[x]).getKeys()
            for y in range(len(destinations)):
                myEdges.append(self.edges.get(sources[x]).get(destinations[y]))
