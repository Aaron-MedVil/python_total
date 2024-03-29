import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Invasion espacial")
pygame.display.set_icon(pygame.image.load('img/ovni.png'))

pj_img = pygame.image.load("img/rocket.png")
pj_x = 368
pj_y = 536
pj_x_change = 0

def player(x, y):
    screen.blit(pj_img, (x, y))

executing = True
while executing:
    screen.fill((205, 144, 228))
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            executing = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pj_x_change = -3
            if event.key == pygame.K_RIGHT:
                pj_x_change = 3
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pj_x_change = 0
    
    pj_x += pj_x_change
    
    if pj_x <= 0:
        pj_x = 0
    
    if pj_x >= 736:
        pj_x = 736
    
    player(pj_x, pj_y)
    pygame.display.update()