import pygame
import sys
from Maze import MazeGraph

def draw_circle(screen, coord, radius, color):
    pygame.draw.circle(screen, color, (coord[0], coord[1]), radius)

def draw_line(screen, coord1, coord2, color):
    pygame.draw.line(screen, color, (coord1[0], coord1[1]), (coord2[0], coord2[1]))

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



print(graph.get_node_coords())
print(graph.get_edges())        
for Edge in graph.get_edges():
    print(Edge)
# Initialize pygame
pygame.init()

# Create an 800x800 window
screen = pygame.display.set_mode((800, 800))
offset = 10
scaling = 15
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    for NodeCoord in graph.get_node_coords():
        draw_circle(screen, [NodeCoord[0]*scaling+offset, NodeCoord[1]*scaling+offset], 10, (0, 255, 0))

    for Edge in graph.get_edges():
        draw_line(screen, [Edge[0][0]*scaling+offset, Edge[0][1]*scaling+offset], [Edge[1][0]*scaling+offset, Edge[1][1]*scaling+offset], (255, 0, 0))

    draw_circle(screen, [3*scaling+offset, 4*scaling+offset], 10, (255, 255, 0))
    graph.get_neighbor_nodes("A")
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()