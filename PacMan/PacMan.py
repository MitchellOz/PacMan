import sys
sys.path.insert(1, 'C:/Users/Mitch/OneDrive/Documents/GitHub/PacMan/PacMan')
from Maze import MazeGraph

class PacMan:
    def __init__(self, CurrentCoord, NextNode, PrevNode, DesiredDirection, Maze):
        self.CurrentCoord = CurrentCoord
        self.NextNode = NextNode
        self.PrevNode = PrevNode
        self.DesiredDirection = DesiredDirection
        self.QueuedDirection = DesiredDirection
        self.Maze = Maze

    def ChangeDirection(self, NewDirection, atNode = False):
        temp = self.DesiredDirection
        self.QueuedDirection = NewDirection
        self.DesiredDirection = NewDirection
        if(self.DirectionPossible(atNode)):
            return True
        if(atNode):
            self.DesiredDirection = "STOP"
        else:
            self.DesiredDirection = temp
        return False

    def DirectionPossible(self, atNode):
        if(atNode):
            NeighborNodes, NeighborCoords = self.GetNeighborCoords(self.NextNode)
            WhichNode = self.InDirectionOf(NeighborCoords, NeighborNodes)
            if (WhichNode is not False):
                self.PrevNode = self.NextNode
                self.NextNode = WhichNode
                return True
        else:
            if(self.InDirectionOf([self.Maze.nodes[self.PrevNode]["coord"]])):
                temp = self.PrevNode
                self.PrevNode = self.NextNode
                self.NextNode = temp
                return True
        return False

    def GetNeighborCoords(self, Node):
        NeighborNodes = self.Maze.get_neighbor_nodes(Node)
        NeighborCoords = []
        for node in NeighborNodes:
            NeighborCoords.append(self.Maze.nodes[node]["coord"])
        return NeighborNodes, NeighborCoords
    
    def InDirectionOf(self, NodeCoords, NeighborNodes = False):
        if(not NeighborNodes):
            for NodeCoord in NodeCoords:
                if(self.DesiredDirection == "UP"):
                    if(self.CurrentCoord[1] > NodeCoord[1]):
                        return True
                if(self.DesiredDirection == "DOWN"):
                    if(self.CurrentCoord[1] < NodeCoord[1]):
                        return True
                if(self.DesiredDirection == "LEFT"):
                    if(self.CurrentCoord[0] > NodeCoord[0]):
                        return True
                if(self.DesiredDirection == "RIGHT"):
                    if(self.CurrentCoord[0] < NodeCoord[0]):
                        return True
            return False
        else:
            if(len(NodeCoords) != 0):
                for i in range(len(NodeCoords)):
                    if(self.DesiredDirection == "UP"):
                        if(self.CurrentCoord[1] > NodeCoords[i][1]):
                            return NeighborNodes[i]
                    if(self.DesiredDirection == "DOWN"):
                        if(self.CurrentCoord[1] < NodeCoords[i][1]):
                            return NeighborNodes[i]
                    if(self.DesiredDirection == "LEFT"):
                        if(self.CurrentCoord[0] > NodeCoords[i][0]):
                            return NeighborNodes[i]
                    if(self.DesiredDirection == "RIGHT"):
                        if(self.CurrentCoord[0] < NodeCoords[i][0]):
                            return NeighborNodes[i]
            return False
    
    def Move(self):
        if(self.CurrentCoord == list(self.Maze.nodes[self.NextNode]["coord"])):
            self.ChangeDirection(self.QueuedDirection, True)
            return True

        if(self.DesiredDirection == "UP"):
            self.CurrentCoord[1] = round(self.CurrentCoord[1] - 0.2, 1)
        if(self.DesiredDirection == "DOWN"):
            self.CurrentCoord[1] = round(self.CurrentCoord[1] + 0.2, 1)
        if(self.DesiredDirection == "LEFT"):
            self.CurrentCoord[0] = round(self.CurrentCoord[0] - 0.2, 1)
        if(self.DesiredDirection == "RIGHT"):
            self.CurrentCoord[0] = round(self.CurrentCoord[0] + 0.2, 1)

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
