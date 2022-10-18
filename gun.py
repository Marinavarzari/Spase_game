import pygame

class Gun():

    def __init__(self, screen):
        """инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load('/Users/marinavarzari/Documents/Game_1/images_1/img2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """draw gun"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """update poition"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.mleft and self.rect.left > 0 :
            self.center -= 1   
        self.rect.centerx = self.center 