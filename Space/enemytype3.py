import pygame
import time
import constants
import spaceship
import enemybullet
import math


class Enemytype3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = constants.enemytype3width
        self.height = constants.enemytype3height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("dopeenemy3.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speedx = constants.enemytype3speed
        self.speedy = constants.enemytype3speed
        self.timer = time.time()
        self.bullettime = constants.enemytype3bullettimer
        self.health = 1

    def update(self, player, ebullets, enemies):
        self.rect.x += self.speedx
        if self.speedx > 3:
            self.speedx -= 1
        self.rect.y += self.speedy
        if self.speedy > 2:
            self.speedy -= 1
        if self.speedx < 0 and self.rect.x + self.width < 0:
            enemies.remove(self)
        if self.speedx > 0 and self.rect.x > constants.size[0]:
            enemies.remove(self)

        distance = math.sqrt((self.rect.x - player.rect.x)**2 + (self.rect.y - player.rect.y)**2)
        xspeed = constants.enemy1bulletspeed * math.fabs(self.rect.x - player.rect.x)/distance
        yspeed = constants.enemy1bulletspeed * math.fabs(self.rect.y - player.rect.y)/distance

        if time.time() - self.timer + 0.0 > constants.enemytype3bullettimer:
            bullet = enemybullet.Enemybullet(self.rect.x + self.width/2 - constants.ebulletwidth/2,
                                             self.rect.y + self.height, xspeed, yspeed)
            ebullets.add(bullet)
            self.timer = time.time()