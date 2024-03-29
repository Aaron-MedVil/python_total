import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Invasion espacial")
pygame.display.set_icon(pygame.image.load('ovni.png'))

executing = True
while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    pantalla.fill((205, 144, 228))
    pygame.display.update()