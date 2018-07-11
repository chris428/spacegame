import pygame
import time
import constants
import random

class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.powerupwidth
        self.height = constants.powerupheight
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = random.randint(0, constants.size[0] - self.width)
        self.rect.y = random.randint(0, constants.size[1] - self.height)
        self.image = pygame.image.load("dopepowerup.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = random.randint(-constants.powerupspeed, constants.powerupspeed)
        while self.speedx == 0:
            self.speedx = random.randint(-constants.powerupspeed, constants.powerupspeed)
        self.speedy = random.randint(-constants.powerupspeed, constants.powerupspeed)
        while self.speedy == 0:
            self.speedy = random.randint(-constants.powerupspeed, constants.powerupspeed)

    def update(self):

        if self.rect.x + self.speedx >= constants.size[0] - self.width or self.rect.x + self.speedx <= 0:
            self.speedx = -self.speedx
        self.rect.x += self.speedx

        if self.rect.y + self.speedy >= constants.size[1] - self.height or self.rect.y + self.speedy <= 0:
            self.speedy = -self.speedy
        self.rect.y += self.speedy
