class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.predecessor = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.distance = d

    def setPredecessor(self, pred):
        self.predecessor = pred

    def getPredecessor(self):
        return self.predecessor

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDiscovery(self, time):
        self.disc = time

    def setFinish(self, time):
        self.fin = time
            
    