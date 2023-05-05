import pygame
import sys
from Maze import MazeGraph
sys.path.insert(1, 'C:/Users/Mitch/OneDrive/Documents/GitHub/PacMan/PacMan/PacMan')
from PacMan import PacMan
from Ghost import Ghost
def draw_circle(screen, coord, radius, color):
    pygame.draw.circle(screen, color, (coord[0], coord[1]), radius)

def draw_line(screen, coord1, coord2, color):
    pygame.draw.line(screen, color, (coord1[0], coord1[1]), (coord2[0], coord2[1]))

graph = MazeGraph()
graph.add_node("A", (0, 0))
graph.add_node("B", (3, 0))
graph.add_node("C", (5, 0))
graph.add_node("D", (0, 2))
graph.add_node("E", (3, 2))
graph.add_node("F", (4, 2))
graph.add_node("G", (5, 2))
graph.add_node("H", (0, 3))
graph.add_node("I", (3, 3))
graph.add_node("J", (4, 3))
graph.add_node("K", (5, 3))
graph.add_node("L", (4, 4))
graph.add_node("M", (5, 4))
graph.add_node("N", (3, 5))
graph.add_node("O", (4, 5))

graph.add_edge("A", "B")
graph.add_edge("A", "D")

graph.add_edge("B", "C")
graph.add_edge("B", "E")

graph.add_edge("C", "G")

graph.add_edge("D", "E")
graph.add_edge("D", "H")

graph.add_edge("E", "F")
graph.add_edge("E", "I")

graph.add_edge("F", "G")
graph.add_edge("F", "J")

graph.add_edge("H", "I")

graph.add_edge("I", "N")

graph.add_edge("J", "K")

graph.add_edge("K", "M")

graph.add_edge("L", "M")

graph.add_edge("O", "L")

graph.add_edge("N", "O")
# graph.add_edge("A", "AB", 5)
# graph.add_edge("A", "C", 4)
# graph.add_edge("A", "AE", 8)
# graph.add_edge("E", "AE", 4)

# graph.add_edge("B", "C", 6)
# # graph.add_edge("B", "F", 8)
# graph.add_edge("B", "AB", 5)

# # graph.add_edge("C", "F", 2)
# graph.add_edge("C", "D", 4)
# graph.add_edge("D", "E", 4)
# #graph.add_edge("D", "G", 10)



MrPacMan = PacMan([3,0], "A", "B", "LEFT", graph)
RedGhost = Ghost([9,0],"A", graph,"B")
PinkGhost = Ghost([7,0],"A", graph,"B")

# Initialize pygame
pygame.init()

# Create an 800x800 window
screen = pygame.display.set_mode((800, 800))
offset = 10
scaling = 70
# Main loop
running = True

current_time = pygame.time.get_ticks()
interval = 50  # 1000 milliseconds = 1 second

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        MrPacMan.ChangeDirection("UP")
    if keys[pygame.K_DOWN]:
        MrPacMan.ChangeDirection("DOWN")
    if keys[pygame.K_LEFT]:
        MrPacMan.ChangeDirection("LEFT")
    if keys[pygame.K_RIGHT]:
        MrPacMan.ChangeDirection("RIGHT")
    if pygame.time.get_ticks() - current_time >= interval:
        MrPacMan.Move()
        RedGhost.PacManNode = MrPacMan.PrevNode
        RedGhost.PacManNodeNext = MrPacMan.NextNode

        PinkGhost.PacManNode = MrPacMan.NextNode
        PinkGhost.PacManNodeNext = MrPacMan.PrevNode
        PinkGhost.Move()
        print(RedGhost.NextNode)
        current_time = pygame.time.get_ticks()

    draw_circle(screen, [MrPacMan.CurrentCoord[0]*scaling+offset, MrPacMan.CurrentCoord[1]*scaling+offset], 10, (255, 255, 0))
    draw_circle(screen, [RedGhost.CurrentCoord[0]*scaling+offset, RedGhost.CurrentCoord[1]*scaling+offset], 10, (255, 0, 0))
    for NodeCoord in graph.get_node_coords():
        draw_circle(screen, [NodeCoord[0]*scaling+offset, NodeCoord[1]*scaling+offset], 10, (0, 255, 0))

    for Edge in graph.get_edges():
        draw_line(screen, [Edge[0][0]*scaling+offset, Edge[0][1]*scaling+offset], [Edge[1][0]*scaling+offset, Edge[1][1]*scaling+offset], (255, 0, 0))

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()