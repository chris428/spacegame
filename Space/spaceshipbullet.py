import pygame
import constants

class Spaceshipbullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, size):
        pygame.sprite.Sprite.__init__(self)
        self.width = size
        self.height = size
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopespaceshipbullet.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = speedx
        self.speedy = -constants.bulletspeed

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy