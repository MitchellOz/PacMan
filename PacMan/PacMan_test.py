import unittest
import sys
from PacMan import PacMan
sys.path.insert(1, 'C:/Users/Mitch/OneDrive/Documents/GitHub/PacMan/PacMan')
from Maze import MazeGraph 

class PacMan_test(unittest.TestCase):

    def setUp(self):
        graph = MazeGraph()
        graph.add_node("A", (6, 0))
        graph.add_node("B", (0, 4))
        graph.add_node("C", (6, 4))
        graph.add_node("D", (10, 4))
        graph.add_node("E", (14, 4))
        graph.add_node("F", (6, 6))
        graph.add_node("G", (14, 8))
        graph.add_node("H", (6, 14))
        graph.add_node("I", (10, 14))

        graph.add_edge("A", "B", 10)
        graph.add_edge("A", "C", 4)
        graph.add_edge("A", "E", 12)

        graph.add_edge("B", "C", 6)
        graph.add_edge("B", "F", 8)

        graph.add_edge("C", "F", 2)
        graph.add_edge("C", "D", 4)

        graph.add_edge("D", "G", 10)

        self.graph = graph
        self.MrPacMan = PacMan([3,4], "C", "B", "RIGHT", graph)

    def test_GetNeighborCoords(self):
        Nodes, NodeCoords = self.MrPacMan.GetNeighborCoords("C")
        self.assertEqual(Nodes, ["A","B","F","D"])
        self.assertEqual(NodeCoords, [(6, 0),(0, 4),(6, 6),(10, 4)])
        Nodes, NodeCoords = self.MrPacMan.GetNeighborCoords("B")
        self.assertEqual(Nodes, ["A","C","F"])
        self.assertEqual(NodeCoords, [(6, 0),(6, 4),(6, 6)])

    def test_InDirectionOf(self):
        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.DesiredDirection = "LEFT"
        self.assertEqual(self.MrPacMan.InDirectionOf([[6,2],[6,6]]), False)
        
        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.DesiredDirection = "LEFT"
        WhichNode = self.MrPacMan.InDirectionOf([(6, 0),(0, 4),(6, 6),(10, 4)],["A","B","F","D"])
        self.assertEqual(WhichNode, "B")

        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.DesiredDirection = "DOWN"
        WhichNode = self.MrPacMan.InDirectionOf([(6, 0),(0, 4),(6, 6),(10, 4)],["A","B","F","D"])
        self.assertEqual(WhichNode, "F")

        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.DesiredDirection = "RIGHT"
        WhichNode = self.MrPacMan.InDirectionOf([(6, 0),(0, 4),(6, 6),(10, 4)],["A","B","F","D"])
        self.assertEqual(WhichNode, "D")

        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.DesiredDirection = "UP"
        WhichNode = self.MrPacMan.InDirectionOf([(6, 0),(0, 4),(6, 6),(10, 4)],["A","B","F","D"])
        self.assertEqual(WhichNode, "A")

    def test_DirectionPossible_inEdge(self):
        self.MrPacMan.DesiredDirection = "LEFT"
        self.assertEqual(self.MrPacMan.DirectionPossible(False), True)
        self.MrPacMan.DesiredDirection = "RIGHT"
        self.assertEqual(self.MrPacMan.DirectionPossible(False), True)
        self.MrPacMan.DesiredDirection = "UP"
        self.assertEqual(self.MrPacMan.DirectionPossible(False), False)

    def test_DirectionPossible_atNode(self):
        self.MrPacMan.NextNode = "C"
        self.MrPacMan.DesiredDirection = "UP"
        self.MrPacMan.CurrentCoord = [6,4]
        self.assertEqual(self.MrPacMan.DirectionPossible(True), True)
        
        self.MrPacMan.NextNode = "A"
        self.MrPacMan.DesiredDirection = "UP"
        self.MrPacMan.CurrentCoord = [6,0]
        self.assertEqual(self.MrPacMan.DirectionPossible(True), False)

    def test_Move(self):
        self.MrPacMan.DesiredDirection = "UP"
        self.MrPacMan.Move()
        self.assertEqual(self.MrPacMan.CurrentCoord, [3,3])
        self.MrPacMan.CurrentCoord = [3,4]
        self.MrPacMan.DesiredDirection = "DOWN"
        self.MrPacMan.Move()
        self.assertEqual(self.MrPacMan.CurrentCoord, [3,5])
        self.MrPacMan.CurrentCoord = [3,4]
        self.MrPacMan.DesiredDirection = "LEFT"
        self.MrPacMan.Move()
        self.assertEqual(self.MrPacMan.CurrentCoord, [2,4])
        self.MrPacMan.CurrentCoord = [3,4]
        self.MrPacMan.DesiredDirection = "RIGHT"
        self.MrPacMan.Move()
        self.assertEqual(self.MrPacMan.CurrentCoord, [4,4])

    def test_ChangeDirection(self):

        self.MrPacMan.CurrentCoord = [3,4]
        self.MrPacMan.ChangeDirection("LEFT")
        self.assertEqual(self.MrPacMan.CurrentCoord, [2,4])

        self.MrPacMan.CurrentCoord = [3,4]
        self.assertEqual(self.MrPacMan.ChangeDirection("RIGHT"), True)
        self.assertEqual(self.MrPacMan.CurrentCoord, [4,4])

        self.MrPacMan.CurrentCoord = [3,4]
        self.assertEqual(self.MrPacMan.ChangeDirection("UP"), False)
        self.assertEqual(self.MrPacMan.CurrentCoord, [3,4])

        self.MrPacMan.CurrentCoord = [3,4]
        self.MrPacMan.ChangeDirection("DOWN")
        self.assertEqual(self.MrPacMan.CurrentCoord, [3,4])

        self.MrPacMan.NextNode = "C"
        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.ChangeDirection("RIGHT",True)
        self.assertEqual(self.MrPacMan.CurrentCoord, [7,4])

        self.MrPacMan.NextNode = "C"
        self.MrPacMan.CurrentCoord = [6,4]
        self.assertEqual(self.MrPacMan.ChangeDirection("LEFT",True), True)
        self.assertEqual(self.MrPacMan.CurrentCoord, [5,4])

        self.MrPacMan.NextNode = "C"
        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.ChangeDirection("UP",True)
        self.assertEqual(self.MrPacMan.CurrentCoord, [6,3])
        
        self.MrPacMan.NextNode = "C"
        self.MrPacMan.CurrentCoord = [6,4]
        self.MrPacMan.ChangeDirection("DOWN",True)
        self.assertEqual(self.MrPacMan.CurrentCoord, [6,5])

if __name__ == "__main__":
    unittest.main()
