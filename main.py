import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Invasion espacial")
pygame.display.set_icon(pygame.image.load('img/ovni.png'))

pj_img = pygame.image.load("img/rocket.png")
pj_x = 368
pj_y = 536

def player():
    screen.blit(pj_img, (pj_x, pj_y))

executing = True
while executing:
    screen.fill((205, 144, 228))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False    
    
    player()
    pygame.display.update()