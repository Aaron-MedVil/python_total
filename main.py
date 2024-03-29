#region Imports
import pygame, random, math
from pygame import mixer

#endregion

#region Screen properties
pygame.init()
executing = True
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invasion espacial")
pygame.display.set_icon(pygame.image.load('img/ovni.png'))
bg = pygame.image.load("img/bg.jpg")

#endregion

#region Music properties
mixer.music.load("sounds/bg.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#endregion

#region Player properties
pj_img = pygame.image.load("img/rocket.png")
pj_x = 368
pj_y = 500
pj_x_change = 0
pj_movement_factor = 2.5

#endregion

#region Enemy properties
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_total = 8
enemy_movement_factor = 1

for e in range(enemy_total):
    enemy_img.append(pygame.image.load("img/alien.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(2)
    enemy_y_change.append(50)

#endregion

#region Bullet properties
bullet_img = pygame.image.load("img/bullet.png")
bullet_fx = mixer.Sound("sounds/shoot.mp3")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 4
bullet_visibility = False

#endregion

#region Colides properties
colide_fx = mixer.Sound("sounds/hit.mp3")

#endregion

#region Score properties
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

#endregion

#region Game over properties
font_end = pygame.font.Font("freesansbold.ttf", 40)

#endregion

#region Methods
def player(x, y):
    screen.blit(pj_img, (x, y))

def enemy(x, y, enemy):
    screen.blit(enemy_img[enemy], (x, y))

def shoot(x, y):
    global bullet_visibility
    bullet_visibility = True
    screen.blit(bullet_img, (x + 24, y + 10))
  
def is_colide(x1, y1, x2, y2):
    diff = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return True if diff < 27 else False

def show_score(x, y):
    txt = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(txt, (x, y))

def txt_end():
    ff = font_end.render("GAME OVER", True, (255, 255, 255))
    screen.blit(ff, (60, 400))
    
#endregion

#region Game loop
while executing:
    screen.blit(bg, (0, 0))
    
    #region Events
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            executing = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                executing = False
            if event.key == pygame.K_LEFT:
                pj_x_change = -pj_movement_factor
            if event.key == pygame.K_RIGHT:
                pj_x_change = pj_movement_factor
            if event.key == pygame.K_SPACE:
                if not bullet_visibility:
                    bullet_fx.play()
                    bullet_x = pj_x
                    shoot(bullet_x, bullet_y)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pj_x_change = 0
    
    #endregion
    
    #region Player movement
    pj_x += pj_x_change
    
    if pj_x <= 0:
        pj_x = 0
    
    if pj_x >= 736:
        pj_x = 736
    
    player(pj_x, pj_y)
    
    #endregion
    
    #region Enemy movement
    for e in range(enemy_total):
        
        if enemy_y[e] > 450:
            for k in range(enemy_total):
                enemy_y[k] = 1000
            txt_end()
            break
        
        enemy_x[e] += enemy_x_change[e]
    
        if enemy_x[e] <= 0:
            enemy_x_change[e] = enemy_movement_factor
            enemy_y[e] += enemy_y_change[e]
        
        if enemy_x[e] >= 736:
            enemy_x_change[e] = -enemy_movement_factor
            enemy_y[e] += enemy_y_change[e]
            
        if bullet_visibility: 
            colide = is_colide(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
            if colide:
                colide_fx.play()
                score += 1
                bullet_y = 500
                bullet_visibility = False
                enemy_x[e] = random.randint(0, 736)
                enemy_y[e] = random.randint(50, 200)
            
        enemy(enemy_x[e], enemy_y[e], e)

    #endregion
    
    #region Bullet movement
    if bullet_y <= -32:
        bullet_y = 500
        bullet_visibility = False
        
    if bullet_visibility:
        shoot(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    
    #endregion
    
    #region Show score
    show_score(text_x, text_y)
    
    #endregion
    
    pygame.display.update()
    
#endregion