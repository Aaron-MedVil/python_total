import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

executing = True

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False