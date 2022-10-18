import pygame, sys
from bullet import Bullet
from ino import Ino

def events(screen, gun, bullets):
    #event handling
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                """right button"""
                if event.key == pygame.K_d:
                    gun.mright = True
                elif event.key == pygame.K_a:
                    gun.mleft = True  
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                """right button"""
                if event.key == pygame.K_d:
                    gun.mright = False
                if event.key == pygame.K_a:
                    gun.mleft = False 

def update(bg_color, screen, gun, ino, bullets):
    """update screen"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ino.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """update position of bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)   

def update_inos(inos):
    """update position of monsters"""
    inos.update()

def create_army(screen, inos):
    """create army of monsters"""
    ino = Ino(screen)
    ino_withd = ino.rect.width
    number_ino_x = int((700 - 2 * ino_withd) / ino_withd)
    ino_height = ino.rect.height
    number_ino_y = int((600 - 150 - ino_height) / ino_height)
    
    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_withd + (ino_withd * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)