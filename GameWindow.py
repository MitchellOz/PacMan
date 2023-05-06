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

graph.add_node("A2", (12, 0))
graph.add_node("B2", (9, 0))
graph.add_node("C2", (7, 0))
graph.add_node("D2", (12, 2))
graph.add_node("E2", (9, 2))
graph.add_node("F2", (8, 2))
graph.add_node("G2", (7, 2))
graph.add_node("H2", (12, 3))
graph.add_node("I2", (9, 3))
graph.add_node("J2", (8, 3))
graph.add_node("K2", (7, 3))
graph.add_node("L2", (8, 4))
graph.add_node("M2", (7, 4))
graph.add_node("N2", (9, 5))
graph.add_node("O2", (8, 5))

graph.add_edge("A2", "B2")
graph.add_edge("A2", "D2")
graph.add_edge("B2", "C2")
graph.add_edge("B2", "E2")
graph.add_edge("C2", "G2")
graph.add_edge("D2", "E2")
graph.add_edge("D2", "H2")
graph.add_edge("E2", "F2")
graph.add_edge("E2", "I2")
graph.add_edge("F2", "G2")
graph.add_edge("F2", "J2")
graph.add_edge("H2", "I2")
graph.add_edge("I2", "N2")
graph.add_edge("J2", "K2")
graph.add_edge("K2", "M2")
graph.add_edge("L2", "M2")
graph.add_edge("O2", "L2")
graph.add_edge("N2", "O2")

graph.add_edge("G", "G2")
graph.add_edge("M", "M2")

MrPacMan = PacMan([2,0], "A", "B", "LEFT", graph)
RedGhost = Ghost([6,0],"A", graph,"B")
PinkGhost = Ghost([7,0],"A", graph,"B")
OrangeGhost = Ghost([4,0],"A", graph,"B",100)
BlueGhost = Ghost([4,0],"A", graph,"B",4)

# Initialize pygame
pygame.init()

# Create an 800x800 window
screen = pygame.display.set_mode((900, 900))
offset = 10
scaling = 70
# Main loop
running = True

current_time = pygame.time.get_ticks()
interval = 5  # 1000 milliseconds = 1 second
font = pygame.font.Font(None, 36)
popup_text = "Game Over!"
text_color = (255, 255, 255)
text_render = font.render(popup_text, True, text_color)
text_rect = text_render.get_rect(center=(450, 450))

font = pygame.font.Font(None, 36)
popup_text = "You Win!"
text_color = (255, 255, 255)
text_render_win = font.render(popup_text, True, text_color)
text_rect_win = text_render.get_rect(center=(450, 450))
show_popup = False
youWin_popup = False

def is_within_range(coord1, coord2, threshold=0.1):
    x_diff = abs(coord1[0] - coord2[0])
    y_diff = abs(coord1[1] - coord2[1])
    return x_diff <= threshold and y_diff <= threshold

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

        BlueGhost.PacManNode = MrPacMan.NextNode
        BlueGhost.PacManNodeNext = MrPacMan.PrevNode

        PinkGhost.Move()
        RedGhost.Move()
        OrangeGhost.Move()
        BlueGhost.Move()


        if(is_within_range(PinkGhost.CurrentCoord, MrPacMan.CurrentCoord) or 
           is_within_range(OrangeGhost.CurrentCoord, MrPacMan.CurrentCoord) or 
           is_within_range(BlueGhost.CurrentCoord, MrPacMan.CurrentCoord) or
           is_within_range(RedGhost.CurrentCoord, MrPacMan.CurrentCoord)):
            show_popup = True
        if(MrPacMan.CurrentCoord in graph.Dots):
            graph.Dots.remove(MrPacMan.CurrentCoord)

        if(len(graph.Dots) == 0):
            youWin_popup = True
        current_time = pygame.time.get_ticks()

    draw_circle(screen, [MrPacMan.CurrentCoord[0]*scaling+offset, MrPacMan.CurrentCoord[1]*scaling+offset], 10, (255, 255, 0))
    draw_circle(screen, [RedGhost.CurrentCoord[0]*scaling+offset, RedGhost.CurrentCoord[1]*scaling+offset], 10, (255, 0, 0))
    draw_circle(screen, [PinkGhost.CurrentCoord[0]*scaling+offset, PinkGhost.CurrentCoord[1]*scaling+offset], 10, (209, 93, 154))
    draw_circle(screen, [OrangeGhost.CurrentCoord[0]*scaling+offset, OrangeGhost.CurrentCoord[1]*scaling+offset], 10, (255, 191, 0))
    draw_circle(screen, [BlueGhost.CurrentCoord[0]*scaling+offset, BlueGhost.CurrentCoord[1]*scaling+offset], 10, (0, 0, 255))

    for dot in graph.Dots:
        draw_circle(screen, [dot[0]*scaling+offset, dot[1]*scaling+offset], 4, (255, 255, 255))

    for NodeCoord in graph.get_node_coords():
        #draw_circle(screen, [NodeCoord[0]*scaling+offset, NodeCoord[1]*scaling+offset], 10, (0, 255, 0))
        pass
    for Edge in graph.get_edges():
        draw_line(screen, [Edge[0][0]*scaling+offset, Edge[0][1]*scaling+offset], [Edge[1][0]*scaling+offset, Edge[1][1]*scaling+offset], (255, 0, 0))
    if show_popup:
        screen.blit(text_render, text_rect)
    if youWin_popup:
        screen.blit(text_render_win, text_rect_win)
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()