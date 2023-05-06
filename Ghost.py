import sys
sys.path.insert(1, 'C:/Users/Mitch/OneDrive/Documents/GitHub/PacMan/PacMan')
from Maze import MazeGraph
import random
class Ghost:
    def __init__(self, CurrentCoord, CurrentNode, Maze, PacManNode,RandThreshold = -1):
        self.CurrentCoord = CurrentCoord
        self.Maze = Maze
        self.PacManNode = PacManNode
        self.NextNode = CurrentNode
        self.DesiredDirection = "LEFT"
        self.RandThreshold = RandThreshold

    def ChangeDirection(self, NextNode):
        self.InDirectionOf(self.Maze.nodes[NextNode]["coord"])

    def InDirectionOf(self, NodeCoord):
        if(self.CurrentCoord[1] > NodeCoord[1]):
            self.DesiredDirection = "UP"
        elif(self.CurrentCoord[1] < NodeCoord[1]):
            self.DesiredDirection = "DOWN"
        elif(self.CurrentCoord[0] > NodeCoord[0]):
            self.DesiredDirection = "LEFT"
        elif(self.CurrentCoord[0] < NodeCoord[0]):
            self.DesiredDirection = "RIGHT"
        else:
            self.DesiredDirection = "STOP"

    def FindPacman(self):
        self.Path = self.Maze.dijkstra(self.NextNode, self.PacManNode)
        if((len(self.Path) < self.RandThreshold) and (self.RandThreshold != -1)):
            self.RandomMovement()
            return
        self.NextNode = self.Path[1] if len(self.Path) > 1 else self.Path[0]
        if(self.NextNode == None):
            self.Path = self.Maze.dijkstra(self.NextNode, self.PacManNodeNext)
            self.NextNode = self.Path[1] if len(self.Path) > 1 else self.Path[0]

        self.ChangeDirection(self.NextNode)

    def RandomMovement(self):
        NeighborNodes = self.Maze.get_neighbor_nodes(self.NextNode)
        NeighborCoords = []
        for node in NeighborNodes:
            NeighborCoords.append(self.Maze.nodes[node]["coord"])
        randNeighbor = random.randint(0, len(NeighborNodes) -1)
        self.NextNode = NeighborNodes[randNeighbor]
        self.InDirectionOf(NeighborCoords[randNeighbor])
    
    def Move(self):
        if(self.CurrentCoord == list(self.Maze.nodes[self.NextNode]["coord"])):
            self.FindPacman()

        if(self.DesiredDirection == "UP"):
            self.CurrentCoord[1] = round(self.CurrentCoord[1] - 0.01, 2)
        if(self.DesiredDirection == "DOWN"):
            self.CurrentCoord[1] = round(self.CurrentCoord[1] + 0.01, 2)
        if(self.DesiredDirection == "LEFT"):
            self.CurrentCoord[0] = round(self.CurrentCoord[0] - 0.01, 2)
        if(self.DesiredDirection == "RIGHT"):
            self.CurrentCoord[0] = round(self.CurrentCoord[0] + 0.01, 2)

        if(self.DesiredDirection == "STOP"):
            pass
        return False

# graph = MazeGraph()
# graph.add_node("A", (6, 0))
# graph.add_node("B", (0, 4))
# graph.add_node("C", (6, 4))
# graph.add_node("D", (10, 4))
# graph.add_node("E", (14, 4))
# graph.add_node("F", (6, 6))
# graph.add_node("G", (14, 8))
# graph.add_node("H", (6, 14))
# graph.add_node("I", (10, 14))



# graph.add_edge("A", "B", 10)
# graph.add_edge("A", "C", 4)
# graph.add_edge("A", "E", 12)

# graph.add_edge("B", "C", 6)
# graph.add_edge("B", "F", 8)

# graph.add_edge("C", "F", 2)
# graph.add_edge("C", "D", 4)

# graph.add_edge("D", "G", 10)
# MrPacMan = PacMan((3,4), "A", "B", "LEFT", graph)
# print(MrPacMan.NextNode)
