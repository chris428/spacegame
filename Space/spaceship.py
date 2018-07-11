import pygame
import constants

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.spaceshipwidth
        self.height = constants.spaceshipheight
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = constants.size[0]/2
        self.rect.y = constants.size[1]/2
        self.image = pygame.image.load("dopespaceship.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = 0
        self.speedy = 0
        self.powerlevel = 0

    def update(self):

        #spaceship perimeter check
        if self.rect.x + self.speedx > constants.size[0] - self.width or self.rect.x + self.speedx < 0:
            self.speedx = 0
        if self.rect.y + self.speedy > constants.size[1] - self.height or self.rect.y + self.speedy < 0:
            self.speedy = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy


