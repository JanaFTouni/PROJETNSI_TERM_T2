import pygame
import sys

#constantes du jue

TITLE = "Nuquinha"
WIDTH = 800
HEIGHT = 600
LOGO = 'billiard-ball.png'

#initialisateur

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
logo = pygame.image.load(LOGO)
pygame.display.set_icon(logo)

#Update

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
