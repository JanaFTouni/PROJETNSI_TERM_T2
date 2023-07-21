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
running = True 
while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT(): # verifier si on a cliker quitter 
            running = False 
 
