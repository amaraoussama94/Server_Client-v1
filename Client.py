# client
import pygame
from network import Network
from player import Player

width = 500
height = 500

def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True

    n = Network()  # connecting to the server
    p = n.get_p()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p, p2)

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("client")
main()

