import pygame
import time
import constants
import spaceship
import enemybullet
import math


class Enemytype1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.enemytype1width
        self.height = constants.enemytype1height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopeenemy1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = constants.enemytype1speed
        self.speedy = 0
        self.timer = time.time()
        self.bullettime = constants.enemytype1bullettimer
        self.health = constants.enemytype1health

    def update(self, player, ebullets, enemies):
        if self.rect.x < player.rect.x - self.width/2 + player.width/2:
            self.rect.x  += constants.enemytype1speed
        if self.rect.x > player.rect.x - self.width/2 + player.width/2:
            self.rect.x -= constants.enemytype1speed
        if self.rect.y < player.rect.y - player.height * 2:
            self.rect.y += constants.enemytype1speed/2
        if self.rect.y > player.rect.y - player.height * 2:
            self.rect.y -= constants.enemytype1speed/2

        distance = math.sqrt((self.rect.x - player.rect.x)**2 + (self.rect.y - player.rect.y)**2)
        xspeed = constants.enemy1bulletspeed * math.fabs(self.rect.x - player.rect.x)/distance
        yspeed = constants.enemy1bulletspeed * math.fabs(self.rect.y - player.rect.y)/distance

        if time.time() - self.timer + 0.0 > constants.enemytype1bullettimer:
            bullet = enemybullet.Enemybullet(self.rect.x + self.width/2 - constants.ebulletwidth/2,
                                             self.rect.y + self.height, xspeed, yspeed)
            ebullets.add(bullet)
            self.timer = time.time()