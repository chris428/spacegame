import pygame
import time
import constants
import spaceship
import enemybullet2
import math


class Enemytype4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.enemytype4width
        self.height = constants.enemytype4height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopeenemy4.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = constants.enemytype4speed
        self.speedy = 0
        self.timer = time.time()
        self.bullettime = constants.enemytype4bullettimer
        self.health = constants.enemytype4health

    def update(self, player, ebullets, enemies):
        distance = math.sqrt((self.rect.x - player.rect.x)**2 + (self.rect.y - player.rect.y)**2)
        xspeed = constants.enemy1bulletspeed * math.fabs(self.rect.x - player.rect.x)/distance
        yspeed = constants.enemy1bulletspeed * math.fabs(self.rect.y - player.rect.y)/distance

        xspd = constants.enemytype4speed * math.fabs(self.rect.x - player.rect.x)/distance
        yspd = constants.enemytype4speed * math.fabs(self.rect.y - player.rect.y)/distance

        if self.rect.x < player.rect.x - self.width/2 + player.width/2:
            self.rect.x  += xspd
        if self.rect.x > player.rect.x - self.width/2 + player.width/2:
            self.rect.x -= xspd
        if self.rect.y < player.rect.y - self.height:
            self.rect.y += yspd
        if self.rect.y > player.rect.y:
            self.rect.y -= yspd
        if time.time() - self.timer + 0.0 > constants.enemytype4bullettimer:
            bullet = enemybullet2.Enemybullet2(self.rect.x + self.width/2 - constants.ebulletwidth/2,
                                             self.rect.y + self.height, xspeed, yspeed * 2)
            ebullets.add(bullet)
            self.timer = time.time()