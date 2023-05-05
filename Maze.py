import heapq

class MazeGraph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node, coord):
        if node not in self.nodes:
            self.nodes[node] = {"coord": coord, "edges": {}}
    
    def add_edge(self, node1, node2, weight):
        self.add_node(node1, self.nodes[node1]["coord"] if node1 in self.nodes else None)
        self.add_node(node2, self.nodes[node2]["coord"] if node2 in self.nodes else None)
        self.nodes[node1]["edges"][node2] = weight
        self.nodes[node2]["edges"][node1] = weight

    def get_neighbor_nodes(self, node):
        if node in self.nodes:
            return list(self.nodes[node]["edges"].keys())
        return None

    def get_node_coords(self):
        node_coords = {node: data["coord"] for node, data in self.nodes.items()}
        return list(node_coords.values())

    def get_edges(self):
        edge_coords = []
        added_edges = set()

        for node1, data in self.nodes.items():
            coord1 = data["coord"]

            for node2 in data["edges"]:
                if (node1, node2) not in added_edges and (node2, node1) not in added_edges:
                    added_edges.add((node1, node2))
                    coord2 = self.nodes[node2]["coord"]
                    edge_coords.append([coord1, coord2])

        return edge_coords
    
    def get_node_coord(self, node):
        if node in self.nodes:
            return self.nodes[node]["coord"]
        return None

# Example usage
# graph = MazeGraph()
# graph.add_node("A", (3, 5))
# graph.add_node("B", (2, 3))
# graph.add_node("C", (4, 5))
# graph.add_edge("A", "B", 3)
# graph.add_edge("A", "C", 1)

# print("Node Coords ", graph.get_node_coords())  # Output: {'A': (3, 5), 'B': (2, 3), 'C': (4, 5)}
# print("Edges ",graph.get_edges())
# print("Neighbors ",graph.get_neighbor_nodes("A"))        # Output: {'A': {'B': [(3, 4), (2, 4)], 'C': None}, 'B': {'A': [(3, 4), (2, 4)]}, 'C': {'A': None}}
# for edge in graph.get_edges():
#     print("edge ", edge)

# print(graph.nodes["A"])