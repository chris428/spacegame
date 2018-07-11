import pygame
import time
import constants

class Enemybullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.ebulletwidth
        self.height = constants.ebulletheight
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopeelaser.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = speedx
        self.speedy = speedy


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy