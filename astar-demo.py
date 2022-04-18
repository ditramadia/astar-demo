class Graph:
    def __init__(self, neighbourList):
        self.neighbourList = neighbourList

    def getNeighbours(self, node):
        return self.neighbourList[node]

    def gScore(self, node):
        gScore = {
            "A": 999,
            "B": 999,
            "C": 999,
            "D": 999,
            "E": 999,
            "F": 999,
            "G": 999,
            "H": 999,
            "I": 999,
            "J": 999,
            "K": 999,
            "L": 999,
        }

        return gScore[node]

    def aStarAlgorithm(self, startingNode, stoppingNode):
        openList = set([startingNode])
        closedList = set([])

        fScore = {}
        fScore[startingNode] = 0

        nodeList = {}
        nodeList[startingNode] = startingNode

        while len(openList) > 0:
            node = None

            for comparingNode in openList:
                if node == None or fScore[comparingNode] + self.gScore(comparingNode) < fScore[node] + self.gScore(node):
                    node = comparingNode

            if node == None:
                print("Path does not exist!")
                return None

            if node == stoppingNode:
                reconstructPath = []

                while nodeList[node] != node:
                    reconstructPath.append(node)
                    node = nodeList[node]

                reconstructPath.append(startingNode)

                reconstructPath.reverse()

                print("Path found: {}".format(reconstructPath))
                return reconstructPath

            for (comparingNode2, weight) in self.getNeighbours(node):
                if comparingNode2 not in openList and comparingNode2 not in closedList:
                    openList.add(comparingNode2)
                    nodeList[comparingNode2] = node
                    fScore[comparingNode2] = fScore[node] + weight
                else:
                    if fScore[comparingNode2] > fScore[node] + weight:
                        fScore[comparingNode2] = fScore[node] + weight
                        nodeList[comparingNode2] = node

                        if comparingNode2 in closedList:
                            closedList.remove(comparingNode2)
                            openList.add(comparingNode2)

            openList.remove(node)
            closedList.add(node)

        print("Path does not exist!")
        return None


neighbourList = {
    "A": [("C", 2000)],
    "B": [("D", 2500)],
    "C": [("A", 2000), ("D", 1500), ("E", 800)],
    "D": [("B", 2500), ("E", 1200), ("F", 1000)],
    "E": [("C", 800), ("D", 1200), ("F", 900), ("G", 700), ("J", 2000)],
    "F": [("D", 1000), ("E", 900), ("G", 500)],
    "G": [("E", 700), ("F", 500), ("H", 600)],
    "H": [("G", 600), ("I", 500), ("L", 1500)],
    "I": [("H", 500), ("J", 300)],
    "J": [("E", 2000), ("I", 300), ("K", 1000)],
    "K": [("J", 1000)],
    "L": [("H", 1500)]
}

startingNode = str(input("Starting Node: "))
stoppingNode = str(input("Stopping Node: "))
graph1 = Graph(neighbourList)
graph1.aStarAlgorithm(startingNode, stoppingNode)
