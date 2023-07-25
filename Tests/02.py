import pygame
from pygame.locals import *

#constantes du jue

TITLE = "Nuquinha"
w = 800
h = 600
LOGO = 'media/billiard-ball.png'

#initialisateur
pygame.init()

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((w, h))
logo = pygame.image.load(LOGO)
pygame.display.set_icon(logo)

#Update
img = pygame.image.load("media/ball20x20.png")
img.convert()
forme = img.get_rect()
forme.center = w//2, h//2

rect_list = []
moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
        elif event.type == MOUSEBUTTONUP:
            moving = False
            ball = img.get_rect()
            ball.center = event.pos
            rect_list.append(ball)

    screen.fill((0, 255, 0))
    
    for ballon in rect_list:
        pygame.draw.rect(screen, (255, 0, 0), ballon, 3)
        screen.blit(img, ballon)
    pygame.display.update()
    
pygame.quit()
