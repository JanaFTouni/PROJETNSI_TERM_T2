import pygame

#constantes du jue

TITLE = "Nuquinha"
WIDTH = 800
HEIGHT = 600
LOGO = 'media/billiard-ball.png'

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
            is_running = False
    pygame.display.update()
    
pygame.quit()
